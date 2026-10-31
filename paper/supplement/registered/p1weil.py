"""Independent P1 (continuous piecewise-linear) Galerkin solver for the localized Weil form.

Written from scratch for the `numerics` role (2026-10-31).  Shares nothing with the project's
solvers except the form definition:

  Q_L(f) = E_J(f) + c ||f||^2 - 2 sum_{n < X} c_n R_f(log n) + 2 s F(i/2) F(-i/2),
  E_J(f) = 1/2 iint_{R^2} (f(x)-f(y))^2 J(|x-y|),  J(u) = e^{-u/2}/(1-e^{-2u}),
  c = psi(1/4) - log pi,  c_n = Lambda(n)/sqrt(n),  R_f(t) = int f(y) f(y+t) dy,  X = e^{2L}.

Discretisation: continuous P1 on (-L, L) with f(+-L) = 0 (eigenfunctions are continuous on R and
vanish at the edges, [EH] Thm 1).  Every node is stored as (anchor, offset) so meshes can be graded
geometrically down to offsets 1e-40 around the edges and around the prime images of the edges.

E_J is assembled element pair by element pair:
  * far pairs (non-adjacent elements): -iint N_a(x) N_b(y) J(|x-y|), with the 1/(2u) part integrated
    analytically in the larger element when the pair is close, Gauss product otherwise;
  * the element itself and its two neighbours: 1/2 iint (f(x)-f(y))^2 J with closed forms for 1/(2u);
  * everything outside the near zone [x_{k-1}, x_{k+2}] (including the exterior of the window) enters
    as the weight int_{R minus near zone} J(|x-y|) dy = T(.) + T(.), T(r) = int_r^inf J.
Prime shifts: exact overlaps of hats with shifted hats (Simpson on the common refinement),
computed in anchored coordinates.

Checks (selfcheck()): E_J against an independent position-side formula; prime and pole terms
against fine-grid quadrature; whole form against Weil's explicit formula with zeta zeros.
"""
import numpy as np

EG = 0.57721566490153286061
CONST_C = -EG - np.pi / 2 - 3 * np.log(2) - np.log(np.pi)      # psi(1/4) - log(pi)
LOG2PI = np.log(2 * np.pi)


def _gl(n):
    x, w = np.polynomial.legendre.leggauss(n)
    return 0.5 * (x + 1), 0.5 * w


GX12, GW12 = _gl(12)
GX6, GW6 = _gl(6)
GX4, GW4 = _gl(4)
GX3, GW3 = _gl(3)
GX30, GW30 = _gl(30)


def _jr_coeffs(nterm=14):
    """J(u) - 1/(2u) = sum_{n>=1} B_n(3/4) 2^{n-1} u^{n-1} / n!  (from x/(e^x-1) * e^{3u/2})."""
    import mpmath as mp
    return np.array([float(mp.bernpoly(n, mp.mpf(3) / 4) * mp.mpf(2) ** (n - 1) / mp.factorial(n))
                     for n in range(1, nterm + 1)])


JR_C = _jr_coeffs()


def Jfull(u):
    return np.exp(-u / 2) / (-np.expm1(-2 * u))


def Jr(u):
    """J(u) - 1/(2u), smooth on [0, inf)."""
    u = np.asarray(u, dtype=float)
    out = np.empty_like(u)
    sm = u < 0.05
    us = u[sm]
    acc = np.zeros_like(us)
    for c in JR_C[::-1]:
        acc = acc * us + c
    out[sm] = acc
    ub = u[~sm]
    out[~sm] = Jfull(ub) - 0.5 / ub
    return out


def Tfull(r):
    """T(r) = int_r^inf J = artanh(e^{-r/2}) + arctan(e^{-r/2}),  r > 0."""
    e = np.exp(-r / 2)
    return 0.5 * np.log1p(e) - 0.5 * np.log(-np.expm1(-r / 2)) + np.arctan(e)


