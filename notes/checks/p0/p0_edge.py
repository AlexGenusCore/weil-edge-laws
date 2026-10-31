"""Independent referee check of the Hadamard constant: piecewise-constant (P0) Galerkin.

P0 functions lie in the form domain of an order-zero form (a jump costs only a log),
so this is a conforming method, independent of the project's earlier hp-FEM.
Cells are stored by distance r from their own edge, so the edge mesh can go down to
r ~ 1e-150 (ell ~ 345) without losing digits.

Models (all on (-L, L)):
  'log'  : Q = (1/2pi) int log|t| |F|^2
         = sum_{i<j} J_ij (f_i-f_j)^2 + sum K_i f_i^2 - (gamma + log 2L) ||f||^2,
           kernel 1/(2|u|) truncated at 2L (exact, see report).
  'weil' : Q = E_J + c||f||^2 - 2 sum_{log n<2L} Lambda(n)/sqrt(n) g(log n) + 2 s F(i/2)F(-i/2),
           J(u) = e^{-u/2}/(1-e^{-2u}), c = psi(1/4) - log pi.
Usage: python p0_edge.py  (runs self-check + the experiments printed in the report)
"""
import sys
import numpy as np

EG = 0.57721566490153286061
GX, GW = np.polynomial.legendre.leggauss(10)
GX = 0.5 * (GX + 1); GW = 0.5 * GW          # nodes on [0,1]
G3X, G3W = np.polynomial.legendre.leggauss(4)
G3X = 0.5 * (G3X + 1); G3W = 0.5 * G3W


def mesh(L, h0, rho, rmin):
    """half-mesh breakpoints in r (distance from own edge), 0 < ... < L:
    geometric with ratio rho from rmin until the step reaches h0, then uniform."""
    br = [0.0, rmin]
    r = rmin
    while r < L:
        r = r + min((rho - 1) * r, h0)
        br.append(r)
    br = np.array(br)
    if L - br[-2] < 0.5 * min((rho - 1) * br[-2], h0):
        br = br[:-1]
    br[-1] = L
    return br


def cells(L, h0, rho, rmin):
    br = mesh(L, h0, rho, rmin)
    r1, r2 = br[:-1], br[1:]
    n = len(r1)
    # left side (side=-1) ordered from x=-L to 0, right side (side=+1) from 0 to L
    side = np.concatenate([-np.ones(n), np.ones(n)])
    R1 = np.concatenate([r1, r1[::-1]])
    R2 = np.concatenate([r2, r2[::-1]])
    return side, R1, R2


def xcoords(L, side, R1, R2):
    a = np.where(side < 0, -L + R1, L - R2)
    b = np.where(side < 0, -L + R2, L - R1)
    return a, b


def j_pair(hs, g, hb):
    """int over two cells (sizes hs<=hb, gap g) of 1/(2|x-y|)."""
    out = np.empty_like(g)
    far = g >= hs
    if far.any():
        gg, s, b = g[far], hs[far], hb[far]
        z = gg[:, None] + s[:, None] * GX[None, :]
        out[far] = s * (0.5 * np.log1p(b[:, None] / z) @ GW)
    nr = ~far
    if nr.any():
        gg, s, b = g[nr], hs[nr], hb[nr]
        S = gg + s + b
        F = lambda u: np.where(u > 0, u * np.log(np.where(u > 0, u, 1.0)), 0.0)
        out[nr] = 0.5 * S * (-F((gg + b) / S) - F((gg + s) / S) + F(gg / S))
    return out


def Jfull(u):
    return np.exp(-u / 2) / (-np.expm1(-2 * u))


def Jr(u):
    """J(u) - 1/(2u), smooth."""
    small = u < 1e-3
    out = np.empty_like(u)
    us = u[small]
    out[small] = 0.25 - us / 48 - us**2 / 32 + 7 * us**3 / 11520
    ub = u[~small]
    out[~small] = Jfull(ub) - 0.5 / ub
    return out


def RT(r):
    """T(r) = int_r^inf J = artanh(e^{-r/2}) + arctan(e^{-r/2}) = -(1/2)log r + RT(r)."""
    e = np.exp(-r / 2)
    return 0.5 * np.log1p(e) - 0.5 * np.log(-np.expm1(-r / 2) / r) + np.arctan(e)


def Tfull(r):
    e = np.exp(-r / 2)
    return 0.5 * np.log((1 + e) / (-np.expm1(-r / 2))) + np.arctan(e)


