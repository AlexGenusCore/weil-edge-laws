"""Check the anchor-snapping rule of p1weil.shift_overlap (|dA| < 1e-9 -> 0) on the registered meshes.
For every registered mesh, every prime-power shift tau = log n used in assembly, and every pair of mesh
anchors (a superset of the element pairs shift_overlap visits), classify |A_i - tau - A_j| < 1e-9 as
an exact identity (checked with rational labels) or an unrelated merge. Also checks make_mesh's 1e-12
anchor merge and reports the smallest non-identity distance (the safety gap)."""
import sys, os
from fractions import Fraction
import numpy as np
sys.path.insert(0, sys.argv[1])          # numerics/k5_L1 (p1weil.py, runlib.py identical to the registered copies)
import p1weil as W
import runlib as R


def label(p, L, xmode):
    """Exact label of an anchor: rational exp(2p) if e^{2L} is rational (xmode), else (sigma, q) with p = sigma*L - log q."""
    if xmode:
        x = np.exp(2 * p); q = Fraction(x).limit_denominator(10 ** 4)
        assert abs(float(q) - x) < 1e-12 * x, (p, x)
        return q
    hits = []
    for sg in (1, -1):
        x = np.exp(sg * L - p); q = Fraction(x).limit_denominator(1000)
        if abs(float(q) - x) < 1e-12 * x:
            hits.append((sg, q))
    assert len(hits) == 1, (p, L, hits)
    return hits[0]


def same(li, lj, n, xmode):
    if xmode:
        return li == n * n * lj
    return li[0] == lj[0] and n * li[1] == lj[1]


def check(name, L, an, xmode=False, H=None):
    mesh = W.make_mesh(L, an, H or L / 40)
    anc = np.array(sorted({float(a) for a in mesh['A']}))
    labs = [label(p, L, xmode) for p in anc]
    # make_mesh merge (1e-12): merged anchors carry distinct labels, and no raw label is lost
    rl = {str(label(float(a[0]), L, xmode)) for a in an}
    ml = [str(x) for x in labs]
    assert len(set(ml)) == len(ml), name + ': two anchors for one point'
    assert rl == set(ml), name + ': distinct anchors merged by make_mesh'
    n_id = n_bad = 0; gap = np.inf; rmax = 0.0
    for n, _ in W.prime_powers(np.exp(2 * L)):
        tau = np.log(n)
        if tau >= 2 * L:
            continue
        d = (anc[:, None] - tau) - anc[None, :]
        for i, j in zip(*np.nonzero(np.abs(d) < 1e-9)):
            if same(labs[i], labs[j], n, xmode):
                n_id += 1; rmax = max(rmax, abs(d[i, j]))
            else:
                n_bad += 1; print('  UNRELATED MERGE', name, n, anc[i], anc[j], d[i, j])
        nz = np.abs(d)[np.abs(d) >= 1e-9]
        idm = np.array([[same(labs[i], labs[j], n, xmode) for j in range(len(anc))] for i in range(len(anc))])
        assert not np.any(idm & (np.abs(d) >= 1e-9)), name + ': identity not snapped'
        gap = min(gap, nz.min() if nz.size else np.inf)
    print(f'{name:34s} anchors={len(anc):3d} snapped identities={n_id:4d} unrelated={n_bad} '
          f'min non-identity |dA|={gap:.2e} max snapped residual={rmax:.1e}')
    RMAX.append(rmax)
    return n_bad, gap


def kink_an(L, rmin, rho, spec, mirror, G2):
    cp = W.chain_points(L, gens=2); deep = []
    for tok in spec.split(','):
        if tok == 'all1':
            deep += [p for p, (g, w) in cp.items() if g == 1]
        elif tok.startswith('n'):
            deep.append(L - np.log(int(tok[1:])))
        elif tok.startswith('q'):
            a, b = tok[1:].split('/'); deep.append(L - np.log(int(a) / int(b)))
    deep = sorted(set(round(p, 12) for p in deep))
    an, _ = R.anchors(L, (rmin, rho), (1e-12, 1.5), G2, deep=[float(p) for p in deep], deep_par=(rmin, rho),
                      mirror_deep=mirror, edge_left=None if mirror else (1e-12, 1.5),
                      mirror_par=None if mirror else (1e-10, 1.6))
    return an


def k5_an(L, rho, rmin):
    cp = W.chain_points(L, gens=2)
    meas = sorted({round(p, 12) for p, (g, w) in cp.items() if g == 1} | {round(L - np.log(6.0), 12)})
    shifts = [np.log(m) for m, _ in W.prime_powers(np.exp(2 * L))]
    coupled = {round(q + sg * t, 12) for q in meas + [L] for t in shifts for sg in (-1, 1) if -L + 1e-9 < q + sg * t < L - 1e-9}
    graded = sorted(set(meas) | coupled)
    an, cp = R.anchors(L, (rmin, rho), (1e-12, 1.5), (1e-16, 1.6), deep=graded, deep_par=(rmin, rho),
                       mirror_deep=False, edge_left=(1e-12, 1.5), mirror_par=(1e-10, 1.6))
    known = {round(a[0], 12) for a in an}
    an += [(p, rmin, rho) for p in graded if p not in known]
    return an


bad = 0; gaps = []; RMAX = []
for r in (1.5, 1.25, 1.15):
    b, g = check(f'kink L=0.6 right rho={r}', 0.6, kink_an(0.6, 1e-40, r, 'n2,n3,q3/2', False, (1e-8, 2.0))); bad += b; gaps.append(g)
for r in (1.5, 1.25):
    b, g = check(f'kink L=0.6 mirror rho={r}', 0.6, kink_an(0.6, 1e-40, r, 'all1,q3/2', True, (1e-8, 2.0))); bad += b; gaps.append(g)
for r in (1.5, 1.25, 1.15):
    b, g = check(f'kink L=0.8 rho={r}', 0.8, kink_an(0.8, 1e-30, r, 'all1,q3/2,q4/3', False, (1e-16, 1.6))); bad += b; gaps.append(g)
for r in (1.5, 1.25):
    b, g = check(f'kink L=1.0 reg rho={r}', 1.0, kink_an(1.0, 1e-30, r, 'all1,q6/1', False, (1e-16, 1.6))); bad += b; gaps.append(g)
b, g = check('kink L=1.0 sens rho=1.25', 1.0, kink_an(1.0, 1e-30, 1.25, 'all1,q6/1', False, (1e-8, 2.0))); bad += b; gaps.append(g)
for r in (1.5, 1.25, 1.15):
    b, g = check(f'K5 rerun L=1.0 rho={r}', 1.0, k5_an(1.0, r, 1e-30)); bad += b; gaps.append(g)
for X in (8, 6, 10):
    for tag, a1, b1 in (('fine', (1e-9, 1.15), (1e-8, 1.5)), ('base', (1e-9, 1.25), (1e-7, 2.0))):
        L0 = np.log(X) / 2
        for k, Lx in enumerate((L0, L0 - 0.001, L0 - 0.002, L0 - 0.004)):
            an, _ = R.anchors(Lx, (1e-40, 1.25), a1, b1)
            b, g = check(f'tail X={X} {tag} L=L0-{(0, 1, 2, 4)[k]}d', Lx, an, xmode=(k == 0), H=Lx / (120 if tag == 'fine' else 60))
            bad += b; gaps.append(g)
print(f'TOTAL unrelated merges: {bad}; smallest non-identity |dA| over all meshes: {min(gaps):.3e}; largest snapped residual: {max(RMAX):.1e}')
assert bad == 0