def RT(r):
    """T(r) + (1/2) log r (smooth at 0)."""
    e = np.exp(-r / 2)
    rr = np.where(r > 0, r, 1.0)
    q = np.where(r > 0, -np.expm1(-rr / 2) / rr, 0.5)
    return 0.5 * np.log1p(e) - 0.5 * np.log(q) + np.arctan(e)


def prime_powers(xmax):
    """[(n, Lambda(n))] for prime powers 2 <= n < xmax."""
    out = []
    for n in range(2, int(np.ceil(xmax)) + 1):
        if n >= xmax:
            break
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


# ----------------------------------------------------------------------------------------- mesh

def chain_points(L, gens=2):
    """Chain points from the right edge (generation 1 and 2) with weights; mirrors are -p.
    Returns dict p -> (generation, weight from +L)."""
    pp = prime_powers(np.exp(2 * L))
    pts = {}
    g1 = {}
    for n, lam in pp:
        p = L - np.log(n)
        if p > -L:
            g1[n] = p
            pts.setdefault(round(p, 12), [1, 0.0, p])
            pts[round(p, 12)][1] += lam / np.sqrt(n)
    if gens >= 2:
        g2 = {}
        for n, p1 in g1.items():
            cn = dict(pp)[n] / np.sqrt(n)
            for m, lam in pp:
                cm = lam / np.sqrt(m)
                for p in (p1 - np.log(m), p1 + np.log(m)):
                    if -L < p < L:
                        key = round(p, 12)
                        g2.setdefault(key, [0.0, p])
                        g2[key][0] += cn * cm
        for key, (w, p) in g2.items():
            if key in pts:
                continue
            pts[key] = [2, w, p]
    return {v[2]: (v[0], v[1]) for v in pts.values()}


def make_mesh(L, anchors, H, frozen=None, frac=0.45):
    """anchors: list of (p, rmin, rho) for interior points and the edges (+-L must be included).
    Geometric zones r = rmin*rho^j out to min(H/(rho-1), frac*gap); uniform filler of size <= H.
    frozen: counts (nl, nr, nf) per gap from a previous call (mesh moves smoothly with L).
    Returns dict with node anchors A, offsets o, element lengths h, counts."""
    an = sorted(anchors, key=lambda a: a[0])
    merged = []
    for p, rmin, rho in an:
        if merged and abs(p - merged[-1][0]) < 1e-12:
            q = merged[-1]
            merged[-1] = (q[0], min(q[1], rmin), min(q[2], rho))
        else:
            merged.append((p, rmin, rho))
    assert abs(merged[0][0] + L) < 1e-14 and abs(merged[-1][0] - L) < 1e-14
    merged[0] = (-L,) + merged[0][1:]
    merged[-1] = (L,) + merged[-1][1:]
    A, o, counts = [], [], []
    for i in range(len(merged) - 1):
        p0, r0, q0 = merged[i]
        p1, r1, q1 = merged[i + 1]
        g = p1 - p0
        assert g > 0
        if frozen is not None:
            nl, nr, nf = frozen[i]
        else:
            lim0 = min(H / (q0 - 1), frac * g)
            lim1 = min(H / (q1 - 1), frac * g)
            nl = int(np.floor(np.log(lim0 / r0) / np.log(q0))) + 1 if lim0 > r0 else 0
            nr = int(np.floor(np.log(lim1 / r1) / np.log(q1))) + 1 if lim1 > r1 else 0
            nf = None
        zl = r0 * q0 ** np.arange(nl)
        zr = r1 * q1 ** np.arange(nr)
        a = zl[-1] if nl else 0.0
        b = zr[-1] if nr else 0.0
        flen = g - a - b
        assert flen > 0, ('zones overlap', p0, p1)
        if nf is None:
            nf = max(1, int(np.ceil(flen / H - 1e-9)))
        counts.append((nl, nr, nf))
        A.append(p0); o.append(0.0)
        for z in zl:
            A.append(p0); o.append(z)
        for k in range(1, nf):
            A.append(p0); o.append(a + k * flen / nf)
        for z in zr[::-1]:
            A.append(p1); o.append(-z)
    A.append(L); o.append(0.0)
    A = np.array(A); o = np.array(o)
    h = (A[1:] - A[:-1]) + (o[1:] - o[:-1])
    assert np.all(h > 0), 'nonpositive element'
    return dict(L=L, A=A, o=o, h=h, counts=counts, anchors=merged)


