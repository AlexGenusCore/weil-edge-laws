"""Edge-resolving discretisation of Weil's Q on [-L, L]: discontinuous piecewise polynomials (degree p) on a mesh
geometrically graded toward +-L and toward the interior singular points (closure of {+-L} under prime shifts).

Q(f) = 1/4 int int_{sq} (f(u)-f(v))^2/|u-v| + 1/2 int f^2 kappa1          [1/x part of the archimedean jump kernel]
       - 1/2 int int R(|u-v|) f f + (C_L + R_tot) |f|^2                    [J = 1/x + R, R analytic]
       + 2 s int int cosh((u-v)/2) f f - sum Lambda(n)/sqrt n * 2 int f(u) f(u + log n)
with kappa1(u) = log(2L/(L-u)) + log(2L/(L+u)).  Discontinuous polynomials are conforming (H^log form domain).
Within one cell [a,b] the 1/x part reduces to the reference matrix S1 + 1/2 log(4L^2/((u-a)(b-u))) weight.
Off-diagonal cell blocks: -1/2 int int J(|u-v|) phi phi, computed with geometrically graded composite Gauss for near pairs.
"""
import numpy as np
import mpmath as mp

mp.mp.dps = 50
GL = {n: np.polynomial.legendre.leggauss(n) for n in (8, 24, 40)}


def legn(p, t):  # orthonormal Legendre Pbar_0..Pbar_p on [-1,1], shape (p+1, len(t))
    t = np.asarray(t, float)
    P = np.empty((p + 1,) + t.shape)
    P[0] = 1
    if p >= 1:
        P[1] = t
    for k in range(1, p):
        P[k + 1] = ((2 * k + 1) * t * P[k] - k * P[k - 1]) / (k + 1)
    return P * np.sqrt((2 * np.arange(p + 1) + 1) / 2)[:, None]


def J(t):  # 2 e^{-t/2}/(1 - e^{-2t}), t > 0
    return 2 * np.exp(-t / 2) / (-np.expm1(-2 * t))


def _Rcoef(K=30):  # R(t) = J(t) - 1/t = sum_{k>=1} a_k t^{k-1},  t J(t) = e^{-t/2} * x/(1-e^{-x}), x = 2t
    b = [mp.bernoulli(k) * (-2) ** k / mp.factorial(k) for k in range(K + 1)]
    e = [(-mp.mpf(1) / 2) ** k / mp.factorial(k) for k in range(K + 1)]
    a = [mp.fsum(b[i] * e[k - i] for i in range(k + 1)) for k in range(K + 1)]
    return np.array([float(x) for x in a[1:]])


RC = _Rcoef()


def R(t):
    t = np.asarray(t, float)
    out = np.empty_like(t)
    sm = t < 0.2
    out[sm] = np.polynomial.polynomial.polyval(t[sm], RC)
    out[~sm] = J(t[~sm]) - 1 / t[~sm]
    return out


def constants(L):
    L = mp.mpf(L)
    Jm = lambda x: 2 * mp.exp(-x / 2) / (1 - mp.exp(-2 * x))
    CL = -(mp.log(mp.pi) + mp.euler + mp.log(1 - mp.exp(-4 * L))) + mp.quad(
        lambda x: 2 * mp.exp(-2 * x) / (1 - mp.exp(-2 * x)) - Jm(x), [0, 2 * L])
    Rt = mp.quad(lambda x: Jm(x) - 1 / x, [0, 2 * L])
    return float(CL + Rt)


_REF = {}


