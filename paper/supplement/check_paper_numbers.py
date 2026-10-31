"""Recompute the numbers quoted in Section 10 of the paper (tables, figure caption and text) from the output
files of this supplement, and compare them with the printed values.  Standard library only; < 1 s.
A printed range [lo, hi] passes if lo is min(values) rounded down or to nearest, and hi is max(values) rounded
up or to nearest, at the printed number of decimals.  Usage: python3 check_paper_numbers.py   (from any folder)"""
import json, math, os, re

H = os.path.dirname(os.path.abspath(__file__))
rd = lambda p: open(os.path.join(H, p)).read()
fails = []


def rng(label, vals, lo, hi):
    nd = max(len(s.split('.')[1]) if '.' in s else 0 for s in (lo, hi))
    u = 10.0 ** -nd
    a, b = min(vals), max(vals)
    ok = (any(abs(float(lo) - f(a / u) * u) < u / 10 for f in (math.floor, round))
          and any(abs(float(hi) - f(b / u) * u) < u / 10 for f in (math.ceil, round)))
    print(f"{'OK  ' if ok else 'DIFF'} {label}: paper {lo}..{hi}, data {a:.{nd + 2}f}..{b:.{nd + 2}f} (n={len(vals)})")
    ok or fails.append(label)


def num(pat, txt, cast=float):
    return [cast(x) for x in re.findall(pat, txt)]


# ---------------- Table 2 (tab:H): -lambda'/(2A^2)
p0 = 'unregistered/p0/'
rng('tab:H pure log L=0.5 (2LA^2, h0=L/500, rho->1)', num(r'h0=L/500 \w+: A\(rho->1\) = [\d.]+  2L\*A\^2 = ([\d.]+)', rd(p0 + 'conv_purelog.out')), '1.00020', '1.00062')
w3 = rd(p0 + 'weil_L0.3.out').split('delta=0.001')[1]
rng('tab:H Weil L=0.3', num(r'-lam\'/\(2A\^2\) = ([\d.]+)', w3), '0.99949', '0.99982')
rng('tab:H Weil L=0.4 graded', num(r'-lam\'/\(2A\^2\)=([\d.]+)', rd(p0 + 'anchor_L0.4_NH500.out')), '0.99812', '0.99975')
ev = rd(p0 + 'evidence.out')
rng('tab:H Weil L=0.4 graded, refined', num(r'\(\+rho shift\): A=[\d.]+ ratio=([\d.]+)', ev), '1.00020', '1.00026')
rng('tab:H Weil L=0.6 graded', num(r'NH500 rho->1: ([\d.]+)', ev), '0.99724', '0.99969')
rng('tab:H Weil L=0.6 graded, refined', num(r'at rho=1.5\): ([\d.]+)', ev), '0.99943', '1.00007')
rng('tab:H contrast L=0.4 ungraded', num(r'= ([\d.]+)  \[', rd(p0 + 'weil_L0.4.out').split('delta=0.001')[1]), '0.995', '0.998')
rng('tab:H contrast, refined (h0=L/1000)', num(r'= ([\d.]+)  \[', rd(p0 + 'weil_L0.4_NH1000.out')), '0.9996', '1.006')
hp = [x for L in ('0.36', '0.4', '0.6', '0.7') for x in num(r'2A\^2\)=([\d.]+)', rd(f'unregistered/hp/excited_L{L}.out'))]
rng('tab:H hp-FEM, all but the disclosed L=0.7 s=1 e0', [x for x in hp if abs(x - 0.99151) > 1e-6], '0.9987', '1.0024')
ts = rd('registered/out/tail_summary.out').split('################ tally')[0]
st = {}
for blk in re.split(r'(?=################ X=)', ts)[1:]:
    X = int(re.match(r'################ X=(\d+)', blk).group(1))
    for s in re.split(r'(?=\n--- )', blk)[1:]:
        h = re.search(r"--- (\w+): .*gate (\w+)( \[exploratory\])?\s+Hadamard \|lam'\|/2A\^2=([\d.]+)", s)
        if h and not h.group(3):
            st[X, h.group(1)] = dict(had=float(h.group(4)), blocks={int(a): (float(b), float(c), float(d)) for a, b, c, d in re.findall(
                r'\[\s*(\d+),\s*\d+\]\s+([\d.]+)\s+([\d.]+)\s+\|\s+[\d.]+\s+[\d.]+\s+[\d.]+\s+([\d.]+)', s)},
                tau={int(a): float(b) for a, b in re.findall(r'^\s+(\d+)\s+([\d.]+)\s+[\d.]+\s+[+-][\d.]+', s, re.M)})