def int_mlog(r1, r2):
    """int_{r1}^{r2} -(1/2) log r dr"""
    F = lambda r: np.where(r > 0, r - r * np.log(np.where(r > 0, r, 1.0)), 0.0)
    return 0.5 * (F(r2) - F(r1))


def primes_upto(N):
    out = []
    for n in range(2, N + 1):
        m, p = n, None
        for q in range(2, n + 1):
            if m % q == 0:
                p = q
                break
        while m % p == 0:
            m //= p
        if m == 1:
            out.append((n, np.log(p)))
    return out


def assemble(L, model='weil', s=1.0, h0=None, rho=2.0, rmin=1e-150):
    if h0 is None:
        h0 = L / 250
    side, R1, R2 = cells(L, h0, rho, rmin)
    N = len(side)
    h = R2 - R1
    Q = np.zeros((N, N))
    for i in range(N):
        j = np.arange(i + 1, N)
        same = side[j] == side[i]
        g = np.where(same, np.maximum(R1[j] - R2[i], R1[i] - R2[j]), 2 * L - R2[i] - R2[j])
        g = np.maximum(g, 0.0)
        hs = np.minimum(h[i], h[j]); hb = np.maximum(h[i], h[j])
        Jij = j_pair(hs, g, hb)
        if model == 'weil':
            # smooth part J_r by 4x4 Gauss product; |x-y| = g + z_i + z_j
            u = g[:, None, None] + h[i] * G3X[None, :, None] + h[j][:, None, None] * G3X[None, None, :]
            Jij = Jij + h[i] * h[j] * np.einsum('kab,a,b->k', Jr(u), G3W, G3W)
        Q[i, j] = -Jij
        Q[j, i] = -Jij
    Q[np.diag_indices(N)] = -Q.sum(axis=1)       # sum_{j != i} J_ij
    # killing + constant
    if model == 'log':
        # kappa = (1/2)[log 2L - log r + log 2L - log(2L - r)]
        r = R1[:, None] + h[:, None] * GX[None, :]
        K = int_mlog(R1, R2) + h * np.log(2 * L) - 0.5 * h * (np.log(2 * L - r) @ GW)
        Q[np.diag_indices(N)] += K - (EG + np.log(2 * L)) * h
    else:
        r = R1[:, None] + h[:, None] * GX[None, :]
        K = int_mlog(R1, R2) + h * (RT(r) @ GW) + h * (Tfull(2 * L - r) @ GW)
        c = -EG - np.pi / 2 - 3 * np.log(2) - np.log(np.pi)
        Q[np.diag_indices(N)] += K + c * h
        a, b = xcoords(L, side, R1, R2)
        for n, lam in primes_upto(int(np.exp(2 * L)) + 1):
            tau = np.log(n)
            if tau >= 2 * L:
                continue
            cn = lam / np.sqrt(n)
            # O_ij = |c_i cap (c_j + tau)|
            lo = np.maximum(a[:, None], a[None, :] + tau)
            hi = np.minimum(b[:, None], b[None, :] + tau)
            O = np.maximum(hi - lo, 0.0)
            # exact lengths for containment (tiny cells)
            inside_j = (a[None, :] + tau >= a[:, None]) & (b[None, :] + tau <= b[:, None])
            inside_i = (a[:, None] >= a[None, :] + tau) & (b[:, None] <= b[None, :] + tau)
            O = np.where(inside_j, h[None, :] * np.ones((N, 1)), O)
            O = np.where(inside_i, h[:, None] * np.ones((1, N)), O)
            Q -= cn * (O + O.T)
        if s != 0:
            xm = 0.5 * (a + b)
            va = 2 * np.exp(-xm / 2) * np.sinh(h / 4) * 2   # int e^{-x/2} = 4 e^{-xm/2} sinh(h/4)
            vb = 2 * np.exp(xm / 2) * np.sinh(h / 4) * 2
            Q += s * (np.outer(va, vb) + np.outer(vb, va))
    return Q, h, side, R1, R2


def eig(Q, h, k=4, parity=None, side=None):
    d = 1 / np.sqrt(h)
    S = Q * d[:, None] * d[None, :]
    w, V = np.linalg.eigh(S)
    res = []
    B = Q / h[:, None]
    N = len(h)
    for m in range(len(w)):
        f = V[:, m] * d
        f[h < 1e-12] = 0.0     # eigh components there are rounding noise / sqrt(h)
        # parity: compare with mirror (cells are mirror-ordered)
        par = 'e' if np.dot(f, h * f[::-1]) > 0 else 'o'
        if parity is not None and par != parity:
            continue
        # inverse iteration in row-scaled form for accurate tiny-cell values
        mu = w[m] * (1 - 1e-13) - 1e-13
        for _ in range(4):
            f = np.linalg.solve(B - mu * np.eye(N), f)
            f /= np.sqrt(np.dot(h, f * f))
        if f[-1] < 0:
            f = -f
        lam = np.dot(f, Q @ f)
        r = np.abs(B @ f - lam * f).max()
        assert r < 1e-8, ('inverse iteration failed', r)
        res.append((lam, f, par))
        if len(res) >= k:
            break
    return res