# ------------------------------------------------------------------------------------- assembly

def _near_adjacent(h1, h2):
    """I_uu, I_uv, I_vv = iint_{[0,h1]x[0,h2]} {u^2, uv, v^2} J(u+v) du dv (vectorised)."""
    a = h2 / h1
    G2 = (GX30[None, :] ** 2 * np.log(GX30[None, :] + a[:, None])) @ GW30   # int_0^1 x^2 log(x+a)
    base = G2 + 1.0 / 9.0                                                   # int_0^1 x^2 log(1+a/x)
    s = 0.5 * h1 ** 3
    Iuu = s * base
    Iuv = s * (a / 2 - base)
    Ivv = s * (a * a / 2 - a / 2 + base)
    # smooth part J_r by 6x6 Gauss
    U = h1[:, None, None] * GX6[None, :, None]
    V = h2[:, None, None] * GX6[None, None, :]
    jr = Jr(U + V) * GW6[None, :, None] * GW6[None, None, :]
    hh = (h1 * h2)
    Iuu += hh * np.einsum('kab,kab->k', jr, U * U)
    Iuv += hh * np.einsum('kab,kab->k', jr, U * V)
    Ivv += hh * np.einsum('kab,kab->k', jr, V * V)
    return Iuu, Iuv, Ivv


def _self_P(h):
    """P(h) = iint_{[0,h]^2} (x-y)^2 J(|x-y|) = h^3/6 + 2 int_0^h (h-u) u^2 J_r(u) du."""
    u = h[:, None] * GX6[None, :]
    return h ** 3 / 6 + 2 * h * (((h[:, None] - u) * u * u * Jr(u)) @ GW6)


