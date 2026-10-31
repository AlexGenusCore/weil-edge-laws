"""K5 rerun at L = 1.0 (registered in PREREG_K5_L1.md).

Identical to kink_run.py with mirror = 0 (right side measured; left edge and mirror points as in the registered
L = 1.0 runs), except for the mesh rule:
  every chain point coupled to a measured point by one prime-power shift log m (m < X = e^{2L}) is graded with
  the measured points' (rmin, rho), so no grading truncation of a coupled zone falls inside the fit window.
Measured points: the right edge +L, every right-side generation-1 point y_n = L - log n, and L - log 6.
Usage: python k5_run.py L rho rmin H_div svals k out.json      (out.json = 'dry' prints the mesh and exits)
Writes raw nodal profiles (no fitting) in the kink_run.py format, so kink_analyze.py reads it unchanged."""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import runlib as R
import p1weil as W

L, rho, rmin, Hdiv = (float(x) for x in sys.argv[1:5])
svals = tuple(float(x) for x in sys.argv[5].split(',')); k = int(sys.argv[6]); out = sys.argv[7]
cp = W.chain_points(L, gens=2)
meas = sorted({round(p, 12) for p, (g, w) in cp.items() if g == 1} | {round(L - np.log(6.0), 12)})
shifts = [np.log(m) for m, _ in W.prime_powers(np.exp(2 * L))]
coupled = {round(q + sg * t, 12) for q in meas + [L] for t in shifts for sg in (-1, 1) if -L + 1e-9 < q + sg * t < L - 1e-9}
graded = sorted(set(meas) | coupled)
right2 = {round(p, 12) for p, (g, w) in cp.items() if g == 2}
an, cp = R.anchors(L, (rmin, rho), (1e-12, 1.5), (1e-16, 1.6), deep=graded, deep_par=(rmin, rho),
                   mirror_deep=False, edge_left=(1e-12, 1.5), mirror_par=(1e-10, 1.6))
known = {round(a[0], 12) for a in an}
extra = [p for p in graded if p not in known]          # coupled points beyond generation 2 (not in chain table)
an += [(p, rmin, rho) for p in extra]
mesh = W.make_mesh(L, an, L / Hdiv)
print(f'L={L} rho={rho} rmin={rmin} H=L/{Hdiv:g} N={len(mesh["h"]) - 1}', flush=True)
print('  measured:', ' '.join(f'{p:+.6f}' for p in meas), flush=True)
print('  graded (rmin, rho):', ' '.join(f'{p:+.6f}' for p in graded), flush=True)
print('  of which beyond generation 2:', ' '.join(f'{p:+.6f}' for p in extra), flush=True)
print('  right-side gen-2 points left at (1e-16, 1.6):', sorted(right2 - set(graded)), flush=True)
if out == 'dry':
    sys.exit(0)

t0 = time.time()
mesh, asm, res, dt = R.solve(L, an, L / Hdiv, svals=svals, k=k)
print(f'N={len(asm["Q0"])} solve {dt:.0f}s', flush=True)
data = dict(rule='PREREG_K5_L1: all coupled chain points graded at (rmin, rho)', mirror=False, L=L, rho=rho,
            rmin=rmin, H=L / Hdiv, N=len(asm['Q0']), deep=[float(p) for p in meas], graded=[float(p) for p in graded],
            chain={repr(float(p)): v for p, v in cp.items()}, states=[])
for s in svals:
    for e in res[s]:
        f = e['f']
        xn = mesh['A'] + mesh['o']
        fv = np.concatenate([[0.0], f, [0.0]])
        par = 'e' if np.sum(fv * np.interp(-xn, xn, fv) * np.gradient(xn)) > 0 else 'o'
        st = dict(s=s, lam=e['lam'], par=par, resid=e['resid'])
        for nm, p, side in (('edge+', L, -1), ('edge-', -L, +1)):
            r, v = R.side_profile(asm, f, p, side)
            st[nm] = dict(r=r.tolist(), v=v.tolist())
        st['pts'] = {}
        for q in meas:
            rl, vl = R.side_profile(asm, f, q, -1)
            rr, vr = R.side_profile(asm, f, q, +1)
            st['pts'][repr(float(q))] = dict(rl=rl.tolist(), vl=vl.tolist(), rr=rr.tolist(), vr=vr.tolist(),
                                             c=R.node_value(asm, f, q))
        data['states'].append(st)
        print(f'  s={s} {par} lam={e["lam"]:.10f} resid={e["resid"]:.1e}', flush=True)
json.dump(data, open(out, 'w'))
print(f'done {time.time() - t0:.0f}s', flush=True)