def reference(p):
    """S1_ab = 1/4 int int (Pa(t)-Pa(t'))(Pb(t)-Pb(t'))/|t-t'|,  Lg_ab = int Pa Pb (log(1-t)+log(1+t))."""
    if p in _REF:
        return _REF[p]
    n = p + 6
    x, w = np.polynomial.legendre.leggauss(n)
    T, W = np.meshgrid(x, (x + 1) / 2, indexing="ij")  # t, w in [0,1]
    wt = np.outer(w, w / 2) * (T + 1)
    Tp = T - (T + 1) * W  # t' < t, t - t' = (t+1) w
    # divided differences dP_k = (P_k(t)-P_k(t'))/(t-t') via the three-term recurrence
    Pt, Pp = [np.ones_like(T), T], [np.ones_like(T), Tp]
    dP = [np.zeros_like(T), np.ones_like(T)]
    for k in range(1, p):
        Pt.append(((2 * k + 1) * T * Pt[k] - k * Pt[k - 1]) / (k + 1))
        Pp.append(((2 * k + 1) * Tp * Pp[k] - k * Pp[k - 1]) / (k + 1))
        dP.append(((2 * k + 1) * (Pt[k] + Tp * dP[k]) - k * dP[k - 1]) / (k + 1))
    nrm = np.sqrt((2 * np.arange(p + 1) + 1) / 2)
    dP = np.array(dP[:p + 1]) * nrm[:, None, None]
    S1 = 0.5 * np.einsum("aij,bij,ij->ab", dP, dP, wt * (T - Tp))  # 1/4 * 2 triangles
    mp.mp.dps = 30
    Lg = np.zeros((p + 1, p + 1))
    for a in range(p + 1):
        for b in range(a, p + 1, 2):
            f = lambda t: mp.legendre(a, t) * mp.legendre(b, t) * mp.sqrt((2 * a + 1) * (2 * b + 1)) / 2
            Lg[a, b] = Lg[b, a] = float(2 * mp.quad(lambda t: f(t) * mp.log(1 + t), [-1, 0, 1]))
    mp.mp.dps = 50
    _REF[p] = (S1, Lg)
    return _REF[p]


def anchors(L):
    """Closure of {+-L} under shifts by +-log n (n prime power, log n < 2L), inside [-L, L]."""
    Lm = mp.mpf(L)
    ells = [mp.log(n) for n in range(2, int(np.exp(2 * L)) + 2) if mp.log(n) < 2 * Lm and len(_pf(n)) == 1]
    pts = [Lm, -Lm]
    todo = list(pts)
    while todo:
        x = todo.pop()
        for e in ells:
            for y in (x + e, x - e):
                if -Lm < y < Lm and all(abs(y - z) > mp.mpf(10) ** -30 for z in pts):
                    pts.append(y); todo.append(y)
    return sorted(pts)


def _pf(n):
    return {d for d in range(2, n + 1) if n % d == 0 and all(d % q for q in range(2, d))}


def primes_list(L):
    out = []
    for n in range(2, int(np.exp(2 * L)) + 2):
        if np.log(n) < 2 * L and len(_pf(n)) == 1:
            pr = next(iter(_pf(n)))
            out.append((mp.log(n), float(np.log(pr) / np.sqrt(n))))
    return out


def mesh(L, H=0.05, sig=0.25, dmin=1e-14, dint=1e-10):
    """Breakpoints (mp): base points {anchors, 0}, uniform refinement to size <= H, geometric grading toward
    +-L (down to dmin) and to both sides of each interior anchor (down to dint).  Symmetric about 0."""
    A = anchors(L)
    base = sorted(set(A) | {mp.mpf(0)})
    pts = set(base)
    for lo, hi in zip(base, base[1:]):
        k = int(np.ceil(float(hi - lo) / H))
        pts |= {lo + (hi - lo) * i / k for i in range(1, k)}
    pts = sorted(pts)
    out = set(pts)
    for i, x in enumerate(pts):
        if x not in A:
            continue
        lim = dmin if abs(abs(x) - mp.mpf(L)) < 1e-30 else dint
        for nb in (pts[i - 1] if i > 0 else None, pts[i + 1] if i + 1 < len(pts) else None):
            if nb is None:
                continue
            d = abs(nb - x) * sig
            while d > lim:
                out.add(x + mp.sign(nb - x) * d)
                d *= sig
    out = sorted(out)
    # enforce exact symmetry
    pos = [x for x in out if x > 0]
    return sorted([-x for x in pos] + [mp.mpf(0)] + pos)


def graded_nodes(h, sig=0.5, K=48, n=8):  # nodes in (0, h), graded toward 0
    x, w = GL[n]
    xs, ws = [], []
    edges = [h * sig ** k for k in range(K + 1)] + [0.0]
    for hi, lo in zip(edges, edges[1:]):
        xs.append(lo + (hi - lo) * (x + 1) / 2); ws.append(w * (hi - lo) / 2)
    return np.concatenate(xs), np.concatenate(ws)