def assemble(mesh, s=0.0, primes=True, drop=()):
    """Return dict with Q (interior nodes), Mass, pole vectors va, vb, Q0 (s=0 part) etc."""
    L, A, o, h = mesh['L'], mesh['A'], mesh['o'], mesh['h']
    M = len(h)                    # elements; nodes 0..M
    Nn = M + 1
    S = np.zeros((Nn, Nn))
    # ---------------- far pairs: U (k < j-1), blocks -iint N_a(x) N_b(y) J(y-x)
    xi = GX12; wi = GW12
    for k in range(M - 2):
        j = np.arange(k + 2, M)
        base = (A[j] - A[k]) + (o[j] - o[k])          # left(e_j) - left(e_k) > 0
        hk = h[k]; hj = h[j]
        gap = base - hk
        hb = np.maximum(hk, hj)
        B = np.zeros((4, len(j)))                      # 00, 01, 10, 11
        sep = gap > 4 * hb
        # well separated: Gauss product on full J, 6x6 or 3x3
        for sel, gx, gw in ((sep & (gap <= 30 * hb), GX6, GW6), (gap > 30 * hb, GX3, GW3)):
            if sel.any():
                bb = base[sel][:, None, None]; hj_ = hj[sel][:, None, None]
                u = bb + hj_ * gx[None, None, :] - hk * gx[None, :, None]
                Jv = Jfull(u) * gw[None, :, None] * gw[None, None, :]
                Na = (1 - gx, gx)
                for a in range(2):
                    for b in range(2):
                        B[2 * a + b, sel] = -hk * hj[sel] * np.einsum('kab,a,b->k', Jv, Na[a], Na[b])
        nr = ~sep
        if nr.any():
            jj = np.nonzero(nr)[0]
            bb = base[jj]; hj_ = hj[jj]
            # (i) outer over e_k (if hk <= hj) else outer over e_j; analytic inner for 1/(2u)
            outer_k = hk <= hj_
            Bn = np.zeros((4, len(jj)))
            if outer_k.any():
                m = outer_k
                x = hk * xi[None, :]                               # local in e_k
                z1 = bb[m][:, None] - x                           # distance x -> left(e_j)
                hj2 = hj_[m][:, None]
                L1 = np.log1p(hj2 / z1)
                in1 = (hj2 - z1 * L1) / (2 * hj2)                  # int N_1(y)/(2(y-x))
                in0 = L1 / 2 - in1
                for a, Na in enumerate((1 - xi, xi)):
                    Bn[2 * a + 0, m] = -hk * ((Na[None, :] * in0) @ wi)
                    Bn[2 * a + 1, m] = -hk * ((Na[None, :] * in1) @ wi)
            if (~outer_k).any():
                m = ~outer_k
                hj2 = hj_[m][:, None]
                y = bb[m][:, None] + hj2 * xi[None, :]            # local coord rel. left(e_k)
                z1 = y - hk                                       # distance right(e_k) -> y
                L1 = np.log1p(hk / z1)
                in1 = (y * L1 - hk) / (2 * hk)                     # int_0^hk (x/hk)/(2(y-x)) dx
                in0 = L1 / 2 - in1
                for b, Nb in enumerate((1 - xi, xi)):
                    Bn[0 + b, m] = -hj_[m] * ((Nb[None, :] * in0) @ wi)
                    Bn[2 + b, m] = -hj_[m] * ((Nb[None, :] * in1) @ wi)
            # (ii) smooth part J_r, 6x6
            u = bb[:, None, None] + hj_[:, None, None] * GX6[None, None, :] - hk * GX6[None, :, None]
            Jv = Jr(u) * GW6[None, :, None] * GW6[None, None, :]
            Na = (1 - GX6, GX6)
            for a in range(2):
                for b in range(2):
                    Bn[2 * a + b] -= hk * hj_ * np.einsum('kab,a,b->k', Jv, Na[a], Na[b])
            B[:, jj] = Bn
        S[k, j] += B[0]; S[k, j + 1] += B[1]; S[k + 1, j] += B[2]; S[k + 1, j + 1] += B[3]
    S += S.T.copy()
    # ---------------- self pairs
    P = _self_P(h)
    c = P / (2 * h * h)
    idx = np.arange(M)
    S[idx, idx] += c; S[idx + 1, idx + 1] += c; S[idx, idx + 1] -= c; S[idx + 1, idx] -= c
    # ---------------- adjacent pairs (e_k, e_{k+1}), coefficient 1
    if M >= 2:
        h1, h2 = h[:-1], h[1:]
        Iuu, Iuv, Ivv = _near_adjacent(h1, h2)
        k = np.arange(M - 1)
        av = np.stack([-1 / h1, 1 / h1, 0 * h1])          # p = a . (f_k, f_k+1, f_k+2)
        bv = np.stack([0 * h2, -1 / h2, 1 / h2])
        for r in range(3):
            for t in range(3):
                val = Iuu * av[r] * av[t] + Iuv * (av[r] * bv[t] + bv[r] * av[t]) + Ivv * bv[r] * bv[t]
                np.add.at(S, (k + r, k + t), val)
    # ---------------- weights int_{R \ [x_{k-1}, x_{k+2}]} J(|x-y|) dy
    xi = GX12; wi = GW12
    Wl = np.zeros((M, 3))     # local (00, 01, 11)
    hm1 = np.concatenate([[0.0], h[:-1]])     # h_{k-1}
    hp1 = np.concatenate([h[1:], [0.0]])      # h_{k+1}
    NN = ((1 - xi) ** 2, xi * (1 - xi), xi ** 2)
    mom = np.array([1 / 3, 1 / 6, 1 / 3])
    for side in ('L', 'R'):
        if side == 'L':
            d = hm1[:, None] + h[:, None] * xi[None, :]
            sing = np.zeros(M, bool); sing[0] = True
            logmom = np.array([-11 / 18, -5 / 36, -1 / 9])        # int N_aN_b log(xi)
        else:
            d = hp1[:, None] + h[:, None] * (1 - xi[None, :])
            sing = np.zeros(M, bool); sing[-1] = True
            logmom = np.array([-1 / 9, -5 / 36, -11 / 18])        # int N_aN_b log(1-xi)
        reg = ~sing
        for t in range(3):
            Wl[reg, t] += h[reg] * ((Tfull(d[reg]) * NN[t][None, :]) @ wi)
            # singular: T = -(1/2) log r + RT(r), r = h*xi (or h*(1-xi))
            Wl[sing, t] += h[sing] * (-0.5 * (np.log(h[sing]) * mom[t] + logmom[t])
                                      + (RT(d[sing]) * NN[t][None, :]) @ wi)
    S[idx, idx] += Wl[:, 0]; S[idx + 1, idx + 1] += Wl[:, 2]
    S[idx, idx + 1] += Wl[:, 1]; S[idx + 1, idx] += Wl[:, 1]
    # ---------------- mass (banded) and constant
    md = np.zeros(Nn); md[:-1] += h / 3; md[1:] += h / 3
    mo = h / 6
    S[np.arange(Nn), np.arange(Nn)] += CONST_C * md
    S[idx, idx + 1] += CONST_C * mo; S[idx + 1, idx] += CONST_C * mo
    # ---------------- primes: -c_n (R + R^T), accumulated in place
    if primes:
        for n, lam in prime_powers(np.exp(2 * L)):
            if n in drop:
                continue
            tau = np.log(n)
            if tau >= 2 * L:
                continue
            for (i_, j_, v_) in shift_overlap(mesh, tau, sparse=True):
                np.add.at(S, (i_, j_), -(lam / np.sqrt(n)) * v_)
                np.add.at(S, (j_, i_), -(lam / np.sqrt(n)) * v_)
    # ---------------- pole vectors int phi_k e^{-+y/2}
    va = np.zeros(Nn); vb = np.zeros(Nn)
    xl = A[:-1] + o[:-1]
    for sgn, v in ((-1, va), (1, vb)):
        ev = np.exp(sgn * 0.5 * (xl[:, None] + h[:, None] * GX6[None, :]))
        np.add.at(v, idx, h * ((ev * (1 - GX6)[None, :]) @ GW6))
        np.add.at(v, idx + 1, h * ((ev * GX6[None, :]) @ GW6))
    Q0 = S[1:M, 1:M].copy()
    del S
    return dict(Q0=Q0, md=md[1:M].copy(), mo=mo[1:M - 1].copy(), va=va[1:M].copy(), vb=vb[1:M].copy(),
                mesh=mesh)


