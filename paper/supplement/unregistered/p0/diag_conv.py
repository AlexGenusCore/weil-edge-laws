"""Diagnose h0-sensitivity of the fitted edge trace for the Weil form."""
import sys, time
sys.path.insert(0, '.')
import numpy as np
import p0_edge as P

L = float(sys.argv[1]); rho = float(sys.argv[2])
for NH in (250, 500, 1000):
    br = L * P.mesh(1.0, 1.0 / NH, rho, 1e-150)
    pm = P.mesh; P.mesh = lambda *a: br
    Q, h, side, R1, R2 = P.assemble(L, 'weil', s=0.0)
    P.mesh = pm
    for par in ('e', 'o'):
        lam, f, _ = P.eig(Q, h, k=1, parity=par)[0]
        line = []
        for lmin, nt in ((30, 4), (60, 4), (30, 5), (100, 3)):
            coef, resid, ell, y = P.edge_fit(f, side, R1, R2, lmin=lmin, nterm=nt)
            line.append(f'A[{lmin},{nt}]={coef[0]:.6f}')
        sel = (side > 0) & (R1 > 0)
        ell = -np.log(np.sqrt(R1[sel] * R2[sel])); y = f[sel] * np.sqrt(ell)
        pick = [np.argmin(abs(ell - e)) for e in (5, 10, 20, 50, 100, 300)]
        print(f'NH={NH} {par} N={len(h)} lam={lam:.9f} ' + ' '.join(line) +
              '  y(ell=5,10,20,50,100,300)=' + ' '.join(f'{y[p]:.5f}' for p in pick), flush=True)
