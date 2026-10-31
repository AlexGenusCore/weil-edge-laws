import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import p1weil as W
L = 0.4
out = {}
for rmin, rho in ((1e-40, 1.5), (1e-40, 1.25)):
    an = [(-L, rmin, rho), (L, rmin, rho)]
    for p in W.chain_points(L):
        an += [(p, rmin, rho), (-p, rmin, rho)]
    asm = W.assemble(W.make_mesh(L, an, L / 40), s=0.0)
    e = W.eig(asm, k=1)[0]
    A, o, fv = W.full_nodes(asm, e['f'])
    sel = (A == L) & (o < 0)
    r = -o[sel]; ell = -np.log(r)
    D = e['lam'] + 2.4150927
    out[rho] = (ell, fv[sel] * np.sqrt(ell - D))
for rho, (ell, a) in out.items():
    print('rho', rho)
    for target in (2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 85, 88, 90, 91.5):
        i = np.argmin(abs(ell - target))
        print(f'   ell={ell[i]:7.3f}  psi*sqrt(ell-D)={a[i]:.6f}')
