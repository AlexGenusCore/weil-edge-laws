"""P0 Galerkin for the Weil form with the mesh also graded at the prime images
+-(L - log n) of the window edges (anchored cells: x = X + o, offsets o kept exactly).
Needed because a uniform cell at y_n = L - log n averages the one-sided germ of psi
there, and the edge equation sees that average through the prime shift: an
O(c_n A ell(h0)^{-3/2}) source error, i.e. a few 1e-3 in A at h0 ~ 1e-3.
Usage: python p0_anchor.py L NH   -> Hadamard ratio -lambda'/(2A^2) for s=0,1, both sectors.
"""
import sys, time
sys.path.insert(0, '.')
import numpy as np
import p0_edge as P


def rseq(h0, rho, rmin):
    r = [0.0, rmin]
    while (rho - 1) * r[-1] < h0:
        r.append(r[-1] * rho)
    return np.array(r)            # last step about h0


def build(L, h0, rho, rmin=1e-100, rmin_int=1e-40, counts=None):
    """counts: filler cell counts per gap (fixed across L for smooth finite differences)."""
    newcounts = []
    taus = [np.log(n) for n, _ in P.primes_upto(int(np.exp(2 * L)) + 1) if np.log(n) < 2 * L]
    re = rseq(h0, rho, rmin)
    ri = re[re >= rmin_int]; ri = np.concatenate([[0.0], ri])   # sub-sequence of re: images align
    R = re[-1]
    # right half [0, L]: zones (X, offsets breakpoints)
    zones = [(L, -re[::-1])]
    ys = sorted({abs(L - t) for t in taus})
    for y in ys:
        assert y - ri[-1] > 0 and y + ri[-1] < L - R, 'zones overlap; change L'
        zones.append((y, np.concatenate([-ri[::-1], ri[1:]])))
    zones.sort()
    cells = []           # (X, o1, o2)
    x = 0.0
    for X, ob in zones:
        lo = X + ob[0]
        n = counts[len(newcounts)] if counts else max(1, int(np.ceil((lo - x) / h0 - 1e-9)))
        newcounts.append(n)
        e = np.linspace(x, lo, n + 1)
        cells += [(0.0, e[k], e[k + 1]) for k in range(n)]
        cells += [(X, ob[k], ob[k + 1]) for k in range(len(ob) - 1)]
        x = X + ob[-1]
    assert abs(x - L) < 1e-15
    right = cells
    left = [(-X, -o2, -o1) for X, o1, o2 in reversed(right)]
    C = np.array(left + right)
    return C, taus, newcounts


def assemble(L, h0, rho, rmin=1e-100, rmin_int=1e-40, counts=None):
    C, taus, counts = build(L, h0, rho, rmin, rmin_int, counts)
    X, o1, o2 = C[:, 0], C[:, 1], C[:, 2]
    h = o2 - o1
    N = len(h)
    Q = np.zeros((N, N))
    for i in range(N):
        j = np.arange(i + 1, N)
        dX = X[j] - X[i]
        same = dX == 0
        g = np.where(same, np.maximum(o1[j] - o2[i], o1[i] - o2[j]),
                     np.maximum((dX + o1[j]) - o2[i], o1[i] - (dX + o2[j])))
        g = np.maximum(g, 0.0)
        hs = np.minimum(h[i], h[j]); hb = np.maximum(h[i], h[j])
        Jij = P.j_pair(hs, g, hb)
        u = g[:, None, None] + h[i] * P.G3X[None, :, None] + h[j][:, None, None] * P.G3X[None, None, :]
        Jij = Jij + h[i] * h[j] * np.einsum('kab,a,b->k', P.Jr(u), P.G3W, P.G3W)
        Q[i, j] = -Jij; Q[j, i] = -Jij
    Q[np.diag_indices(N)] = -Q.sum(axis=1)
    # killing: distances to the right and left edge
    K = np.zeros(N)
    # distance to an edge is exact only for cells anchored at that edge; elsewhere
    # D2 - D1 loses h to rounding, so integrate the smooth T with the exact h.
    for own, D1, D2 in ((X == L, (L - X) - o2, (L - X) - o1), (X == -L, (X + L) + o1, (X + L) + o2)):
        D1 = np.maximum(D1, 0.0)
        r = D1[:, None] + h[:, None] * P.GX[None, :]
        K += np.where(own, P.int_mlog(D1, D2) + h * (P.RT(r) @ P.GW),
                      h * (P.Tfull(np.where(own[:, None], 1.0, r)) @ P.GW))
    c = -P.EG - np.pi / 2 - 3 * np.log(2) - np.log(np.pi)
    Q[np.diag_indices(N)] += K + c * h
    a, b = X + o1, X + o2
    for n, lam in P.primes_upto(int(np.exp(2 * L)) + 1):
        tau = np.log(n)
        if tau >= 2 * L:
            continue
        cn = lam / np.sqrt(n)
        aligned = np.abs(X[:, None] - (X[None, :] + tau)) < 1e-12
        lo = np.where(aligned, np.maximum(o1[:, None], o1[None, :]), np.maximum(a[:, None], a[None, :] + tau))
        hi = np.where(aligned, np.minimum(o2[:, None], o2[None, :]), np.minimum(b[:, None], b[None, :] + tau))
        O = np.maximum(hi - lo, 0.0)
        inside_j = ~aligned & (a[None, :] + tau >= a[:, None]) & (b[None, :] + tau <= b[:, None])
        inside_i = ~aligned & (a[:, None] >= a[None, :] + tau) & (b[:, None] <= b[None, :] + tau)
        O = np.where(inside_j, np.broadcast_to(h[None, :], (N, N)), O)
        O = np.where(inside_i, np.broadcast_to(h[:, None], (N, N)), O)
        Q -= cn * (O + O.T)
    xm = X + 0.5 * (o1 + o2)
    va = 4 * np.exp(-xm / 2) * np.sinh(h / 4)
    vb = 4 * np.exp(xm / 2) * np.sinh(h / 4)
    return Q, h, X, o1, o2, va, vb, counts