def mass_dense(asm):
    n = len(asm['md'])
    Mm = np.zeros((n, n))
    Mm[np.arange(n), np.arange(n)] = asm['md']
    Mm[np.arange(n - 1), np.arange(1, n)] = asm['mo']
    Mm[np.arange(1, n), np.arange(n - 1)] = asm['mo']
    return Mm


def mass_mul(asm, f):
    y = asm['md'] * f
    y[:-1] += asm['mo'] * f[1:]
    y[1:] += asm['mo'] * f[:-1]
    return y


def qform(asm, f, s):
    """f^T Q_s f."""
    return f @ asm['Q0'] @ f + 2 * s * (f @ asm['va']) * (f @ asm['vb'])


def shift_overlap(mesh, tau, sparse=False):
    """R[i, j] = int phi_i(y) phi_j(y + tau) dy over all nodes (incl. boundary).
    sparse=True: list of (i, j, value) triplet arrays instead of a dense matrix."""
    A, o, h = mesh['A'], mesh['o'], mesh['h']
    M = len(h)
    Xl = A[:-1] + o[:-1]
    Xr = Xl + h
    pad = 1e-10
    a = Xl - tau; b = Xr - tau                          # images of elements e' under y -> y - tau
    st = np.searchsorted(Xr, a - pad, 'left')
    en = np.searchsorted(Xl, b + pad, 'right')
    cnt = np.maximum(en - st, 0)
    ep = np.repeat(np.arange(M), cnt)                   # e' (image element)
    e = np.concatenate([np.arange(s0, s1) for s0, s1 in zip(st, en) if s1 > s0]) if cnt.sum() else np.zeros(0, int)
    # relative frame: anchor of left node of e
    dA = (A[ep] - tau) - A[e]
    dA = np.where(np.abs(dA) < 1e-9, 0.0, dA)
    a1 = o[e]; a2 = o[e] + h[e]
    b1 = dA + o[ep]; b2 = b1 + h[ep]
    img_in = (b1 >= a1) & (b2 <= a2)
    e_in = (a1 >= b1) & (a2 <= b2) & ~img_in
    lo = np.maximum(a1, b1); hi = np.minimum(a2, b2)
    ln = np.where(img_in, h[ep], np.where(e_in, h[e], hi - lo))
    keep = ln > 0
    e, ep, ln, img_in, e_in = e[keep], ep[keep], ln[keep], img_in[keep], e_in[keep]
    a1, b1, lo = a1[keep], b1[keep], lo[keep]
    he, hep = h[e], h[ep]
    fr = np.array([0.0, 0.5, 1.0])
    # fractions along e and along e' at lo, mid, hi of the overlap
    se = np.where(img_in[:, None], (b1 - a1)[:, None] / he[:, None] + (hep / he)[:, None] * fr[None, :],
                  np.where(e_in[:, None], fr[None, :], (lo - a1)[:, None] / he[:, None] + (ln / he)[:, None] * fr[None, :]))
    sp = np.where(img_in[:, None], fr[None, :],
                  np.where(e_in[:, None], (a1 - b1)[:, None] / hep[:, None] + (he / hep)[:, None] * fr[None, :],
                           (lo - b1)[:, None] / hep[:, None] + (ln / hep)[:, None] * fr[None, :]))
    se = np.clip(se, 0, 1); sp = np.clip(sp, 0, 1)
    simp = np.array([1.0, 4.0, 1.0]) / 6
    Nn = M + 1
    trip = []
    for a_, Na in enumerate((1 - se, se)):
        for b_, Nb in enumerate((1 - sp, sp)):
            trip.append((e + a_, ep + b_, ln * ((Na * Nb) @ simp)))
    if sparse:
        return trip
    R = np.zeros((Nn, Nn))
    for i_, j_, v_ in trip:
        np.add.at(R, (i_, j_), v_)
    return R


