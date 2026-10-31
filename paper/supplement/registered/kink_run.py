"""Kink runs: P1 eigenfunctions with deep grading at the edges and at selected chain points.
Usage: python kink_run.py L rho rmin H_div deep_spec svals k out.json [mirror]
  mirror: 1 = mirrors and left edge graded like the right side (default); 0 = right side only
  deep_spec: comma list of right-side chain points given as 'n<int>' (y_n = L - log n) or 'q<a>/<b>'
             (L - log(a/b)); mirrors are graded too.  'all1' = every generation-1 point.
Writes raw nodal profiles (no fitting) to out.json."""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import runlib as R
import p1weil as W

L = float(sys.argv[1]); rho = float(sys.argv[2]); rmin = float(sys.argv[3]); Hdiv = float(sys.argv[4])
spec = sys.argv[5]; svals = tuple(float(x) for x in sys.argv[6].split(',')); k = int(sys.argv[7])
out = sys.argv[8]
mirror = (sys.argv[9] != '0') if len(sys.argv) > 9 else True
cp = W.chain_points(L, gens=2)
deep = []
for tok in spec.split(','):
    if tok == 'all1':
        deep += [p for p, (g, w) in cp.items() if g == 1]
    elif tok.startswith('n'):
        deep.append(L - np.log(int(tok[1:])))
    elif tok.startswith('q'):
        a, b = tok[1:].split('/')
        deep.append(L - np.log(int(a) / int(b)))
deep = sorted(set(round(p, 12) for p in deep))
t0 = time.time()
G2 = tuple(float(x) for x in os.environ.get('KINK_GEN2', '1e-8,2.0').split(','))
an, cp = R.anchors(L, (rmin, rho), (1e-12, 1.5), G2, deep=[float(p) for p in deep], deep_par=(rmin, rho),
                   mirror_deep=mirror, edge_left=None if mirror else (1e-12, 1.5),
                   mirror_par=None if mirror else (1e-10, 1.6))
mesh, asm, res, dt = R.solve(L, an, L / Hdiv, svals=svals, k=k)
print(f'L={L} rho={rho} rmin={rmin} N={len(asm["Q0"])} solve {dt:.0f}s', flush=True)
data = dict(gen2=G2, mirror=mirror, L=L, rho=rho, rmin=rmin, H=L / Hdiv, N=len(asm['Q0']), deep=[float(p) for p in deep],
            chain={repr(float(p)): v for p, v in cp.items()}, states=[])
for s in svals:
    for e in res[s]:
        f = e['f']
        xn = mesh['A'] + mesh['o']
        fv = np.concatenate([[0.0], f, [0.0]])
        fm = np.interp(-xn, xn, fv)
        par = 'e' if np.sum(fv * fm * np.gradient(xn)) > 0 else 'o'
        st = dict(s=s, lam=e['lam'], par=par, resid=e['resid'])
        for nm, p, side in (('edge+', L, -1), ('edge-', -L, +1)):
            r, v = R.side_profile(asm, f, p, side)
            st[nm] = dict(r=r.tolist(), v=v.tolist())
        st['pts'] = {}
        for p in deep:
            for q in ((p, -p) if mirror else (p,)):
                rl, vl = R.side_profile(asm, f, q, -1)
                rr, vr = R.side_profile(asm, f, q, +1)
                st["pts"][repr(float(q))] = dict(rl=rl.tolist(), vl=vl.tolist(), rr=rr.tolist(), vr=vr.tolist(),
                                         c=R.node_value(asm, f, q))
        data['states'].append(st)
        print(f'  s={s} {par} lam={e["lam"]:.10f} resid={e["resid"]:.1e}', flush=True)
json.dump(data, open(out, 'w'))
print(f'done {time.time()-t0:.0f}s', flush=True)
