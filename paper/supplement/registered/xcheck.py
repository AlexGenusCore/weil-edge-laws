"""X=8 edge-profile drift: is it the coincidence 2L = log 8?  Compare X=8 and X=7.9 with all generation-1
points graded like the edges (1e-40, 1.25); E0 (s=0) profile psi*sqrt(ell - Dpred)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import runlib as R, p1weil as W
for X in (8.0, 7.9, 7.0):
    L = np.log(X) / 2
    an, cp = R.anchors(L, (1e-40, 1.25), (1e-9, 1.25), (1e-7, 2.0), deep=[L - np.log(2), L - np.log(4)], deep_par=(1e-40, 1.25))
    mesh = W.make_mesh(L, an, L / 60)
    asm = W.assemble(mesh)
    e = W.eig(asm, s=0.0, k=1)[0]
    r, v = R.side_profile(asm, e['f'], L, -1)
    ell = -np.log(r); Dp = e['lam'] + R.DSHIFT
    row = []
    for t in (10, 20, 30, 40, 50, 60, 70, 80, 85):
        i = np.argmin(abs(ell - t)); row.append(v[i] * np.sqrt(ell[i] - Dp))
    fits = [R.edge_fit(asm, e['f'], L, lmin=lm) for lm in (12, 20, 30)]
    print(f'X={X} N={len(asm["Q0"])} lam={e["lam"]:.8f}  psi*sqrt(ell-Dpred) at ell=10..85: ' + ' '.join(f'{x:.6f}' for x in row))
    print('     fits lmin 12/20/30: A=' + ' '.join(f'{f["A"]:.6f}' for f in fits) + '  D-Dpred=' + ' '.join(f'{f["D"]-Dp:+.4f}' for f in fits), flush=True)
