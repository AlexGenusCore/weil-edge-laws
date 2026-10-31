"""Tail runs at X = e^{2L}: eigenfunctions, lambda' (backward differences), edge traces, and the zero
side 2|F(gamma)|^2 at zeta zeros, plus per-unit-interval integrals of a(t)|F(t)|^2.
Usage: python tail_run.py X tag rho1 rmin1 rho2 rmin2 Hdiv d out.npz
  (rho1, rmin1): grading at generation-1 points; (rho2, rmin2): generation 2 (rho2=0: not graded).
  Edges always graded to 1e-40 with ratio 1.25 (edge fits need ell up to ~90).
States (pre-registered rule, PREREG.md):
  E0 = s=0 even ground state;  O5 = s=5 odd ground state;
  Em1 = s=-1 even ground state;  O20 = s=20 odd ground state;
  E1 = s=1 lowest even state with |A| >= 1;  O1 = s=1 lowest odd state with |A| >= 1.
"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import runlib as R
import p1weil as W

X = float(sys.argv[1]); tag = sys.argv[2]
rho1, rmin1, rho2, rmin2, Hdiv, d = map(float, sys.argv[3:9])
out = sys.argv[9]
L0 = np.log(X) / 2
zeros = np.loadtxt(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'zeros.txt'))
EDGE = (1e-40, 1.25)


def a_sym(t):
    """a(t) = Re psi(1/4 + i t/2) - log(pi), asymptotic series (t >= 50: error < 1e-15)."""
    z = 0.25 + 0.5j * t
    z2 = 1 / (z * z)
    ser = np.log(z) - 0.5 / z - z2 * (1 / 12 - z2 * (1 / 120 - z2 * (1 / 252 - z2 * (1 / 240 - z2 / 132))))
    return ser.real - np.log(np.pi)


def run_L(L):
    an, cp = R.anchors(L, EDGE, (rmin1, rho1), (rmin2, rho2) if rho2 > 0 else None)
    mesh = W.make_mesh(L, an, L / Hdiv)
    asm = W.assemble(mesh)
    res = {s: W.eig(asm, s=s, k=2) for s in (0.0, -1.0, 5.0, 20.0)}
    res[1.0] = W.eig(asm, s=1.0, k=40)
    return mesh, asm, res


def sample(asm, f, L, n=4001):
    """eigenfunction on the scaled grid u = x/L in (-1, 1) (for matching across L)."""
    m = asm['mesh']
    xn = m['A'] + m['o']
    u = np.linspace(-1, 1, n)
    return np.interp(u * L, xn, np.concatenate([[0.0], f, [0.0]]))


t0 = time.time()
mesh, asm, res = run_L(L0)
print(f'X={X} L={L0:.6f} N={len(asm["Q0"])} {time.time()-t0:.0f}s', flush=True)
sel = {}
sel['E0'] = (0.0, [e for e in res[0.0] if e['par'] == 'e'][0])
sel['O5'] = (5.0, [e for e in res[5.0] if e['par'] == 'o'][0])
sel['Em1'] = (-1.0, [e for e in res[-1.0] if e['par'] == 'e'][0])
sel['O20'] = (20.0, [e for e in res[20.0] if e['par'] == 'o'][0])
for nm, par in (('E1', 'e'), ('O1', 'o')):
    for e in res[1.0]:
        if e['par'] == par and abs(R.edge_fit(asm, e['f'], L0)['A']) >= 1:
            sel[nm] = (1.0, e)
            break
info = {}
for nm, (s, e) in sel.items():
    ef = R.edge_fit(asm, e['f'], L0)
    efm = R.edge_fit(asm, e['f'], L0, sign=-1)
    info[nm] = dict(s=s, lam=e['lam'], par=e['par'], A=ef['A'], Am=efm['A'], Dfit=ef['D'], rms=ef['rms'],
                    Q1=W.qform(asm, e['f'], 1.0), samp=sample(asm, e['f'], L0),
                    idx=[x for x in res[s] if x['par'] == e['par']].index(e))
    print(f"  {nm}: s={s} {e['par']} lam={e['lam']:+.10f} A+={ef['A']:+.6f} A-={efm['A']:+.6f} D-Dpred={ef['D']-e['lam']-R.DSHIFT:+.4f}"
          f" (#{info[nm]['idx']} in sector)", flush=True)
# zero side and per-unit Fourier integrals
gx, gw = np.polynomial.legendre.leggauss(6); gx = 0.5 * (gx + 1); gw = 0.5 * gw
T0, T1 = 50, int(zeros[-1])
tg = (np.arange(T0, T1)[:, None] + gx[None, :]).ravel()
ag = a_sym(tg)
for nm, (s, e) in sel.items():
    F = W.fourier(asm, e['f'], zeros)
    info[nm]['F2z'] = np.abs(F) ** 2
    Fg = np.abs(W.fourier(asm, e['f'], tg)) ** 2
    info[nm]['Eunit'] = ((ag * Fg).reshape(-1, 6) @ gw)       # int_k^{k+1} a |F|^2
    info[nm]['Munit'] = (Fg.reshape(-1, 6) @ gw)               # int_k^{k+1} |F|^2
print(f'  Fourier done {time.time()-t0:.0f}s', flush=True)
# backward differences
lams = {nm: [v['lam']] for nm, v in info.items()}
for j, Lx in enumerate((L0 - d, L0 - 2 * d, L0 - 4 * d)):
    m2, a2, r2 = run_L(Lx)
    for nm, v in info.items():
        cands = [x for x in r2[v['s']] if x['par'] == v['par']]
        ov = [abs(np.dot(sample(a2, x['f'], Lx), v['samp'])) / np.linalg.norm(sample(a2, x['f'], Lx)) / np.linalg.norm(v['samp'])
              for x in cands]
        b = int(np.argmax(ov))
        lams[nm].append(cands[b]['lam'])
        v.setdefault('match', []).append((b, max(ov)))
    print(f'  L={Lx:.6f} done {time.time()-t0:.0f}s', flush=True)
for nm, v in info.items():
    l0, l1, l2, l4 = lams[nm]
    dd = (3 * l0 - 4 * l1 + l2) / (2 * d)
    d2 = (3 * l0 - 4 * l2 + l4) / (4 * d)
    v['lams'] = np.array(lams[nm])
    v['lamp_d'] = dd; v['lamp_2d'] = d2; v['lamp'] = (4 * dd - d2) / 3
    print(f"  {nm}: lam'(d)={dd:+.6f} lam'(2d)={d2:+.6f} Richardson={v['lamp']:+.6f}  2A^2={2*v['A']**2:.6f}"
          f"  match={v['match']}", flush=True)
save = dict(X=X, L=L0, tag=tag, N=len(asm['Q0']), zeros=zeros, T0=T0, d=d,
            params=np.array([rho1, rmin1, rho2, rmin2, Hdiv]))
for nm, v in info.items():
    for kk, vv in v.items():
        if kk in ('samp', 'match'):
            continue
        save[f'{nm}_{kk}'] = np.asarray(vv) if not isinstance(vv, str) else vv
np.savez(out, **save)
print(f'saved {out} {time.time()-t0:.0f}s', flush=True)
