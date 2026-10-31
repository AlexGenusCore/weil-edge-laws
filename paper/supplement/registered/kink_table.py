"""Compact table of graded kink rows (finest rho per group) for the report."""
import sys, os, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import kink_analyze as K
from kink_summary import GROUPS, extrap
for title, pat in GROUPS + [('L=1.0 DIAGNOSTIC all gen-2 deep (post-registration)', 'out/k10d_r*.json')]:
    files = sorted(glob.glob(pat), key=lambda f: -float(f.split('_r')[-1][:-5]))
    if not files:
        continue
    rows = {f: K.analyse(f, 20.0, 6.0, quiet=True) for f in files}
    rhos = [float(f.split('_r')[-1][:-5]) for f in files]
    print(f'\n{title} (rho {rhos}; values at rho={rhos[-1]}, K5/K0 extrapolated)')
    print('| s | sector | lam | A | point | gen | n or W | kappa0 | sigma0 | side | K5 dev (extrap) | K5 dev (calibrated) | D_fit-D |')
    for i, r0 in enumerate(rows[files[0]]):
        if abs(r0['A']) < 0.2:
            continue
        rr = [rows[f][i] for f in files]
        fin = rr[-1]
        if fin['gen'] == 1:
            k5 = (extrap(rhos, [x['b0'] for x in rr]) if len(rr) > 1 else fin['b0'] - (-0.0841 * np.log(rhos[-1]) ** 2)) + fin['Dpred'] + fin['beta']
            d0 = (extrap(rhos, [x['Dfit'] for x in rr]) if len(rr) > 1 else fin['Dfit'] - 0.0841 * np.log(rhos[-1]) ** 2) - fin['Dpred']
            extra = f"{k5:+.4f} | {fin['K5cal']:+.4f} | {d0:+.4f}"
            nw = f"n={fin['n']} (beta={fin['beta']:.3f})"
        else:
            extra = '— | — | —'
            nw = f"W={fin['W']:.4f}"
        print(f"| {fin['s']:+.0f} | {fin['par']} | {fin['lam']:+.4f} | {fin['A']:+.4f} | {fin['q']:+.4f}{'' if fin['right'] else ' (mirror)'} | {fin['gen']} | {nw} |"
              f" {fin['kappa0']:.5f} | {fin['sigma0']:.5f} | {fin['side0']:.4f} | {extra} |")
