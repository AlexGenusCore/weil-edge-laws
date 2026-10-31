"""Error bars for the kink tables (post hoc; uses only the existing [NUM] runs, verdicts are not changed).

For every graded row (|A| >= 0.2) of the registered kink runs and of the post-registration L = 1.0 diagnostic:
  value   = registered analysis (window ell in [20, ell_max - 6], finest rho; K5/K0' rho-extrapolated);
  mesh    = max |value(rho) - value(finest rho)| over the rho of the group (K5/K0': spread of the two
            two-mesh extrapolations where three meshes exist, else 0 and flagged);
  window  = max |value(lmin) - value(20)| for lmin in {15, 25}  (finite-ell systematic);
  err     = mesh + window   (a systematic band, not a statistical sigma).
Usage: python consolidate_kink.py NUMERICS_DIR > kink_errors.out   (writes kink_errors.json next to this file)"""
import sys, os, glob, json
import numpy as np

NUM = sys.argv[1]
sys.path.insert(0, NUM)
import kink_analyze as K                      # registered analysis code, unchanged
from kink_summary import extrap

GROUPS = [('L=0.6 right', 'k06_r*.json'), ('L=0.6 symmetric', 'k06m_r*.json'), ('L=0.8 right', 'k08_r*.json'),
          ('L=1.0 right (registered mesh)', 'k10_r*.json'), ('L=1.0 sensitivity (gen-2 at 1e-8)', 'k10g_r*.json'),
          ('L=1.0 diagnostic (post-registration)', 'k10d_r*.json')]
HERE = os.path.dirname(os.path.abspath(__file__))
if glob.glob(os.path.join(HERE, 'k5_L1', 'out', 'k5L1_r1.25.json')):      # the registered rerun (PREREG_K5_L1.md)
    GROUPS += [('L=1.0 K5 rerun, primary (rho 1.5, 1.25)', os.path.join(HERE, 'k5_L1', 'out', 'k5L1_r1.[25]*.json')),
               ('L=1.0 K5 rerun, supplementary (rho 1.5, 1.25, 1.15)', os.path.join(HERE, 'k5_L1', 'out', 'k5L1_r*.json'))]
WINDOWS = (15.0, 20.0, 25.0)


def rho_of(f):
    return float(f.split('_r')[-1][:-5])


out = []
for title, pat in GROUPS:
    files = sorted(glob.glob(os.path.join(NUM, 'out', pat)), key=lambda f: -rho_of(f))   # absolute pat wins in join
    rhos = [rho_of(f) for f in files]
    rows = {(f, w): K.analyse(f, w, 6.0, quiet=True) for f in files for w in WINDOWS}
    fin = files[-1]
    for i, r in enumerate(rows[(fin, 20.0)]):
        if abs(r['A']) < 0.2:
            continue
        rec = dict(group=title, rhos=rhos, s=r['s'], par=r['par'], lam=r['lam'], A=r['A'], q=r['q'], right=bool(r['right']),
                   gen=r['gen'], W=r['W'], n=r.get('n'), beta=r.get('beta'))
        for key in ('kappa0', 'sigma0', 'side0'):
            v = r[key]
            mesh = max(abs(rows[(f, 20.0)][i][key] - v) for f in files)
            win = max(abs(rows[(fin, w)][i][key] - v) for w in (15.0, 25.0))
            rec[key] = dict(v=v, mesh=mesh, win=win, err=mesh + win)
        if r['gen'] == 1:
            for key, comb in (('K5', lambda x: x['b0']), ('K0', lambda x: x['Dfit'])):
                def ext(w, fs=files, rh=rhos):
                    vals = [comb(rows[(f, w)][i]) for f in fs]
                    e = extrap(rh, vals) if len(fs) > 1 else vals[-1]
                    return e + (r['Dpred'] + r['beta'] if key == 'K5' else -r['Dpred'])
                v = ext(20.0)
                if len(files) >= 3:
                    mesh = abs(ext(20.0, files[:2], rhos[:2]) - ext(20.0, files[1:], rhos[1:]))
                else:
                    mesh = float('nan')       # two meshes: extrapolation is exactly determined, no internal check
                win = max(abs(ext(w) - v) for w in (15.0, 25.0))
                rec[key] = dict(v=v, mesh=mesh, win=win, err=(0 if np.isnan(mesh) else mesh) + win)
            rec['K5cal'] = [rows[(f, 20.0)][i]['K5cal'] for f in files]
        out.append(rec)

json.dump(out, open(os.path.join(HERE, 'kink_errors.json'), 'w'), indent=1)
for g in dict.fromkeys(r['group'] for r in out):
    print(f'\n## {g}')
    for r in (x for x in out if x['group'] == g):
        tag = f"s={r['s']:+.0f} {r['par']} A={r['A']:+.4f} q={r['q']:+.4f}{'' if r['right'] else ' (mirror)'} gen{r['gen']}" + \
              (f" n={r['n']}" if r['gen'] == 1 else f" W={r['W']:.4f}")
        line = '  '.join(f"{k}={r[k]['v']:.5f}(mesh {r[k]['mesh']:.1e}, win {r[k]['win']:.1e})" for k in ('kappa0', 'sigma0', 'side0'))
        print(tag + '\n   ' + line)
        if r['gen'] == 1:
            print('   ' + '  '.join(f"{k}dev={r[k]['v']:+.5f}(mesh {r[k]['mesh']:.1e}, win {r[k]['win']:.1e})" for k in ('K5', 'K0'))
                  + '  K5cal by rho=' + ','.join(f'{c:+.5f}' for c in r['K5cal']))
