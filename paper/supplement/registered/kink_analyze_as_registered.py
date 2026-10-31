"""Analyse kink_run.py output: edge law K0', first-generation jump/cusp/side (K1), K5 offset,
generation-2 profile (K2).  Usage: python kink_analyze.py out.json [lmin] [lcut]"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import p1weil as W

DSHIFT = np.log(2 * np.pi) + W.EG


def cn_table(L):
    return {n: lam / np.sqrt(n) for n, lam in W.prime_powers(np.exp(2 * L))}


def W2(L, n):
    """Weight of length-2 chains from +L landing on y_n = L - log n (generic L)."""
    c = cn_table(L)
    w = 0.0
    for a in c:
        for b in c:
            if a * b == n:
                w += c[a] * c[b]
            if a == n * b:
                w += c[a] * c[b]
    return w


def fit(ell, y, lmin, lmax, nterm=3):
    m = (ell >= lmin) & (ell <= lmax)
    X = np.stack([ell[m] ** (-k) for k in range(nterm)], 1)
    co, *_ = np.linalg.lstsq(X, y[m], rcond=None)
    return co, np.abs(X @ co - y[m]).max()


def edge(st, sign, lmin, lcut):
    e = st['edge+' if sign > 0 else 'edge-']
    r = np.array(e['r']); v = np.array(e['v'])
    ell = -np.log(r)
    lmax = ell.max() - lcut
    m = (ell >= lmin) & (ell <= lmax)
    X = np.stack([ell[m], np.ones(m.sum()), 1 / ell[m], 1 / ell[m] ** 2], 1)
    co, *_ = np.linalg.lstsq(X, v[m] ** -2.0, rcond=None)
    A = np.sign(v[m][-1]) * co[0] ** -0.5
    return dict(A=A, D=-co[1] / co[0], ell=ell, v=v, lmax=lmax)


def analyse(path, lmin=12.0, lcut=6.0, quiet=False):
    d = json.load(open(path))
    num = lambda k: float(k.replace('np.float64(', '').rstrip(')'))
    L = d['L']
    c = cn_table(L)
    chain = {num(k): v for k, v in d['chain'].items()}
    rows = []
    for st in d['states']:
        ep = edge(st, +1, lmin, lcut)
        em = edge(st, -1, lmin, lcut) if d.get('mirror', True) else dict(A=(1 if st['par'] == 'e' else -1) * ep['A'], D=np.nan)
        Dp = st['lam'] + DSHIFT
        head = dict(L=L, rho=d['rho'], s=st['s'], par=st['par'], lam=st['lam'], A=ep['A'], Am=em['A'],
                    Dfit=ep['D'], Dpred=Dp)
        if not quiet:
            print(f"L={L} rho={d['rho']} s={st['s']} {st['par']} lam={st['lam']:.8f} A+={ep['A']:.6f} A-={em['A']:.6f}"
                  f" Dfit-Dpred={ep['D']-Dp:+.4f}")
        for key, pt in st['pts'].items():
            q = num(key)
            right = any(abs(q - p) < 1e-9 for p in chain)
            p0 = q if right else -q
            gen, wt = [v for p, v in chain.items() if abs(p - p0) < 1e-9][0]
            Asrc = ep['A'] if right else em['A']
            rl, vl, rr, vr = map(np.array, (pt['rl'], pt['vl'], pt['rr'], pt['vr']))
            nmin = min(len(rl), len(rr))
            rl, vl, rr, vr = rl[:nmin], vl[:nmin], rr[:nmin], vr[:nmin]
            assert np.allclose(rl, rr, rtol=1e-12), 'asymmetric zone'
            ell = -np.log(rl)
            src, oth = (vl, vr) if right else (vr, vl)
            Jsrc = src - oth
            pw = gen + 0.5
            kap = Jsrc * ell ** pw / (wt * Asrc)
            lmax = min(ell.max(), ep['lmax'] + lcut) - lcut
            ck, rk = fit(ell, kap, lmin, lmax)
            # cusp without the (mesh-truncated) node value: vl + vr = 2c + W A ell^-pw (s0 + s1/ell + s2/ell^2)
            m = (ell >= lmin) & (ell <= lmax)
            X = np.stack([np.ones(m.sum())] + [wt * Asrc * ell[m] ** (-pw - k) for k in range(3)], 1)
            cs, *_ = np.linalg.lstsq(X, (vl + vr)[m], rcond=None)
            sig0 = cs[1]
            side0 = (ck[0] + sig0) / (sig0 - ck[0])
            cnode = (pt['c'] - cs[0] / 2) / (wt * Asrc * lmax ** -pw)
            row = dict(head, q=q, right=right, gen=gen, W=wt, kappa0=ck[0], kappa1=ck[1], sigma0=sig0, side0=side0,
                       node_bias=cnode, fit_res=rk, lwin=(lmin, lmax))
            if gen == 1:
                n = [m for m in c if abs((L - np.log(m)) - p0) < 1e-9][0]
                beta = W2(L, n) / c[n]
                edgev = np.interp(ell, ep['ell'][::-1], ep['v'][::-1]) if right else np.interp(ell, em['ell'][::-1], em['v'][::-1])
                # edge and kink zones share the offsets r_j: use exact nodal values
                e_r = np.array(st['edge+' if right else 'edge-']['r'])
                e_v = np.array(st['edge+' if right else 'edge-']['v'])
                idx = np.searchsorted(e_r, rl)
                okm = (idx < len(e_r))
                idx = np.minimum(idx, len(e_r) - 1)
                same = okm & np.isclose(e_r[idx], rl, rtol=1e-12)
                ev = np.where(same, e_v[idx], np.nan)
                inv = c[n] * ev / Jsrc - ell
                cb, rb = fit(ell[same], inv[same], lmin, lmax)
                row.update(n=n, beta=beta, b0=cb[0], b1=cb[1], K5pred=-Dp - beta, K5raw=cb[0] + Dp + beta,
                           K5cal=cb[0] + ep['D'] + beta if right else cb[0] + em['D'] + beta,
                           kappa1_pred=1.5 * Dp + beta)
                if not quiet:
                    print(f"   y={q:+.5f} n={n} gen1 {'R' if right else 'L'}: kappa0={ck[0]:.4f} (1)  sigma0={sig0:.4f} (1/3)"
                          f"  side0={side0:.4f} (-2)  b0={cb[0]:+.4f} pred={-Dp-beta:+.4f} dev={cb[0]+Dp+beta:+.4f}"
                          f" dev_cal={row['K5cal']:+.4f}  kappa1={ck[1]:.3f} (pred {1.5*Dp+beta:.3f})")
            else:
                if not quiet:
                    print(f"   y={q:+.5f} gen{gen} W={wt:.6f} {'R' if right else 'L'}: kappa0={ck[0]:.4f} (1)"
                          f"  sigma0={sig0:.4f} (1/{2*gen+1})  side0={side0:.4f} ({-(gen+1)/gen:.3f})  win={lmin:.0f}-{lmax:.0f}")
            rows.append(row)
    return rows


if __name__ == '__main__':
    a = sys.argv[1:]
    analyse(a[0], *(float(x) for x in a[1:]))
