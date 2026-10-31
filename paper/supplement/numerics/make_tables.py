"""LaTeX tables (booktabs) for the kink and tail numerics, generated from data, not typed.
Inputs: kink_errors.json (consolidate_kink.py) and NUMERICS_DIR/out/tail_summary.out ([NUM], registered analysis).
Usage: python3 make_tables.py NUMERICS_DIR   -> tab_kink_gen1.tex, tab_kink_gen2.tex, tab_k5.tex, tab_tail_T1.tex, tab_tail_T2.tex"""
import sys, os, re, json, math
from fractions import Fraction
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
NUM = sys.argv[1]
rows = json.load(open(os.path.join(HERE, 'kink_errors.json')))
TOL = 0.005


def up(e, nd):
    """error rounded up at nd decimals (never shown as 0)."""
    return max(math.ceil(e * 10 ** nd - 1e-9), 1) / 10 ** nd


def cell(vals, errs, nd):
    lo, hi, e = min(vals), max(vals), up(max(errs), nd)
    if f'{lo:.{nd}f}' == f'{hi:.{nd}f}':
        return f'${lo:.{nd}f}\\pm{e:.{nd}f}$'
    return f'$[{lo:.{nd}f},{hi:.{nd}f}]\\pm{e:.{nd}f}$'


FAM = OrderedDict([('L=0.6 right', '0.6'), ('L=0.6 symmetric', '0.6'), ('L=0.8 right', '0.8'),
                   ('L=1.0 right (registered mesh)', '1.0 reg.'), ('L=1.0 sensitivity (gen-2 at 1e-8)', '1.0 sens.'),
                   ('L=1.0 diagnostic (post-registration)', '1.0 diag.$^\\dagger$'),
                   ('L=1.0 K5 rerun, primary (rho 1.5, 1.25)', '1.0 rerun$^\\ddagger$'),
                   ('L=1.0 K5 rerun, supplementary (rho 1.5, 1.25, 1.15)', '1.0 rerun, $\\rho\\to1.15^\\ddagger$')])
SEC = {'e': 'even', 'o': 'odd'}


def groups(gen):
    out = OrderedDict()
    for r in rows:
        if r['gen'] != gen or r['group'] not in FAM:
            continue
        key = (FAM[r['group']], r['s'], r['par'], round(r['A'], 3))
        out.setdefault(key, []).append(r)
    return out


def fv(v):
    """signed value at 4 decimals, or 6 when rounding would hide which side of the tolerance it is on."""
    return f'{v:+.6f}' if abs(abs(v) - TOL) < 5e-5 else f'{v:+.4f}'


def sci(x):
    m, e = f'{x:.0e}'.split('e')
    return f'{m}\\cdot10^{{{int(e)}}}'


def write(name, text):
    open(os.path.join(HERE, name), 'w').write(text)
    print('wrote', name)


def head(cols, spec):
    return f'\\begin{{tabular}}{{{spec}}}\n\\toprule\n' + ' & '.join(cols) + ' \\\\\n\\midrule\n'


# ---------------------------------------------------------------- generation 1 (leading profile)
t = head(['$L$', '$s$', 'sector', '$\\lambda$', '$A$', 'rows', '$\\kappa_0$ (1)', '$\\sigma_0$ ($\\frac13$)',
          'side ($-2$)'], 'lrlrrrlll')
for (fam, s, par, A), rr in groups(1).items():
    if 'rerun, $\\rho' in fam:
        continue                                   # same leading constants as the primary rerun rows
    t += (f'{fam} & {s:+.0f} & {SEC[par]} & ${rr[0]["lam"]:+.4f}$ & ${A:.3f}$ & {len(rr)} & '
          + ' & '.join(cell([x[k]['v'] for x in rr], [x[k]['err'] for x in rr], 4) for k in ('kappa0', 'sigma0', 'side0'))
          + ' \\\\\n')
write('tab_kink_gen1.tex', t + '\\bottomrule\n\\end{tabular}\n')

# ---------------------------------------------------------------- generation 2
t = head(['$L$', 'point', '$W$', '$s$', 'sector', '$A$', 'rows', '$\\kappa_0$ (1)', '$\\sigma_0$ ($\\frac15$)',
          'side ($-\\frac32$)'], 'llrrlrrlll')
for (fam, s, par, A), rr in groups(2).items():
    if 'rerun, $\\rho' in fam:
        continue
    L = float(fam.split()[0])
    for W in sorted({round(x['W'], 6) for x in rr}, reverse=True):
        sub = [x for x in rr if round(x['W'], 6) == W]
        fr = Fraction(math.exp(L - abs(sub[0]['q']) if not sub[0]['right'] else L - sub[0]['q'])).limit_denominator(10)
        pt = f'$L-\\log{fr.numerator}$' if fr.denominator == 1 else f'$L-\\log\\frac{{{fr.numerator}}}{{{fr.denominator}}}$'
        t += (f'{fam} & {pt} & ${W:.4f}$ & {s:+.0f} & {SEC[par]} & ${A:.3f}$ & {len(sub)} & '
              + ' & '.join(cell([x[k]['v'] for x in sub], [x[k]['err'] for x in sub], 4) for k in ('kappa0', 'sigma0', 'side0'))
              + ' \\\\\n')
write('tab_kink_gen2.tex', t + '\\bottomrule\n\\end{tabular}\n')

# ---------------------------------------------------------------- K6 offset (registered K5) and K1 edge offset (registered K0')
t = head(['$L$, mesh', 'state', '$n$', '$\\beta_n$', '$b_0+D+\\beta_n$', '$\\max_\\rho|b_0+D_{\\rm fit}+\\beta_n|$', 'verdict'],
         'llrrlll')