def edge_fit(f, side, R1, R2, lmin=8.0, nterm=4):
    sel = (side > 0) & (R1 > 0)
    r = np.sqrt(R1[sel] * R2[sel])
    ell = -np.log(r)
    y = f[sel] * np.sqrt(ell)
    m = ell >= lmin
    X = np.stack([ell[m] ** (-k) for k in range(nterm)], axis=1)
    coef, *_ = np.linalg.lstsq(X, y[m], rcond=None)
    resid = np.max(np.abs(X @ coef - y[m]))
    return coef, resid, ell, y


def selfcheck():
    u = np.array([1e-3 * 0.999, 1e-3 * 1.001, 0.01, 0.3])
    a = Jr(u)
    assert abs(a[0] - a[1]) < 1e-6, a
    assert abs(Jr(np.array([0.01]))[0] - (Jfull(np.array([0.01]))[0] - 50)) < 1e-12
    # T(r) = int_r^inf J numerically
    import mpmath as mp
    for r in (0.05, 0.7):
        num = mp.quad(lambda t: mp.exp(-t / 2) / (1 - mp.exp(-2 * t)), [r, 1, mp.inf])
        assert abs(float(num) - Tfull(np.array([r]))[0]) < 1e-12
        assert abs(Tfull(np.array([r]))[0] - (-0.5 * np.log(r) + RT(np.array([r]))[0])) < 1e-12
    # j_pair: near and far branches agree, and match mpmath
    for hs, g, hb in ((0.1, 0.1, 0.2), (0.1, 0.0999999, 0.2), (0.3, 0.0, 0.5)):
        A = j_pair(np.array([hs]), np.array([g]), np.array([hb]))[0]
        B = float(mp.quad(lambda x: mp.quad(lambda y: 0.5 / (y - x), [hs + g, hs + g + hb]), [0, hs]))
        assert abs(A - B) < 1e-10 * B, (hs, g, hb, A, B)
    print('selfcheck ok')


def position_side_check(L=0.45, s=1.0):
    """Compare the P0 matrix with the paper's position-side formula on a coarse mesh."""
    import mpmath as mp
    mp.mp.dps = 30
    n = 18
    Q, h, side, R1, R2 = assemble(L, 'weil', s, h0=L / (n // 2), rho=2.0, rmin=L / (n // 2))
    # mesh is uniform here (rmin above h0): verify
    a, b = xcoords(L, side, R1, R2)
    assert np.allclose(h, h[0])
    H = h[0]
    rng = np.random.default_rng(1)
    f = rng.standard_normal(len(h))
    lhs = f @ Q @ f
    N = len(f)
    gk = [H * sum(f[i] * f[i - k] for i in range(k, N)) for k in range(N + 1)]
    gk += [0.0]

    def g(x):
        k = int(mp.floor(x / H))
        t = x / H - k
        if k >= N:
            return mp.mpf(0)
        # autocorrelation of P0 f is piecewise linear on the H-grid
        return (1 - t) * gk[k] + t * gk[k + 1]
    pts = [k * H for k in range(N + 1)]
    pole = 4 * mp.quad(lambda x: g(x) * mp.cosh(x / 2), pts)
    g0 = gk[0]
    integ = mp.quad(lambda x: 2 * (mp.exp(-2 * x) * g0 - mp.exp(-x / 2) * g(x)) / (1 - mp.exp(-2 * x)), pts)
    primes = 0
    for nn, lam in primes_upto(int(np.exp(2 * L)) + 1):
        if np.log(nn) < 2 * L:
            primes += 2 * lam / mp.sqrt(nn) * g(mp.log(nn))
    rhs = s * pole - g0 * (mp.log(mp.pi) + mp.euler + mp.log(1 - mp.exp(-4 * L))) + integ - primes
    print(f'position-side check L={L} s={s}: matrix {lhs:.12f}  paper {float(rhs):.12f}  diff {lhs-float(rhs):.2e}')


if __name__ == '__main__':
    selfcheck()
    position_side_check()
