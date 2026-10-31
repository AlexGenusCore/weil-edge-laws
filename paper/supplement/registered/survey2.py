import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import runlib as R, p1weil as W
X = 8
L = np.log(X) / 2
an, cp = R.anchors(L, (1e-30, 1.5), (1e-8, 1.5), (1e-6, 2.0))
mesh = W.make_mesh(L, an, L / 40)
asm = W.assemble(mesh)
for s in (0.0, 1.0, 5.0, -5.0):
    st = W.eig(asm, s=s, k=36, refine=True)
    print(f's={s}')
    for e in st:
        ef = R.edge_fit(asm, e['f'], L, lmin=12)
        if abs(ef['A']) > 0.1 or e is st[0]:
            print(f'   {e["par"]} lam={e["lam"]:+.6f}  A={ef["A"]:+.4f}', flush=True)
