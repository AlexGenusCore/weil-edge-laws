"""True Weil form (pole strength s) : check -lambda'(L) / (2 A^2) = 1 (Theorem 2).
lambda' by central differences on L-scaled meshes; A by edge fit, extrapolated in rho."""
import sys, time
sys.path.insert(0, '.')
import numpy as np
import p0_edge as P

L0 = float(sys.argv[1]) if len(sys.argv) > 1 else 0.4
NH = int(sys.argv[2]) if len(sys.argv) > 2 else 500


def run(L, rho, svals):
    # mesh built for L=1 and scaled, so discretisation error is smooth in L
    br = L * P.mesh(1.0, 1.0 / NH, rho, 1e-150)
    P_mesh = P.mesh
    P.mesh = lambda *a: br                      # inject scaled mesh
    try:
        Q0, h, side, R1, R2 = P.assemble(L, 'weil', s=0.0)
    finally:
        P.mesh = P_mesh
    a, b = P.xcoords(L, side, R1, R2)
    xm = 0.5 * (a + b)
    va = 4 * np.exp(-xm / 2) * np.sinh(h / 4)
    vb = 4 * np.exp(xm / 2) * np.sinh(h / 4)
    out = {}
    for s in svals:
        Q = Q0 + s * (np.outer(va, vb) + np.outer(vb, va))
        for par in ('e', 'o'):
            lam, f, _ = P.eig(Q, h, k=1, parity=par)[0]
            coef, resid, ell, y = P.edge_fit(f, side, R1, R2, lmin=30.0, nterm=4)
            out[(s, par)] = (lam, coef[0], resid)
    return out


svals = (0.0, 1.0)
for d in ((2e-3, 1e-3) if NH <= 500 else (1e-3,)):
    t = time.time()
    lo = run(L0 - d, 1.25, svals)
    hi = run(L0 + d, 1.25, svals)
    mid = run(L0, 1.25, svals)
    mid15 = run(L0, 1.5, svals)
    print(f'L={L0} delta={d} NH={NH}  ({time.time()-t:.0f}s)')
    for key in mid:
        lp = (hi[key][0] - lo[key][0]) / (2 * d)
        A125, A15 = mid[key][1], mid15[key][1]
        x1, x2 = np.log(1.5) ** 2, np.log(1.25) ** 2
        A0 = A125 - (A15 - A125) * x2 / (x1 - x2)
        print(f'  s={key[0]} {key[1]}: lam={mid[key][0]:.10f} lam\'={lp:+.6e}  A(1.5)={A15:.6f} A(1.25)={A125:.6f}'
              f' A(rho->1)={A0:.6f}   -lam\'/(2A^2) = {-lp/(2*A0*A0):.5f}  [rho=1.25 A: {-lp/(2*A125*A125):.5f}]',
              flush=True)
