"""Spectrum survey at X = 6, 8, 10: lam, parity, edge trace A for the lowest states, s = 0 and 1."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import runlib as R
for X in (6, 8, 10):
    L = np.log(X) / 2
    an, cp = R.anchors(L, (1e-30, 1.5), (1e-8, 1.5), (1e-6, 2.0))
    mesh, asm, out, dt = R.solve(L, an, L / 40, svals=(0.0, 1.0), k=8)
    print(f'X={X} L={L:.6f} N={len(asm["Q0"])} t={dt:.0f}s', flush=True)
    for s, st in out.items():
        for e in st:
            ef = R.edge_fit(asm, e['f'], L, lmin=12)
            print(f'   s={s} {e["par"]} lam={e["lam"]:+.8f}  A={ef["A"]:+.5f}  2A^2={2*ef["A"]**2:.5f}  Dfit-Dpred={ef["D"]-e["lam"]-R.DSHIFT:+.3f}')
