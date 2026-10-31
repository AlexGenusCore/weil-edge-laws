"""Apply the PREREG.md kink criteria to the production runs (uses kink_analyze.analyse, window [20, lmax-6]).
Usage: python kink_summary.py > out/kink_summary.out"""
import sys, os, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import kink_analyze as K

TOL = dict(k1=0.005, s1=0.003, side1=0.015, k2=0.01, s2=0.004, side2=0.015, k5=0.005, d=0.005)
GROUPS = [('L=0.6 right', 'out/k06_r*.json'), ('L=0.6 symmetric', 'out/k06m_r*.json'),
          ('L=0.8 right', 'out/k08_r*.json'), ('L=1.0 right', 'out/k10_r*.json'),
          ('L=1.0 right, gen-2 coarse (sensitivity)', 'out/k10g_r*.json')]


def extrap(rhos, vals):
    """v = v_inf + c (log rho)^2 (least squares)."""
    x = np.log(np.array(rhos)) ** 2
    Xm = np.stack([np.ones_like(x), x], 1)
    co, *_ = np.linalg.lstsq(Xm, np.array(vals), rcond=None)
    return co[0]


def pf(ok):
    return 'PASS' if ok else 'FAIL'


def main():
    tally = {}
    for title, pat in GROUPS:
        files = sorted(glob.glob(pat), key=lambda f: -float(f.split('_r')[-1][:-5]))
        if not files:
            continue
        rows = {f: K.analyse(f, 20.0, 6.0, quiet=True) for f in files}
        rhos = [float(f.split('_r')[-1][:-5]) for f in files]
        print(f'\n######## {title}: rho = {rhos}')
        nrow = len(rows[files[0]])
        for i in range(nrow):
            r0 = rows[files[0]][i]
            rr = [rows[f][i] for f in files]
            assert all(abs(x['q'] - r0['q']) < 1e-9 and x['par'] == r0['par'] and x['s'] == r0['s'] for x in rr)
            graded = abs(r0['A']) >= 0.2
            g = r0['gen']
            fin = rr[-1]                       # finest rho
            spread = {k: max(abs(x[k] - fin[k]) for x in rr) for k in ('kappa0', 'sigma0', 'side0')}
            head = (f"s={r0['s']:+.0f} {r0['par']} lam={r0['lam']:+.6f} A={r0['A']:+.5f}  q={r0['q']:+.6f}"
                    f" ({'R' if r0['right'] else 'mirror'}) gen{g}" + (f" n={r0['n']}" if g == 1 else f" W={r0['W']:.6f}"))
            if g == 1:
                tk, ts, tsd = TOL['k1'], TOL['s1'], TOL['side1']
                sig_pred, side_pred = 1 / 3, -2.0
            else:
                tk, ts, tsd = TOL['k2'], TOL['s2'], TOL['side2']
                sig_pred, side_pred = 0.2, -1.5
            res = dict(k=abs(fin['kappa0'] - 1) <= tk + (spread['kappa0'] if spread['kappa0'] > tk / 2 else 0),
                       s=abs(fin['sigma0'] - sig_pred) <= ts + (spread['sigma0'] if spread['sigma0'] > ts / 2 else 0),
                       side=abs(fin['side0'] - side_pred) <= tsd + (spread['side0'] if spread['side0'] > tsd / 2 else 0),
                       sign=fin['kappa0'] > 0 and abs(fin['side0']) > 1)
            line = (f"   kappa0={fin['kappa0']:.5f} sigma0={fin['sigma0']:.5f} side0={fin['side0']:.5f}"
                    f"  (mesh spread {spread['kappa0']:.1e}/{spread['sigma0']:.1e}/{spread['side0']:.1e})")
            verdict = ''
            if g == 1 and 'b0' in r0:
                b0inf = extrap(rhos, [x['b0'] for x in rr]) if len(rr) > 1 else fin['b0']
                dinf = extrap(rhos, [x['Dfit'] for x in rr]) if len(rr) > 1 else fin['Dfit']
                dev = b0inf + fin['Dpred'] + fin['beta']
                cal = [x['K5cal'] for x in rr]
                ddev = dinf - fin['Dpred']
                res['K5'] = abs(dev) <= TOL['k5'] and all(abs(c) <= TOL['k5'] for c in cal)
                res['K0'] = abs(ddev) <= TOL['d']
                line += (f"\n   K5: beta={fin['beta']:.6f} pred b0=-D-beta={-fin['Dpred']-fin['beta']:+.5f}; raw b0 by rho="
                         + ','.join(f"{x['b0']:+.5f}" for x in rr) + f"; extrapolated dev={dev:+.5f};"
                         f" calibrated (b0+Dfit+beta) by rho=" + ','.join(f'{c:+.5f}' for c in cal)
                         + f"\n   K0': D_fit-D extrapolated={ddev:+.5f} (by rho " + ','.join(f"{x['Dfit']-x['Dpred']:+.5f}" for x in rr) + ')')
            verdict = ' '.join(f'{k}:{pf(v)}' for k, v in res.items())
            print(head + ('' if graded else '   [not graded: |A|<0.2]'))
            print(line)
            print('   ' + verdict)
            if graded:
                for k, v in res.items():
                    key = f'{k}-gen{g}'
                    tally.setdefault(key, [0, 0])
                    tally[key][0] += int(v)
                    tally[key][1] += 1
    print('\n######## tally over graded rows (pass/total)')
    for k, (p, n) in sorted(tally.items()):
        print(f'   {k}: {p}/{n}')


if __name__ == '__main__':
    main()