t0 = head(['$L$, mesh', 'state', '$D$', '$D_{\\rm fit}-D$', 'verdict'], 'llrll')
seen, seen0 = set(), set()
for r in rows:
    if r['gen'] != 1 or r['group'] not in FAM or not r['right']:
        continue
    fam = FAM[r['group']]
    key = (fam, r['s'], r['par'], round(r['lam'], 4), r['n'])
    if key in seen:
        continue
    seen.add(key)
    k5, k0 = r['K5'], r['K0']
    post = 'diag' in fam            # rho = 1.35 run has a shorter window: only its rho = 1.5 calibrated value is usable
    cal = abs(r['K5cal'][0]) if post else max(abs(c) for c in r['K5cal'])
    ok5 = abs(k5['v']) <= TOL and cal <= TOL
    ok0 = abs(k0['v']) <= TOL
    st = f'$s={r["s"]:+.0f}$ {SEC[r["par"]]}, $\\lambda={r["lam"]:+.3f}$'
    e5 = f'\\pm{up(k5["err"], 4):.4f}' if k5['err'] > 0 else ''
    e0 = f'\\pm{up(k0["err"], 4):.4f}' if k0['err'] > 0 else ''
    v5 = 'n/a' if post else ('PASS' if ok5 else '\\textbf{FAIL}')
    t += f'{fam} & {st} & {r["n"]} & ${r["beta"]:.3f}$ & ${fv(k5["v"])}{e5}$ & ${cal:.4f}$ & {v5} \\\\\n'
    if (fam, st) not in seen0:
        seen0.add((fam, st))
        D = r['lam'] + 1.8378770664093453 + 0.5772156649015329
        d0, v0 = ('---', 'n/a') if post else (f'${fv(k0["v"])}{e0}$', 'PASS' if ok0 else '\\textbf{FAIL}')
        t0 += f'{fam} & {st} & ${D:+.4f}$ & {d0} & {v0} \\\\\n'
write('tab_k5.tex', t + '\\bottomrule\n\\end{tabular}\n')
write('tab_k0.tex', t0 + '\\bottomrule\n\\end{tabular}\n')

# ---------------------------------------------------------------- tail law T1 (from the registered summary)
txt = open(os.path.join(NUM, 'out', 'tail_summary.out')).read()
t = head(['$X$', 'state', '$\\lambda$', "$|\\lambda'|/2A^2$", 'mesh', '$[100,200]$', '$[400,800]$', '$[1600,3200]$',
          '$[6400,10300]$', '$\\tau/\\tau_{\\rm pred}-1$, $T\\ge400$', 'no $\\lambda$-shift', 'T1'], 'rlrrrrrrrlll')
for blk in re.split(r'(?=################ X=)', txt)[1:]:
    X = int(re.match(r'################ X=(\d+)', blk).group(1))
    for st in re.split(r'(?=\n--- )', blk)[1:]:
        h = re.search(r"--- (\w+): s=([+-]\d+) (\w) lam=([+-][\d.]+) .*?blocks ([\d.e+-]+)\s+gate (\w+)( \[exploratory\])?\s+"
                      r"Hadamard \|lam'\|/2A\^2=([\d.]+)", st)
        if not h or h.group(7):
            continue
        name, lam, mesh, gate, had = h.group(1), float(h.group(4)), float(h.group(5)), h.group(6), float(h.group(8))
        bl = dict(re.findall(r'\[\s*(\d+),\s*\d+\]\s+([\d.]+)', st))
        lead = re.findall(r'\[\s*\d+,\s*\d+\]\s+[\d.]+\s+[\d.]+\s+\|\s+[\d.]+\s+[\d.]+\s+([\d.]+)', st)
        tau = [float(x) for T, x in re.findall(r'^\s+(\d+)\s+[\d.]+\s+[\d.]+\s+([+-][\d.]+)', st, re.M) if int(T) >= 400]
        verdict = 'not graded' if gate == 'FAIL' else ('PASS' if 'T1:PASS' in st else 'FAIL')
        t += (f'{X} & {name} & ${lam:+.3f}$ & ${had:.4f}$ & ${sci(mesh)}$ & ' + ' & '.join(f'${float(bl[k]):.3f}$' for k in ('100', '400', '1600', '6400'))
              + f' & ${min(tau):+.3f}$ to ${max(tau):+.3f}$ & ${float(lead[0]):.2f}\\to{float(lead[-1]):.2f}$ & {verdict} \\\\\n')
write('tab_tail_T1.tex', t + '\\bottomrule\n\\end{tabular}\n')

# ---------------------------------------------------------------- sector split T2
t = head(['$X$', '$2c_X$', 'pair', '$\\alpha\\pm\\sigma_\\alpha$', '$\\beta$', '$(\\alpha-2c_X)/\\sigma_\\alpha$', 'verdict'], 'rrllrrl')
for blk in re.split(r'(?=################ X=)', txt)[1:]:
    X = int(re.match(r'################ X=(\d+)', blk).group(1))
    c2 = 2 * float(re.search(r'c_X=([\d.]+)', blk).group(1))
    for pair, a, sa, b, v in re.findall(r'\((\w+,\w+)\): alpha=([+-][\d.]+) \+- ([\d.]+)\s+beta=([+-][\d.]+).*?\]\s+(PASS|FAIL)', blk):
        a, sa = float(a), float(sa)
        t += f'{X} & ${c2:.3f}$ & ({pair}) & ${a:+.3f}\\pm{sa:.3f}$ & ${float(b):+.2f}$ & ${(a - c2) / sa:+.1f}$ & {v} \\\\\n'
write('tab_tail_T2.tex', t + '\\bottomrule\n\\end{tabular}\n')