assert len(st) == 12
rng('tab:H P1, 12 tail states', [v['had'] for v in st.values()], '0.9960', '1.0097')
rng('Sec. 10.1 explicit formula vs edge fit, L=0.4, |A_fit/A_pred-1| in units of 1e-5',
    [abs(x - 1) * 1e5 for x in num(r'A_fit/A_pred = ([\d.]+)', rd('unregistered/hp/check_explicit_and_Vfit_L0.4.out'))], '1', '23')

# ---------------- Tables 3-4 (tab:kink1, tab:kink2) and kink text: registered graded rows
K = json.load(open(os.path.join(H, 'numerics/kink_errors.json')))
REG = ('L=0.6 right', 'L=0.6 symmetric', 'L=0.8 right', 'L=1.0 right (registered mesh)', 'L=1.0 sensitivity (gen-2 at 1e-8)')
for gen, n, exp in ((1, 50, (('0.9986', '1.0019'), ('0.3322', '0.3346'), ('-2.0035', '-1.9969'))), (2, 20, None)):
    rows = [r for r in K if r['gen'] == gen and r['group'] in REG]
    print(f"{'OK  ' if len(rows) == n else 'DIFF'} registered graded generation-{gen} rows: {len(rows)} (paper {n})")
    if exp:
        for key, (lo, hi) in zip(('kappa0', 'sigma0', 'side0'), exp):
            rng(f'gen-1 {key}', [r[key]['v'] for r in rows], lo, hi)
ks = rd('registered/out/kink_summary.out')
graded = [b for b in re.split(r'\n(?=s=[+-])', ks) if 'not graded' not in b and 'sign:' in b]
print(f"{'OK  ' if len(graded) == 70 and all('sign:PASS' in b for b in graded) else 'DIFF'} sign PASS in all {len(graded)} graded rows (paper 70)")

# ---------------- Table 5 (tab:k0) and Table 6 (tab:k5): K0' and K5 deviations per family
g1 = lambda grp, par=None: [r for r in K if r['gen'] == 1 and r['right'] and r['group'] == grp and (par is None or r['par'] == par)]
rng("K0' main meshes L=0.6, 0.8, 1.0 reg", [r['K0']['v'] for g in REG[:4] for r in g1(g)], '0.0013', '0.0049')
rng("K0' sensitivity mesh", [r['K0']['v'] for r in g1(REG[4])], '0.0081', '0.0094')
RR, RS = 'L=1.0 K5 rerun, primary (rho 1.5, 1.25)', 'L=1.0 K5 rerun, supplementary (rho 1.5, 1.25, 1.15)'
rng("K0' rerun, even", [r['K0']['v'] for r in g1(RR, 'e')], '0.0039', '0.0039')
rng("K0' rerun, odd (registered FAIL)", [r['K0']['v'] for r in g1(RR, 'o')], '0.00510', '0.00510')
rng("K0' rerun rho->1.15, odd (FAIL)", [r['K0']['v'] for r in g1(RS, 'o')], '0.005005', '0.005005')
k5 = lambda rows: [r['K5']['v'] for r in rows]
rng('K5 L=0.6, four states', k5(g1('L=0.6 right')), '-0.0018', '-0.0005')
rng('K5 L=0.8 even', k5(g1('L=0.8 right', 'e')), '-0.0007', '-0.0005')
rng('K5 L=0.8 odd', k5(g1('L=0.8 right', 'o')), '-0.0025', '-0.0021')
reg = g1(REG[3])
rng('K5 L=1.0 reg, n=3,4,5,7 (FAIL)', k5([r for r in reg if r['n'] != 2]), '0.0102', '0.0609')
rng('K5 L=1.0 reg, n=2', k5([r for r in reg if r['n'] == 2]), '-0.0017', '-0.0003')
rng('K5 L=1.0 sens (raw)', k5(g1(REG[4])), '-0.0172', '-0.0048')
rng('K5 L=1.0 diagnostic', k5(g1('L=1.0 diagnostic (post-registration)')), '-0.0040', '-0.0007')
rng('K5 rerun even', k5(g1(RR, 'e')), '-0.0005', '-0.0003')
rng('K5 rerun odd', k5(g1(RR, 'o')), '-0.0019', '-0.0017')
rng('K5 rerun rho->1.15', k5(g1(RS)), '-0.0019', '-0.0004')
rng('K5 rerun calibrated, every rho', [abs(c) for r in g1(RR) + g1(RS) for c in r['K5cal']], '0.0030', '0.0035')