# ----------------------------------------------------------------------------------- eigen-solve

def eig(asm, s=0.0, k=6, refine=True):
    """Lowest k eigenpairs of Q_s f = lam Mass f.  Returns list of dicts (lam, f, par, resid) with f on
    interior nodes, Mass-normalised, sign fixed so that f at the node nearest +L is positive."""
    Q = asm['Q0'].copy()
    if s != 0:
        Q += s * np.outer(asm['va'], asm['vb'])
        Q += s * np.outer(asm['vb'], asm['va'])
    md, mo = asm['md'], asm['mo']
    n = len(md)
    d = 1 / np.sqrt(md)
    off = mo * d[:-1] * d[1:]
    # Cholesky of the scaled tridiagonal mass: lower bidiagonal (ld, ll)
    ld = np.empty(n); ll = np.empty(n - 1)
    ld[0] = 1.0
    for i in range(1, n):
        ll[i - 1] = off[i - 1] / ld[i - 1]
        ld[i] = np.sqrt(1.0 - ll[i - 1] ** 2)
    C = Q * d[:, None]
    C *= d[None, :]

    def fwd(Y):                        # Y <- L^{-1} Y (rows), in place
        Y[0] /= ld[0]
        for i in range(1, n):
            Y[i] -= ll[i - 1] * Y[i - 1]
            Y[i] /= ld[i]
    fwd(C)
    C = np.ascontiguousarray(C.T)
    fwd(C)                             # C = L^{-1} Qs L^{-T} (symmetric)
    try:
        import scipy.linalg as sl
        w, Yv = sl.eigh(C, subset_by_index=[0, min(k, n) - 1], overwrite_a=True, driver='evr')
    except ImportError:
        w, Yv = np.linalg.eigh(0.5 * (C + C.T))
        w, Yv = w[:k], Yv[:, :k]
    del C
    G = Yv.copy()                      # back substitution L^T g = y
    G[-1] /= ld[-1]
    for i in range(n - 2, -1, -1):
        G[i] = (G[i] - ll[i] * G[i + 1]) / ld[i]
    V = G * d[:, None]
    res = []
    rowsc = 1 / md

    for m in range(len(w)):
        f = V[:, m].copy()
        lam = w[m]
        if refine:
            mu = lam - 1e-10 * max(1.0, abs(lam))
            B = Q * rowsc[:, None]
            B[np.arange(n), np.arange(n)] -= mu
            B[np.arange(n - 1), np.arange(1, n)] -= mu * mo * rowsc[:-1]
            B[np.arange(1, n), np.arange(n - 1)] -= mu * mo * rowsc[1:]
            try:
                import scipy.linalg as sl
                lu = sl.lu_factor(B, overwrite_a=True, check_finite=False)
                solve = lambda r: sl.lu_solve(lu, r, check_finite=False)
            except ImportError:
                solve = lambda r: np.linalg.solve(B, r)
            for _ in range(3):
                f = solve(mass_mul(asm, f) * rowsc)
                f /= np.sqrt(f @ mass_mul(asm, f))
            del B
            lam = f @ Q @ f
            r = np.abs((Q @ f - lam * mass_mul(asm, f)) * rowsc).max()
        else:
            f /= np.sqrt(f @ mass_mul(asm, f))
            r = np.nan
        if f[-1] < 0:
            f = -f
        par = 'e' if f @ mass_mul(asm, f[::-1]) > 0 else 'o'
        res.append(dict(lam=lam, f=f, par=par, resid=r, s=s))
    return res


