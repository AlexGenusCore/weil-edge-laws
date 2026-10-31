"""Helpers on top of p1weil: anchor sets, solves, edge fits, local profiles."""
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import p1weil as W

EG = W.EG
DSHIFT = np.log(2 * np.pi) + EG          # D = lam + log(2 pi) + gamma


def anchors(L, edge, gen1, gen2=None, deep=(), deep_par=None, mirror_deep=True, edge_left=None, mirror_par=None):
    """edge/gen1/gen2/deep_par = (rmin, rho).  deep: right-side points p; their mirrors -p are deep
    too if mirror_deep, else they get the gen1/gen2 parameters.  edge_left: parameters of the left
    edge (default = edge).  Returns anchor list for make_mesh and the chain table {p: (gen, weight)}."""
    cp = W.chain_points(L, gens=2)
    an = [(-L,) + tuple(edge_left or edge), (L,) + tuple(edge)]
    deepset = [round(p, 10) for p in deep]
    for p, (g, w) in cp.items():
        par = gen1 if g == 1 else gen2
        mpar = par
        if round(p, 10) in deepset:
            par = deep_par
            if mirror_deep:
                mpar = deep_par
        if not mirror_deep and mirror_par is not None:
            mpar = mirror_par
        if par is not None:
            an.append((p,) + tuple(par))
        if mpar is not None:
            an.append((-p,) + tuple(mpar))
    return an, cp


def solve(L, an, H, svals=(0.0,), k=6, frozen=None, drop=()):
    t = time.time()
    mesh = W.make_mesh(L, an, H, frozen=frozen)
    asm = W.assemble(mesh, drop=drop)
    out = {}
    for s in svals:
        out[s] = W.eig(asm, s=s, k=k)
    return mesh, asm, out, time.time() - t


def side_profile(asm, f, p, side):
    """Nodal values at anchor p: side=-1 -> nodes p - r (offsets < 0), +1 -> p + r.  Returns r, values."""
    A, o, fv = W.full_nodes(asm, f)
    sel = (np.abs(A - p) < 1e-12) & (np.sign(o) == side)
    r = np.abs(o[sel])
    order = np.argsort(r)
    return r[order], fv[sel][order]


def node_value(asm, f, p):
    A, o, fv = W.full_nodes(asm, f)
    sel = (np.abs(A - p) < 1e-12) & (o == 0)
    assert sel.sum() == 1, (p, sel.sum())
    return fv[sel][0]


def edge_fit(asm, f, L, sign=+1, lmin=15.0, lcut=6.0):
    """psi(sign*(L - r)) on the deep edge zone; fit psi^-2 = a0 ell + a1 + a2/ell + a3/ell^2 on
    ell in [lmin, ell_max - lcut].  Returns A (signed), D = -a1/a0, rms, and the profile."""
    r, y = side_profile(asm, f, sign * L, -sign)
    ell = -np.log(r)
    m = (ell >= lmin) & (ell <= ell.max() - lcut)
    X = np.stack([ell[m], np.ones(m.sum()), 1 / ell[m], 1 / ell[m] ** 2], 1)
    co, *_ = np.linalg.lstsq(X, y[m] ** -2.0, rcond=None)
    rms = np.sqrt(np.mean((X @ co - y[m] ** -2.0) ** 2)) / np.mean(y[m] ** -2.0)
    A = np.sign(y[m][-1]) * co[0] ** -0.5
    return dict(A=A, D=-co[1] / co[0], rms=rms, co=co, ell=ell, y=y)


def pick(states, par, idx=0):
    sel = [e for e in states if e['par'] == par]
    return sel[idx] if len(sel) > idx else None
