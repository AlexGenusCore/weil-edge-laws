"""Kink convergence study: mesh-to-mesh differences only (rho = 1.5, 1.25, 1.15; H = L/40, L/80)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import kink_analyze as K
files = ['out/kconv_r150.json', 'out/kconv_r125.json', 'out/kconv_r125_H80.json', 'out/kconv_r115.json']
for lmin, lcut in ((12, 6), (20, 6)):
    print(f'--- fit window ell >= {lmin}, ell <= ell_max - {lcut}')
    rows = {f: K.analyse(f, lmin, lcut, quiet=True) for f in files}
    keys = ['kappa0', 'sigma0', 'side0', 'b0', 'Dfit']
    for i, r0 in enumerate(rows[files[0]]):
        tag = f"{r0['par']} lam={r0['lam']:+.5f} A={r0['A']:.4f} q={r0['q']:+.4f} gen{r0['gen']}"
        print(tag)
        for kk in keys:
            if kk not in r0:
                continue
            vals = [rows[f][i][kk] for f in files]
            print(f'   {kk:7s}: ' + '  '.join(f'{v:+.5f}' for v in vals) +
                  f'   |1.25-1.15|={abs(vals[1]-vals[3]):.1e} |H40-H80|={abs(vals[1]-vals[2]):.1e} |1.5-1.25|={abs(vals[0]-vals[1]):.1e}')