def full_nodes(asm, f):
    """Nodal values including the boundary zeros, with node positions (A, o)."""
    m = asm['mesh']
    return m['A'], m['o'], np.concatenate([[0.0], f, [0.0]])


def fourier(asm, f, t):
    """F(t) = int f(y) e^{ity} dy for the P1 function (exact), t array (|t| >~ 1e-3)."""
    m = asm['mesh']
    A, o, h = m['A'], m['o'], m['h']
    fv = np.concatenate([[0.0], f, [0.0]])
    fl, fr = fv[:-1], fv[1:]
    out = np.empty(len(t), complex)
    for i0 in range(0, len(t), 256):
        tt = np.asarray(t[i0:i0 + 256], float)[:, None]
        z = tt * h[None, :]
        ph = np.exp(1j * (tt * A[None, :-1] + tt * o[None, :-1]))
        small = np.abs(z) < 1e-3
        zz = np.where(small, 1.0, z)
        eiz = np.exp(1j * zz)
        E0 = np.where(small, 1 + 1j * z / 2 - z * z / 6, (eiz - 1) / (1j * zz))
        E1 = np.where(small, 0.5 + 1j * z / 3 - z * z / 8, (eiz * (1 - 1j * zz) - 1) / (zz * zz))
        out[i0:i0 + 256] = (ph * h[None, :] * (fl[None, :] * E0 + (fr - fl)[None, :] * E1)).sum(axis=1)
    return out


# ------------------------------------------------------------------------------------ self-check

def W_primes(asm, f):
    """-2 sum c_n R_f(log n) for the interior P1 vector f."""
    m = asm['mesh']; L = m['L']
    fv = np.concatenate([[0.0], f, [0.0]])
    tot = 0.0
    for n, lam in prime_powers(np.exp(2 * L)):
        if np.log(n) < 2 * L:
            R = shift_overlap(m, np.log(n))
            tot -= 2 * lam / np.sqrt(n) * (fv @ R @ fv)
    return tot


