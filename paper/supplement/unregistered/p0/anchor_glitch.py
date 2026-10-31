import sys; sys.path.insert(0, '.')
import numpy as np, p0_edge as P, p0_anchor as A
L = 0.4; NH = 500; rho = 1.5
Q, h, X, o1, o2, va, vb, _ = A.assemble(L, L / NH, rho)
lam, f, _ = P.eig(Q, h, k=1, parity='e')[0]
sel = (X == L) & (o2 < 0)
r = np.sqrt(o1[sel] * o2[sel]); ell = -np.log(r); y = f[sel] * np.sqrt(ell)
o = np.argsort(ell); ell, y = ell[o], y[o]
m = ell >= 100
Xm = lambda e: np.stack([e ** (-k) for k in range(4)], axis=1)
c, *_ = np.linalg.lstsq(Xm(ell[m]), y[m], rcond=None)
d = y - Xm(ell) @ c
for k in range(0, len(ell), 12):
    print(f'ell={ell[k]:7.2f}  y={y[k]:.7f}  y-fit={d[k]:+.2e}')
