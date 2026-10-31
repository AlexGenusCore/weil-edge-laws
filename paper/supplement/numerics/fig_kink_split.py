"""Figure: generation-1 kink profile (the 2/3 : -1/3 split) against the prediction, from existing [NUM] data.

Data: numerics/out/k06_r1.15.json (L = 0.6, s = 0, even ground state, right side, rho = 1.15, r_min = 1e-40).
The fits replicate kink_analyze.py (registered window ell in [20, ell_max - 6]):
  A from psi(L - r)^-2 = a0 ell + a1 + a2/ell + a3/ell^2;  psi(q) from the cusp fit (the node value at q is truncated).
Plotted: u_src = [psi(q - r) - psi(q)] ell^{3/2}/(c_n A) -> 2/3 and u_oth = [psi(q + r) - psi(q)] ell^{3/2}/(c_n A) -> -1/3.
Usage: python3 fig_kink_split.py NUMERICS_DIR   (writes fig_kink_split.pdf next to this file)"""
import sys, os, json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

d = json.load(open(os.path.join(sys.argv[1], 'out', 'k06_r1.15.json')))
L = d['L']
st = [s for s in d['states'] if s['s'] == 0 and s['par'] == 'e'][0]
num = lambda k: float(k.replace('np.float64(', '').rstrip(')'))
chain = {num(k): v for k, v in d['chain'].items()}

# edge trace A (kink_analyze.edge, lmin = 20, lcut = 6)
r = np.array(st['edge+']['r']); v = np.array(st['edge+']['v']); ell = -np.log(r)
lmax_e = ell.max() - 6
m = (ell >= 20) & (ell <= lmax_e)
X = np.stack([ell[m], np.ones(m.sum()), 1 / ell[m], 1 / ell[m] ** 2], 1)
A = np.linalg.lstsq(X, v[m] ** -2.0, rcond=None)[0][0] ** -0.5

curves = {}
for key, pt in st['pts'].items():
    q = num(key)
    gen, w = [val for p, val in chain.items() if abs(p - q) < 1e-9][0]
    if gen != 1:
        continue
    n = int(round(np.exp(L - q)))
    rl, vl, rr, vr = map(np.array, (pt['rl'], pt['vl'], pt['rr'], pt['vr']))
    j = np.searchsorted(rr, rl).clip(0, len(rr) - 1)
    both = np.isclose(rr[j], rl, rtol=1e-12, atol=0)
    rl, vl, vr = rl[both], vl[both], vr[j[both]]
    el = -np.log(rl)
    lmax = min(el.max(), lmax_e + 6) - 6
    mm = (el >= 20) & (el <= lmax)
    Xc = np.stack([np.ones(mm.sum())] + [w * A * el[mm] ** (-1.5 - k) for k in range(3)], 1)
    cs = np.linalg.lstsq(Xc, (vl + vr)[mm], rcond=None)[0]
    psi_q = cs[0] / 2
    Xk = np.stack([el[mm] ** -k for k in range(3)], 1)
    kap = np.linalg.lstsq(Xk, ((vl - vr) * el ** 1.5 / (w * A))[mm], rcond=None)[0][0]
    sig = cs[1]
    keep = el <= lmax                     # plot through the end of the fit window (nodes near r_min are truncated)
    el, vl, vr = el[keep], vl[keep], vr[keep]
    curves[n] = dict(ell=el, src=(vl - psi_q) * el ** 1.5 / (w * A), oth=(vr - psi_q) * el ** 1.5 / (w * A),
                     kappa0=kap, sigma0=sig, lmax=lmax)
    print(f'n={n} q={q:+.5f} c_n={w:.6f} A={A:.5f} kappa0={kap:.5f} sigma0={sig:.5f} '
          f'source-side limit {(kap + sig) / 2:.5f} (2/3), other side {(sig - kap) / 2:.5f} (-1/3)')

# self-check against the registered table (numerics/out/kink_table.out, L = 0.6 right, rho = 1.15)
assert abs(A - 1.5671) < 1e-4, A
assert abs(curves[2]['kappa0'] - 1.00014) < 2e-5 and abs(curves[2]['sigma0'] - 0.33345) < 2e-5
assert abs(curves[3]['kappa0'] - 1.00014) < 2e-5 and abs(curves[3]['sigma0'] - 0.33344) < 2e-5

plt.rcParams.update({'font.family': 'serif', 'mathtext.fontset': 'cm', 'font.size': 9, 'pdf.fonttype': 42,
                     'axes.linewidth': 0.6, 'xtick.major.width': 0.6, 'ytick.major.width': 0.6})
fig, ax = plt.subplots(figsize=(5.0, 3.0))
lo, hi = 20, curves[2]['lmax']
ax.axvspan(lo, hi, color='0.93', lw=0, zorder=0)
ax.text((lo + hi) / 2, 0.88, 'fit window', ha='center', va='center', fontsize=8, color='0.35')
for y, lab in ((2 / 3, r'$+\frac{2}{3}$'), (-1 / 3, r'$-\frac{1}{3}$')):
    ax.axhline(y, color='black', lw=0.8, ls=(0, (5, 3)), zorder=1)
    ax.text(97, y, lab, ha='left', va='center', fontsize=10)
c = curves[2]
ax.plot(c['ell'], c['src'], color='black', lw=1.4, zorder=3, label=r'$n=2$ (line)')
ax.plot(c['ell'], c['oth'], color='black', lw=1.4, zorder=3)
c = curves[3]
sel = np.r_[0:len(c['ell']):12]
ax.plot(c['ell'][sel], c['src'][sel], ls='none', marker='o', ms=4.2, mfc='white', mec='0.35', mew=0.9, zorder=4,
        label=r'$n=3$ (open circles)')
ax.plot(c['ell'][sel], c['oth'][sel], ls='none', marker='o', ms=4.2, mfc='white', mec='0.35', mew=0.9, zorder=4)
ax.plot([], [], color='black', lw=0.8, ls=(0, (5, 3)), label='prediction')
ax.text(8, 0.74, r'source side $z-r$', fontsize=8)
ax.text(8, -0.26, r'far side $z+r$', fontsize=8)
ax.set_xlim(0, 96)
ax.set_ylim(-0.55, 0.95)
ax.set_xlabel(r'$\ell=\log(1/r)$')
ax.set_ylabel(r'$[\psi(z\mp r)-\psi(z)]\,\ell^{3/2}/(c_nA)$')
ax.legend(loc='center', bbox_to_anchor=(0.55, 0.47), fontsize=7.5, frameon=False, handlelength=2.4)
for s in ('top', 'right'):
    ax.spines[s].set_visible(False)
fig.tight_layout()
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fig_kink_split.pdf')
fig.savefig(out)
print('wrote', out)
