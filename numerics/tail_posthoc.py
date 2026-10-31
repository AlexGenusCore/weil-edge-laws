"""POST-HOC (not registered): cross-X comparison of Z/P0 (no c_X) and Z/P1 (with c_X) for the primary states,
and the effective kink coefficient k_eff = (Z/P1 - 1)/(-sum c_n^2 <a^-2>)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import tail_analyze as TA
B = [(400, 800), (800, 1600), (1600, 3200), (3200, 6400), (6400, 10300)]
for nm in ('E0', 'Em1', 'O5', 'O20'):
    print(f'--- {nm}')
    for X in (6, 8, 10):
        d = TA.load(f'out/tail_X{X}_fine.npz')
        bl = {(b[0], b[1]): b for b in TA.blocks(d, nm)}
        r0, r1, ke = [], [], []
        for T1, T2 in B:
            P0, P1, Pl, ia, ia2 = TA.preds(d, nm, T1, T2)
            Z = bl[(T1, T2)][2]
            r0.append(Z / P0); r1.append(Z / P1)
            ke.append((Z / P1 - 1) / (-TA.SIGC2(X) * ia2))
        print(f'   X={X:2d} lam={d["st"][nm]["lam"]:+7.3f}  Z/P0: ' + ' '.join(f'{x:.4f}' for x in r0)
              + '   Z/P1: ' + ' '.join(f'{x:.4f}' for x in r1) + '   k_eff: ' + ' '.join(f'{x:+.2f}' for x in ke))
