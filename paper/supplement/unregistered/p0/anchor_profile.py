import sys; sys.path.insert(0, '.')
import numpy as np, p0_edge as P, p0_anchor as A
L = 0.4; NH = 1000; rho = 1.5
Q, h, X, o1, o2, va, vb, _ = A.assemble(L, L / NH, rho)
for par in ('e', 'o'):
    lam, f, _ = P.eig(Q, h, k=1, parity=par)[0]
    sel = (X == L) & (o2 < 0)
    r = np.sqrt(o1[sel] * o2[sel]); ell = -np.log(r); y = f[sel] * np.sqrt(ell)
    o = np.argsort(ell); ell, y = ell[o], y[o]
    for lmin, nt in ((30, 4), (30, 6), (60, 4), (15, 6), (100, 3)):
        m = ell >= lmin
        Xm = np.stack([ell[m] ** (-k) for k in range(nt)], axis=1)
        c, *_ = np.linalg.lstsq(Xm, y[m], rcond=None)
        print(par, f'lmin={lmin} nt={nt} coef=', ' '.join(f'{v:+.5f}' for v in c[:4]), f' maxres={np.abs(Xm@c-y[m]).max():.1e}')
    # half-integer powers allowed?
    m = ell >= 30
    Xm = np.stack([ell[m] ** (-k / 2) for k in range(0, 7)], axis=1)
    c, *_ = np.linalg.lstsq(Xm, y[m], rcond=None)
    print(par, 'half-powers fit coef=', ' '.join(f'{v:+.4f}' for v in c), f' maxres={np.abs(Xm@c-y[m]).max():.1e}')
    pick = [np.argmin(abs(ell - e)) for e in (3, 5, 10, 20, 50, 100, 200)]
    print(par, 'y(ell=3,5,10,20,50,100,200)=', ' '.join(f'{y[p]:.6f}' for p in pick))
