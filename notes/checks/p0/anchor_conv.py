"""Anchored mesh: convergence of A in NH and in the depth of the grading at y_n."""
import sys; sys.path.insert(0, '.')
import numpy as np, p0_edge as P, p0_anchor as A
L = float(sys.argv[1]); rho = float(sys.argv[2]); s = float(sys.argv[3]) if len(sys.argv) > 3 else 0.0
for NH, rint in ((500, 1e-20), (500, 1e-60), (1000, 1e-40), (2000, 1e-40)):
    Q, h, X, o1, o2, va, vb, _ = A.assemble(L, L / NH, rho, rmin_int=rint)
    Q = Q + s * (np.outer(va, vb) + np.outer(vb, va))
    out = []
    for par in ('e', 'o'):
        lam, f, _ = P.eig(Q, h, k=1, parity=par)[0]
        out.append(f'{par}: lam={lam:.9f} A={A.edge_fit(f, X, o1, o2, L):.6f}')
    print(f'NH={NH} rmin_int={rint:.0e} N={len(h)}  ' + '   '.join(out), flush=True)