def assemble(L, p, pts):
    """Return A0 (Q at s=0), pole vectors c, sv (Q_s = A0 + 2s(cc^T - sv sv^T)), element data."""
    ne = len(pts) - 1
    a = pts[:-1]; b = pts[1:]
    r = np.array([float((bb - aa) / 2) for aa, bb in zip(a, b)])
    m = [(aa + bb) / 2 for aa, bb in zip(a, b)]
    N = ne * (p + 1)
    A = np.zeros((N, N))
    S1, Lg = reference(p)
    ctot = constants(L)
    # same-cell blocks
    xq, wq = GL[24]
    T, Wd = np.meshgrid(xq, (xq + 1) / 2, indexing="ij")
    wt = np.outer(wq, wq / 2) * (T + 1)
    Tp = T - (T + 1) * Wd
    PT, PP = legn(p, T.ravel()), legn(p, Tp.ravel())
    for i in range(ne):
        Rk = R(r[i] * (T + 1) * Wd).ravel() * wt.ravel()
        M = PT @ (Rk[:, None] * PP.T)
        Rblk = -0.5 * r[i] * (M + M.T)
        blk = S1 + 0.5 * np.log(4 * L * L / r[i] ** 2) * np.eye(p + 1) - 0.5 * Lg + Rblk + ctot * np.eye(p + 1)
        A[i * (p + 1):(i + 1) * (p + 1), i * (p + 1):(i + 1) * (p + 1)] = blk
    # off-diagonal blocks: -1/2 int int J(|u-v|) phi phi; i to the right of j; u = a_i + x, v = b_j - y
    xf, wf = GL[24]
    for i in range(ne):
        for j in range(i):
            gap = float(a[i] - b[j])
            near = gap < max(r[i], r[j])
            if near:
                x, wx = graded_nodes(2 * r[i]); y, wy = graded_nodes(2 * r[j])
            else:
                x, wx = r[i] * (xf + 1), r[i] * wf; y, wy = r[j] * (xf + 1), r[j] * wf
            K = J(gap + x[:, None] + y[None, :])
            Pi = legn(p, x / r[i] - 1) * wx / np.sqrt(r[i])
            Pj = legn(p, 1 - y / r[j]) * wy / np.sqrt(r[j])
            blk = -0.5 * Pi @ K @ Pj.T
            A[i * (p + 1):(i + 1) * (p + 1), j * (p + 1):(j + 1) * (p + 1)] += blk
            A[j * (p + 1):(j + 1) * (p + 1), i * (p + 1):(i + 1) * (p + 1)] += blk.T
    # primes: -coef * (int phi_i(u) phi_j(u+l) + transpose)
    xg, wg = GL[24]
    for ell, coef in primes_list(L):
        for i in range(ne):
            for j in range(ne):
                lo, hi = max(a[i], a[j] - ell), min(b[i], b[j] - ell)
                if hi <= lo:
                    continue
                hw, md = (hi - lo) / 2, (hi + lo) / 2
                ti = np.array([float((md - m[i]) / r[i])]) + float(hw / r[i]) * xg
                tj = np.array([float((md + ell - m[j]) / r[j])]) + float(hw / r[j]) * xg
                blk = (legn(p, ti) * wg) @ legn(p, tj).T * float(hw) / np.sqrt(r[i] * r[j])
                A[i * (p + 1):(i + 1) * (p + 1), j * (p + 1):(j + 1) * (p + 1)] -= coef * blk
                A[j * (p + 1):(j + 1) * (p + 1), i * (p + 1):(i + 1) * (p + 1)] -= coef * blk.T
    c = np.zeros(N); sv = np.zeros(N)
    x40, w40 = GL[40]
    for i in range(ne):
        u = float(m[i]) + r[i] * x40
        Pw = legn(p, x40) * w40 * np.sqrt(r[i])
        c[i * (p + 1):(i + 1) * (p + 1)] = Pw @ np.cosh(u / 2)
        sv[i * (p + 1):(i + 1) * (p + 1)] = Pw @ np.sinh(u / 2)
    return A, c, sv, dict(a=a, b=b, r=r, m=m, p=p, ne=ne)


