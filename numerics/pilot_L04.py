"""Pilot: L=0.4 (referee's P0 values: s=0 even lam=-1.5400, A_e=1.5696, A_o=0.4510; s=1 A_e=0.0621)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import runlib as R
L = 0.4
for rmin, rho, H in ((1e-40, 1.5, L / 40), (1e-40, 1.25, L / 40), (1e-40, 1.25, L / 80)):
    an, cp = R.anchors(L, (rmin, rho), (rmin, rho))
    mesh, asm, out, dt = R.solve(L, an, H, svals=(0.0, 1.0), k=4)
    print(f'rmin={rmin:g} rho={rho} H=L/{L/H:.0f} N={len(asm["Q0"])} t={dt:.1f}s', flush=True)
    for s, st in out.items():
        for e in st:
            ef = R.edge_fit(asm, e['f'], L)
            efm = R.edge_fit(asm, e['f'], L, sign=-1)
            print(f'   s={s} {e["par"]} lam={e["lam"]:.10f} resid={e["resid"]:.1e}  A+={ef["A"]:.6f} A-={efm["A"]:.6f}'
                  f' D={ef["D"]:.4f} (lam+2.41509={e["lam"]+R.DSHIFT:.4f}) rms={ef["rms"]:.1e}')
