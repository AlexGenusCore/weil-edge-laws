"""Tail analysis of tail_run.py output.
  python tail_analyze.py conv base.npz other.npz ...   -> mesh-to-mesh differences only
  python tail_analyze.py test run.npz [run2.npz ...]   -> measured vs predicted (after PREREG)"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import p1weil as W

BLOCKS = [(100, 200), (200, 400), (400, 800), (800, 1600), (1600, 3200), (3200, 6400), (6400, 10300)]
TFULL = [100, 200, 400, 800, 1600, 3200, 6400]
STATES = ['E0', 'Em1', 'O5', 'O20', 'E1', 'O1']
gx, gw = np.polynomial.legendre.leggauss(40)


def a_sym(t):
    z = 0.25 + 0.5j * t
    z2 = 1 / (z * z)
    ser = np.log(z) - 0.5 / z - z2 * (1 / 12 - z2 * (1 / 120 - z2 * (1 / 252 - z2 * (1 / 240 - z2 / 132))))
    return ser.real - np.log(np.pi)


def integ(fun, T1, T2):
    """int_{T1}^{T2} fun(t) dt on a log scale (Gauss 40 per factor 2)."""
    tot = 0.0
    lo = T1
    while lo < T2:
        hi = min(2 * lo, T2)
        u = np.log(lo) + (np.log(hi) - np.log(lo)) * 0.5 * (gx + 1)
        t = np.exp(u)
        tot += 0.5 * (np.log(hi) - np.log(lo)) * np.sum(gw * fun(t) * t)
        lo = hi
    return tot


def cX(X):
    for n, lam in W.prime_powers(X + 1):
        if n == int(round(X)) and abs(X - n) < 1e-12:
            return lam / np.sqrt(n)
    return 0.0


def load(path):
    z = np.load(path, allow_pickle=True)
    d = dict(X=float(z['X']), L=float(z['L']), zeros=z['zeros'], T0=int(z['T0']), N=int(z['N']), st={})
    for nm in STATES:
        if f'{nm}_lam' not in z:
            continue
        g = {k[len(nm) + 1:]: z[k] for k in z.files if k.startswith(nm + '_')}
        d['st'][nm] = dict(lam=float(g['lam']), par=str(g['par']), s=float(g['s']), A=float(g['A']),
                           Am=float(g['Am']), lamp=float(g['lamp']), lamp_d=float(g['lamp_d']),
                           lamp_2d=float(g['lamp_2d']), Q1=float(g['Q1']), F2z=g['F2z'], Eunit=g['Eunit'],
                           Munit=g['Munit'], Dfit=float(g['Dfit']))
    return d


def blocks(d, nm):
    st = d['st'][nm]
    zs = d['zeros']
    out = []
    for T1, T2 in BLOCKS:
        Z = 2 * st['F2z'][(zs > T1) & (zs <= T2)].sum()
        E = st['Eunit'][T1 - d['T0']:T2 - d['T0']].sum() / np.pi
        out.append((T1, T2, Z, E))
    return out


def ztail(d, nm, T):
    st = d['st'][nm]
    return st['Q1'] - 2 * st['F2z'][d['zeros'] <= T].sum()


def conv(paths):
    ds = [load(p) for p in paths]
    base = ds[0]
    print('reference', paths[0], 'N =', base['N'])
    for nm in base['st']:
        b = base['st'][nm]
        print(f"{nm}: lam={b['lam']:+.8f} lam'={b['lamp']:+.5f} (d: {b['lamp_d']:+.5f}, 2d: {b['lamp_2d']:+.5f}) 2A^2={2*b['A']**2:.5f}")
        for p, d in zip(paths[1:], ds[1:]):
            if nm not in d['st']:
                continue
            o = d['st'][nm]
            print(f"   vs {os.path.basename(p)} (N={d['N']}): dlam={o['lam']-b['lam']:+.1e} dlam'/lam'={o['lamp']/b['lamp']-1:+.1e}"
                  f" dA/A={o['A']/b['A']-1:+.1e}")
            bb, ob = blocks(base, nm), blocks(d, nm)
            print('      Z blocks rel diff: ' + ' '.join(f'{x[2]/y[2]-1:+.1e}' for x, y in zip(ob, bb)))
            print('      E blocks rel diff: ' + ' '.join(f'{x[3]/y[3]-1:+.1e}' for x, y in zip(ob, bb)))
            print('      full Z(T) rel diff: ' + ' '.join(f'{ztail(d, nm, T)/ztail(base, nm, T)-1:+.1e}' for T in TFULL))


def preds(d, nm, T1, T2):
    st = d['st'][nm]
    lam, lp = st['lam'], abs(st['lamp'])
    eps = 1 if st['par'] == 'e' else -1
    c = cX(d['X'])
    P0 = lp / np.pi * integ(lambda t: a_sym(t) / (t * t * (a_sym(t) - lam)), T1, T2)
    P1 = lp / np.pi * integ(lambda t: (a_sym(t) + eps * c) / (t * t * (a_sym(t) - lam)), T1, T2)
    Pl = lp / np.pi * (1 / T1 - 1 / T2)
    w = integ(lambda t: 1 / t ** 2, T1, T2)
    ia = integ(lambda t: 1 / (t * t * a_sym(t)), T1, T2) / w
    ia2 = integ(lambda t: 1 / (t * t * a_sym(t) ** 2), T1, T2) / w
    return P0, P1, Pl, ia, ia2


SIGC2 = lambda X: sum((lam / np.sqrt(n)) ** 2 for n, lam in W.prime_powers(X))


def test(paths):
    for p in paths:
        d = load(p)
        X = d['X']; c = cX(X)
        print(f"===== X={X:g} L={d['L']:.6f} c_X={c:.4f} sum_n<X c_n^2={SIGC2(X):.4f}  ({os.path.basename(p)}, N={d['N']})")
        for nm, st in d['st'].items():
            eps = 1 if st['par'] == 'e' else -1
            print(f"--- {nm}: s={st['s']} {st['par']} lam={st['lam']:+.6f} lam'={st['lamp']:+.5f} (d {st['lamp_d']:+.5f}, 2d {st['lamp_2d']:+.5f})"
                  f" 2A^2={2*st['A']**2:.5f} [Hadamard ratio {abs(st['lamp'])/(2*st['A']**2):.4f}]")
            print('     block        Z/Plead  Z/P0    Z/P1    E/P0    pred P1/P0  -S<a^-2>  Z/E')
            for T1, T2, Z, E in blocks(d, nm):
                P0, P1, Pl, ia, ia2 = preds(d, nm, T1, T2)
                print(f'   [{T1:5d},{T2:5d}] {Z/Pl:7.4f} {Z/P0:7.4f} {Z/P1:7.4f} {E/P0:7.4f}   {P1/P0:7.4f}   {-SIGC2(X)*ia2:+.4f}  {Z/E:7.4f}')
            lp = abs(st['lamp'])
            print('     full tail  tau=piTZ/|lam\'|   pred T*int(a+eps c)/(t^2(a-lam))   PredF 1+(lam+eps c)/(log(T/2pi)+1-lam)')
            for T in TFULL:
                tau = np.pi * T * ztail(d, nm, T) / lp
                pr = T * integ(lambda t: (a_sym(t) + eps * c) / (t * t * (a_sym(t) - st['lam'])), T, 1e7) \
                    + T * (1 + eps * c / np.log(1e7 / 2 / np.pi)) / 1e7
                pf = 1 + (st['lam'] + eps * c) / (np.log(T / 2 / np.pi) + 1 - st['lam'])
                print(f'   T={T:5d}   {tau:8.4f}     {pr:8.4f}     {pf:8.4f}')
        # sector splits
        ev = [nm for nm in d['st'] if d['st'][nm]['par'] == 'e']
        od = [nm for nm in d['st'] if d['st'][nm]['par'] == 'o']
        for e_ in ev:
            for o_ in od:
                be, bo = blocks(d, e_), blocks(d, o_)
                print(f'   split ln(Z/E)[{e_}] - ln(Z/E)[{o_}]  vs 2c_X<1/a>:')
                for (T1, T2, Ze, Ee), (_, _, Zo, Eo) in zip(be, bo):
                    _, _, _, ia, ia2 = preds(d, e_, T1, T2)
                    print(f'      [{T1:5d},{T2:5d}] {np.log(Ze/Ee) - np.log(Zo/Eo):+.4f}   pred {2*c*ia:+.4f}   <1/a>={ia:.4f}')


if __name__ == '__main__':
    mode = sys.argv[1]
    {'conv': conv, 'test': test}[mode](sys.argv[2:])