def _autocorr_E(asm, f, nfine=200000):
    """Independent E_J: 2 int_0^inf J(u) (g(0) - g(u)) du with g the autocorrelation of the
    P1 function on a fine uniform grid (FFT).  Only for coarse test meshes."""
    m = asm['mesh']
    L = m['L']
    x = np.linspace(-L, L, nfine + 1)
    xn = m['A'] + m['o']
    fv = np.interp(x, xn, np.concatenate([[0.0], f, [0.0]]))
    dx = x[1] - x[0]
    nfft = 1 << int(np.ceil(np.log2(2 * len(x))))
    Fh = np.fft.rfft(fv, nfft)
    g = np.fft.irfft(Fh * np.conj(Fh), nfft)[:len(x)] * dx    # trapezoid-ish autocorrelation
    # trapezoid correction is O(dx^2); fine for a check at 1e-8 level with nfine large
    u = np.arange(len(x)) * dx
    integrand = np.zeros_like(u)
    integrand[1:] = Jfull(u[1:]) * (g[0] - g[1:])
    # near u=0: g(0)-g(u) ~ C u^2 so integrand ~ u/2 -> 0
    I1 = np.trapezoid(integrand, u) if hasattr(np, 'trapezoid') else np.trapz(integrand, u)
    # beyond 2L: g = 0, int_{2L}^inf J g(0) = g(0) T(2L)
    return 2 * (I1 + g[0] * Tfull(np.array([2 * L]))[0])


def selfcheck(L=0.9, s=1.0, zeros=None):
    rng = np.random.default_rng(3)
    an = [(-L, 0.02, 1.5), (L, 0.02, 1.5)]
    mesh = make_mesh(L, an, H=L / 12)
    asm = assemble(mesh)
    xn = (mesh['A'] + mesh['o'])[1:-1]
    f = (L * L - xn ** 2) * np.cos(2.3 * xn + 0.4) + 0.3 * rng.standard_normal(len(xn)) * (L * L - xn ** 2)
    # (1) E_J against the position-side autocorrelation formula
    e1 = f @ asm['Q0'] @ f - W_primes(asm, f) - CONST_C * (f @ mass_mul(asm, f))
    e2 = _autocorr_E(asm, f)
    print(f'E_J: matrix {e1:.12f}  autocorr {e2:.12f}  diff {e1 - e2:.2e}')
    # (2) primes and pole by fine quadrature
    x = np.linspace(-L, L, 400001)
    fv = np.interp(x, mesh['A'] + mesh['o'], np.concatenate([[0.0], f, [0.0]]))
    tz = np.trapezoid if hasattr(np, 'trapezoid') else np.trapz
    for n, lam in prime_powers(np.exp(2 * L)):
        R = shift_overlap(mesh, np.log(n))[1:-1, 1:-1]
        r1 = f @ R @ f
        r2 = tz(fv * np.interp(x + np.log(n), x, fv, right=0.0), x)
        print(f'R_f(log {n}): matrix {r1:.12f} quad {r2:.12f} diff {r1 - r2:.1e}')
    pa = 2 * (f @ asm['va']) * (f @ asm['vb'])
    pb = 2 * tz(fv * np.exp(-x / 2), x) * tz(fv * np.exp(x / 2), x)
    print(f'pole: {pa:.12f} {pb:.12f} diff {pa - pb:.1e}')
    # (3) explicit formula: Q_1(f) = 2 sum_{gamma>0} |F(gamma)|^2
    if zeros is not None:
        Q1 = qform(asm, f, 1.0)
        F = fourier(asm, f, zeros)
        zs = 2 * np.sum(np.abs(F) ** 2)
        tail = 2 * np.sum(np.abs(F[-500:]) ** 2) / 500 * (np.log(zeros[-1] / 2 / np.pi) / 2 / np.pi) * zeros[-1] / 3
        print(f'explicit formula: Q_1 {Q1:.12f}  zero sum (n<={len(zeros)}) {zs:.12f}  diff {Q1 - zs:.2e}'
              f'  (tail estimate {tail:.1e})')
    return asm


if __name__ == '__main__':
    import sys
    z = None
    if len(sys.argv) > 1:
        z = np.loadtxt(sys.argv[1])
    for L in (0.45, 0.9, 1.15):
        print(f'--- L = {L}')
        selfcheck(L, 1.0, z)
