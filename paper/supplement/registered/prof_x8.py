import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import runlib as R, p1weil as W
X = float(sys.argv[1]) if len(sys.argv) > 1 else 8
L = np.log(X) / 2
for g1 in ((1e-9, 1.25), (1e-30, 1.25)):
    an, cp = R.anchors(L, (1e-40, 1.25), g1, (1e-7, 2.0))
    mesh = W.make_mesh(L, an, L / 60)
    asm = W.assemble(mesh)
    e = W.eig(asm, s=0.0, k=1)[0]
    r, v = R.side_profile(asm, e['f'], L, -1)
    ell = -np.log(r); Dp = e['lam'] + R.DSHIFT
    print(f'X={X} gen1={g1} N={len(asm["Q0"])} lam={e["lam"]:.8f} Dpred={Dp:.4f}')
    for t in (5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 85):
        i = np.argmin(abs(ell - t))
        print(f'   ell={ell[i]:6.2f} psi*sqrt(ell-Dpred)={v[i]*np.sqrt(ell[i]-Dp):.6f}  psi*sqrt(ell)={v[i]*np.sqrt(ell[i]):.6f}')
    for lmin in (10, 15, 20, 30):
        ef = R.edge_fit(asm, e['f'], L, lmin=lmin)
        print(f'   fit lmin={lmin}: A={ef["A"]:.6f} D-Dpred={ef["D"]-Dp:+.4f}')