def parity_basis(el):
    """Columns: orthonormal even / odd combinations (cell i>0 with its mirror)."""
    p, ne = el["p"], el["ne"]
    h = ne // 2  # cells h..ne-1 are on the right; mirror of cell i is ne-1-i
    N = ne * (p + 1)
    E = np.zeros((N, h * (p + 1))); O = np.zeros((N, h * (p + 1)))
    for k, i in enumerate(range(h, ne)):
        im = ne - 1 - i
        for q in range(p + 1):
            col = k * (p + 1) + q
            # phi_q on mirror cell at -u equals (-1)^q phi_q on cell i at u
            E[i * (p + 1) + q, col] = O[i * (p + 1) + q, col] = 1 / np.sqrt(2)
            E[im * (p + 1) + q, col] = (-1) ** q / np.sqrt(2)
            O[im * (p + 1) + q, col] = -(-1) ** q / np.sqrt(2)
    return E, O


class Model:
    def __init__(self, L, p=8, **mk):
        self.L = L
        self.pts = mesh(L, **mk)
        A, c, sv, el = assemble(L, p, self.pts)
        self.el = el
        E, O = parity_basis(el)
        self.E, self.O = E, O
        self.Ae, self.Ao = E.T @ A @ E, O.T @ A @ O
        self.ce, self.so = E.T @ c, O.T @ sv
        self.asym = np.abs(E.T @ A @ O).max()
        self.N = A.shape[0]

    def even(self, s, k=1):
        w, V = np.linalg.eigh(self.Ae + 2 * s * np.outer(self.ce, self.ce))
        return w[:k], V[:, :k]

    def odd(self, s, k=1):
        w, V = np.linalg.eigh(self.Ao - 2 * s * np.outer(self.so, self.so))
        return w[:k], V[:, :k]

    def values(self, vec, parity="e"):
        """Right-half function values: list of (cell index, t-grid, psi) with psi normalised so that psi(0+) > 0
        is NOT assumed; returns coefficients per right cell."""
        p = self.el["p"]
        return vec.reshape(-1, p + 1) / np.sqrt(2)  # coefficients on right cells h..ne-1 (orthonormal phi)

    def evalright(self, vec, ts=np.linspace(-1, 1, 9)):
        """psi at points of every right cell: returns (u-L distance d as float, psi), using mp distances."""
        p, ne = self.el["p"], self.el["ne"]
        C = self.values(vec)
        P = legn(p, ts)
        ds, ps = [], []
        Lm = mp.mpf(self.L)
        for k, i in enumerate(range(ne // 2, ne)):
            r = self.el["r"][i]
            ps.append(C[k] @ P / np.sqrt(r))
            ds.append([float(Lm - self.el["m"][i]) - r * t for t in ts])
        return np.array(ds), np.array(ps)

    def edge(self, vec):  # psi(L-) from the last cell (t = 1)
        p = self.el["p"]
        C = self.values(vec)
        return C[-1] @ legn(p, [1.0])[:, 0] / np.sqrt(self.el["r"][-1])


class Secular:
    """Rank-one-per-sector updates: even Ae + 2s ce ce^T, odd Ao - 2s so so^T, via the secular equation (s > 0)."""

    def __init__(self, M):
        self.M = M
        self.me, self.Ue = np.linalg.eigh(M.Ae); self.ze = self.Ue.T @ M.ce
        self.mo, self.Uo = np.linalg.eigh(M.Ao); self.zo = self.Uo.T @ M.so

    @staticmethod
    def _root(mu, z, a):
        f = lambda lam: 1 + a * np.sum(z * z / (mu - lam))
        if a > 0:
            lo, hi = mu[0], mu[1]
        else:
            lo, hi = mu[0] + a * np.sum(z * z) - 1, mu[0]
        for _ in range(200):
            mid = (lo + hi) / 2
            if mid in (lo, hi): break
            if (f(mid) > 0) == (a > 0): hi = mid
            else: lo = mid
        return (lo + hi) / 2

    def even(self, s):
        lam = self._root(self.me, self.ze, 2 * s)
        y = self.ze / (self.me - lam); v = self.Ue @ y
        return lam, v / np.linalg.norm(v)

    def odd(self, s):
        lam = self._root(self.mo, self.zo, -2 * s)
        y = self.zo / (self.mo - lam); v = self.Uo @ y
        return lam, v / np.linalg.norm(v)