def edge_fit(f, X, o1, o2, L, lmin=30.0, nterm=4):
    sel = (X == L) & (o2 < 0)
    r = np.sqrt(o1[sel] * o2[sel])
    ell = -np.log(r)
    y = f[sel] * np.sqrt(ell)
    m = ell >= lmin
    Xm = np.stack([ell[m] ** (-k) for k in range(nterm)], axis=1)
    coef, *_ = np.linalg.lstsq(Xm, y[m], rcond=None)
    return coef[0]


def run(L, h0, rho, svals=(0.0, 1.0), counts=None):
    Q0, h, X, o1, o2, va, vb, counts = assemble(L, h0, rho, counts=counts)
    out = {}
    for s in svals:
        Q = Q0 + s * (np.outer(va, vb) + np.outer(vb, va))
        for par in ('e', 'o'):
            lam, f, _ = P.eig(Q, h, k=1, parity=par)[0]
            out[(s, par)] = (lam, edge_fit(f, X, o1, o2, L))
    return out, len(h), counts


if __name__ == '__main__':
    L0 = float(sys.argv[1]); NH = int(sys.argv[2])
    d = 1e-3
    t = time.time()
    # mesh is not scaled with L here (anchors move); use delta small and compare two rho
    res = {}
    for rho in (1.5, 1.25):
        mid, N, cnt = run(L0, L0 / NH, rho)
        lo, _, _ = run(L0 - d, L0 / NH, rho, counts=cnt)
        hi, _, _ = run(L0 + d, L0 / NH, rho, counts=cnt)
        res[rho] = (mid, lo, hi)
        print(f'rho={rho} N={N} done ({time.time()-t:.0f}s)', flush=True)
    x1, x2 = np.log(1.5) ** 2, np.log(1.25) ** 2
    print(f'L={L0} NH={NH} delta={d}')
    for key in res[1.25][0]:
        lp = {rho: (res[rho][2][key][0] - res[rho][1][key][0]) / (2 * d) for rho in res}
        A15, A125 = res[1.5][0][key][1], res[1.25][0][key][1]
        A0 = A125 - (A15 - A125) * x2 / (x1 - x2)
        print(f'  s={key[0]} {key[1]}: lam={res[1.25][0][key][0]:.10f}  lam\'(1.5)={lp[1.5]:+.6e} lam\'(1.25)={lp[1.25]:+.6e}'
              f'  A(1.5)={A15:.6f} A(1.25)={A125:.6f} A(rho->1)={A0:.6f}  -lam\'/(2A^2)={-lp[1.25]/(2*A0*A0):.5f}', flush=True)
