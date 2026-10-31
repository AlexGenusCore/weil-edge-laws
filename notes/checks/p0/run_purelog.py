"""Pure log symbol: Theorem 4 predicts 2L*A^2 = 1 for every eigenfunction."""
import sys, time
sys.path.insert(0, '.')
import numpy as np
import p0_edge as P

L = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
for h0f, rho in ((250, 2.0), (400, 2.0), (250, 1.5)):
    t = time.time()
    Q, h, side, R1, R2 = P.assemble(L, 'log', h0=L / h0f, rho=rho, rmin=1e-150)
    res = P.eig(Q, h, k=6)
    print(f'L={L} N={len(h)} h0=L/{h0f} rho={rho}  ({time.time()-t:.1f}s)')
    for lam, f, par in res:
        for lmin in (8.0, 30.0):
            coef, resid, ell, y = P.edge_fit(f, side, R1, R2, lmin=lmin, nterm=4)
            A = coef[0]
            print(f'  {par} lam={lam:.8f}  lmin={lmin:4.0f}  A={A:+.6f}  2L*A^2={2*L*A*A:.6f}  fit-resid={resid:.1e}'
                  f'  raw y(ell~{ell[-1]:.0f})={y[-1]:+.5f}')
    sys.stdout.flush()
