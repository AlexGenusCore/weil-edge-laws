import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import runlib as R, p1weil as W
for X in (6, 8, 10):
    L = np.log(X) / 2
    an, cp = R.anchors(L, (1e-30, 1.25), (1e-9, 1.25), (1e-7, 2.0))
    asm = W.assemble(W.make_mesh(L, an, L / 60))
    for s in (-2.0, -1.0, 2.0, 20.0):
        st = W.eig(asm, s=s, k=3)
        for e in st[:2]:
            ef = R.edge_fit(asm, e['f'], L, lmin=12)
            print(f'X={X} s={s:+.0f} {e["par"]} lam={e["lam"]:+.6f} A={ef["A"]:+.4f}', flush=True)
