"""Apply the PREREG.md tail criteria (T1, T1-full, T1-lambda, T2, gate) to the production runs.
Usage: python tail_summary.py > out/tail_summary.out"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import tail_analyze as TA

PRIMARY = ['E0', 'Em1', 'O5', 'O20']
EXPLOR = ['E1', 'O1']


def pf(ok):
    return 'PASS' if ok else 'FAIL'


def kink_scale(X, T1, T2):
    w = TA.integ(lambda t: 1 / t ** 2, T1, T2)
    return TA.SIGC2(X) * TA.integ(lambda t: 1 / (t * t * TA.a_sym(t) ** 2), T1, T2) / w


tally = {}
for X in (6, 8, 10):
    fine = TA.load(f'out/tail_X{X}_fine.npz')
    base = TA.load(f'out/tail_X{X}_base.npz')
    c = TA.cX(X)
    print(f'\n################ X={X}  L={fine["L"]:.6f}  c_X={c:.6f}  sum c_n^2={TA.SIGC2(X):.4f}  N fine/base={fine["N"]}/{base["N"]}')
    valid = {}
    for nm in PRIMARY + EXPLOR:
        if nm not in fine['st']:
            continue
        st = fine['st'][nm]
        bf, bb = TA.blocks(fine, nm), TA.blocks(base, nm)
        mdiff = max(max(abs(x[2] / y[2] - 1), abs(x[3] / y[3] - 1)) for x, y in zip(bf, bb) if x[0] >= 200)
        lcons = abs(st['lamp_d'] / st['lamp_2d'] - 1)
        ok = lcons <= 3e-3 and mdiff <= 3e-3
        valid[nm] = ok and nm in PRIMARY
        eps = 1 if st['par'] == 'e' else -1
        print(f"\n--- {nm}: s={st['s']:+.0f} {st['par']} lam={st['lam']:+.6f} lam'={st['lamp']:+.5f}"
              f" (base {base['st'][nm]['lamp']:+.5f})  |lam'(d)/lam'(2d)-1|={lcons:.1e}  fine-vs-base blocks {mdiff:.1e}"
              f"  gate {pf(ok)}{'' if nm in PRIMARY else ' [exploratory]'}  Hadamard |lam'|/2A^2={abs(st['lamp'])/(2*st['A']**2):.4f}")
        print('   block          Z/P1     tol    |  Z/P0   E/P0   Z/Plead  alt(no lam-shift)  E/Z-1  P6:2S<a-2>+eps c<1/a>')
        t1 = []; t1alt = []
        for (T1, T2, Z, E), (_, _, Zb, Eb) in zip(bf, bb):
            P0, P1, Pl, ia, ia2 = TA.preds(fine, nm, T1, T2)
            ks = kink_scale(X, T1, T2)
            tol = 2 * ks + 0.005
            alt = Pl * (1 + eps * c * ia)
            if T1 >= 400:
                t1.append(abs(Z / P1 - 1) <= tol)
                t1alt.append(abs(Z / alt - 1) <= tol)
            print(f'   [{T1:5d},{T2:5d}] {Z/P1:7.4f}  {tol:6.4f}  | {Z/P0:6.4f} {E/P0:6.4f} {Z/Pl:7.4f}   {Z/alt:7.4f}        {E/Z-1:+.4f}  {2*ks+eps*c*ia:+.4f}')
        print('   full tail:   T     tau      tau_pred   ratio-1    tol     PredF')
        t1f = []
        for T in TA.TFULL:
            tau = np.pi * T * TA.ztail(fine, nm, T) / abs(st['lamp'])
            pr = T * TA.integ(lambda t: (TA.a_sym(t) + eps * c) / (t * t * (TA.a_sym(t) - st['lam'])), T, 1e7) \
                + T * (1 + eps * c / np.log(1e7 / 2 / np.pi)) / 1e7
            pfF = 1 + (st['lam'] + eps * c) / (np.log(T / 2 / np.pi) + 1 - st['lam'])
            tol = 2 * TA.SIGC2(X) / TA.a_sym(np.array([float(T)]))[0] ** 2 + 0.005
            if T >= 400:
                t1f.append(abs(tau / pr - 1) <= tol)
            print(f'             {T:5d}  {tau:8.4f}  {pr:8.4f}  {tau/pr-1:+8.4f}  {tol:6.4f}  {pfF:8.4f}')
        if nm in PRIMARY:
            res = {'T1': all(t1), 'T1-full': all(t1f)}
            if abs(st['lam']) >= 1:
                res['T1-lambda'] = not all(t1alt)
            print('   ' + ' '.join(f'{k}:{pf(v)}' for k, v in res.items()) + ('' if valid[nm] else '  [gate failed: not graded]'))
            if valid[nm]:
                for k, v in res.items():
                    tally.setdefault(k, [0, 0]); tally[k][0] += int(v); tally[k][1] += 1
    # T2 sector split
    print(f'\n   T2 sector split at X={X}: fit S_k = alpha<1/a> + beta<a^-2> on blocks T1>=200; prediction alpha = 2c_X = {2*c:.4f}')
    for e_ in ('E0', 'Em1', 'E1'):
        for o_ in ('O5', 'O20', 'O1'):
            if e_ not in fine['st'] or o_ not in fine['st']:
                continue
            be, bo = TA.blocks(fine, e_), TA.blocks(fine, o_)
            S, u1, u2, rowtxt = [], [], [], []
            for (T1, T2, Ze, Ee), (_, _, Zo, Eo) in zip(be, bo):
                _, _, _, ia, ia2 = TA.preds(fine, e_, T1, T2)
                sv = np.log(Ze / Ee) - np.log(Zo / Eo)
                rowtxt.append(f'{sv:+.4f}/{2*c*ia:+.4f}')
                if T1 >= 200:
                    S.append(sv); u1.append(ia); u2.append(ia2)
            S, u1, u2 = map(np.array, (S, u1, u2))
            Xm = np.stack([u1, u2], 1)
            co, *_ = np.linalg.lstsq(Xm, S, rcond=None)
            r = S - Xm @ co
            cov = np.linalg.inv(Xm.T @ Xm) * (r @ r) / max(1, len(S) - 2)
            sa = np.sqrt(cov[0, 0])
            a0 = (u1 @ S) / (u1 @ u1)              # beta = 0 fit
            prim = e_ in PRIMARY and o_ in PRIMARY and valid.get(e_) and valid.get(o_)
            ok = abs(co[0] - 2 * c) <= max(0.10, 3 * sa)
            print(f'   ({e_},{o_}): alpha={co[0]:+.4f} +- {sa:.4f}  beta={co[1]:+.4f}   [beta=0: alpha={a0:+.4f}]  '
                  f'{pf(ok) if prim else "(not graded)"}')
            print('        blocks measured/pred(2c<1/a>): ' + ' '.join(rowtxt))
            if prim:
                tally.setdefault(f'T2 X={X}', [0, 0]); tally[f'T2 X={X}'][0] += int(ok); tally[f'T2 X={X}'][1] += 1
print('\n################ tally (pass/total over graded items)')
for k, (p, n) in tally.items():
    print(f'   {k}: {p}/{n}')