# ---------------- Tail law (text of Section 10.3), registered
B = lambda T, i: [v['blocks'][T][i] for v in st.values()]
rng('T1 Z/Z_pred on [100,200]', B(100, 0), '0.80', '0.98')
rng('T1 Z/Z_pred on [6400,10300]', B(6400, 0), '0.968', '1.000')
rng('T1 without lambda-shift', [v['blocks'][T][2] for v in st.values() for T in v['blocks']], '0.20', '0.87')
rng('T1 tolerance on [400,800]', B(400, 1), '0.13', '0.21')
rng('Upsilon(6400) = pi T Z/|lambda\'|', [v['tau'][6400] for v in st.values()], '0.42', '0.88')
al = {X: [(float(a), float(s)) for a, s in re.findall(r'alpha=([+-][\d.]+) \+- ([\d.]+).*?\]\s+(?:PASS|FAIL)', b)]   # graded pairs
      for X, b in zip((6, 8, 10), re.split(r'(?=################ X=)', ts)[1:])}
rng('T2 alpha, X=8', [a for a, s in al[8]], '0.51', '0.67')
rng('T2 (alpha-2c_8)/sigma, X=8 high pairs', sorted((a - 0.490129) / s for a, s in al[8])[-2:], '2.6', '3.0')
rng('T2 alpha, X=6 (paper prints 0.02+-0.07)', [a for a, s in al[6]], '0.01', '0.02')
rng('T2 alpha, X=10', [a for a, s in al[10]], '0.32', '0.44')

# ---------------- The term eps c_X (not registered)
zs = rd('unregistered/zero_side/zero_side_split.out')
parts = [p for p in re.split(r'\n(?=L=)', zs) if p.startswith('L=')]
blk = lambda p, col: num(r'\[(?:250,500|500,1000|1000,1981)\]\s+' + r'([\d.]+)\s+' * (col + 1), p)[col::col + 1] if col else num(r'\[(?:250,500|500,1000|1000,1981)\]\s+([\d.]+)', p)
cx = [p for p in parts if 'c_X=0.00000' not in p]
rng('X=2,3 with c_X', [x for p in cx for x in blk(p, 0)], '0.968', '1.014')
noX = lambda par: [float(x) for p in cx for x in re.findall(r'\[(?:250,500|500,1000|1000,1981)\]\s+[\d.]+\s+([\d.]+)', p.split('[o]')[0 if par == 'e' else 1])]
rng('X=2,3 without c_X, even', noX('e'), '1.09', '1.13')
rng('X=2,3 without c_X, odd', noX('o'), '0.86', '0.91')
rng('control L=0.4', [x for p in parts if 'c_X=0.00000' in p for x in blk(p, 0)], '0.971', '0.999')
x4 = rd('unregistered/zero_side/split_x4_check.out').split(' s=0 o:')[0]
rows4 = re.findall(r'\[(?:100,200|200,400|400,800|800,1600)\]\s+([\d.]+)\s+([\d.]+)', x4)
rng('X=4 even, with c_4', [float(b) for a, b in rows4], '0.989', '0.994')
rng('X=4 even, without c_4', [float(a) for a, b in rows4], '1.06', '1.10')
lan = re.findall(r'X= ?(\d+): .*T=  10303: S= *([-\d.]+) pred= *([-\d.]+)', rd('unregistered/zero_side/fr_constants.out'))
dev = [abs(float(s) / float(p) - 1) for X, s, p in lan if X in ('2', '3', '4', '8')]
print(f"{'OK  ' if max(dev) < 0.005 else 'DIFF'} Landau sign check at T=10303, X=2,3,4,8: max rel. dev {max(dev):.4f} (paper: within 0.5%)")
max(dev) < 0.005 or fails.append('Landau')

print('\nALL OK' if not fails else f'\n{len(fails)} MISMATCH(ES): ' + '; '.join(fails))
