"""referee2-tail-abelian: mesh stability of the X=4 (L=log 2), s=0 zero-side numbers of repair proof.md §9.4,
and the size of Z_x for the paper's own (q=1) split.
For h0 = L/1000 (repair's mesh) and L/2000: even and odd ground states, per dyadic block
  Zinc/P1 (even, |lambda'| by 2nd-order backward differences, mesh rescaled with L as in the repair),
  Zinc/Einc for both sectors, derivative-free split ln(Ze/Ee)-ln(Zo/Eo) vs 2 c_4 <1/a>,
  Zinc/ZMM_q1 with ZMM_q1 >= P0<1+delta_U> + (P1-P0)<cos2theta>(1+delta_U) ~ P1 + P0<delta_U> (lower bound, Re part only).
Odd state: lambda, edge-fit 2A^2 and shell <t^2(a-lam)|F|^2>[800,1600] (mesh sensitivity).
Float64, uncertified.  Usage ([VM]): python -I mesh_x4_check.py > mesh_x4_check.out
"""
import json, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "p0"))  # supplement: P0 code
from p0_edge import assemble, eig, xcoords, edge_fit  # noqa: E402
import mpmath as mp  # noqa: E402

z = json.load(open(os.path.join(HERE, "zeros.json")))
gam = np.array([float(z[str(i)]) for i in range(1, len(z) + 1)])
C = float(mp.digamma(0.25) - mp.log(mp.pi))


def a_sym(t):
    w = 0.25 + 0.5j * t
    return (np.log(w) - 1 / (2 * w) - 1 / (12 * w ** 2) + 1 / (120 * w ** 4)).real - np.log(np.pi)


def Ft(t, f, a, b, chunk=1000):
    out = np.empty(len(t), complex)
    for i in range(0, len(t), chunk):
        tt = t[i:i + chunk]
        out[i:i + chunk] = ((np.exp(1j * np.outer(tt, b)) - np.exp(1j * np.outer(tt, a))) @ f) / (1j * tt)
    return out


def trap(y, x):
    return float(np.sum((y[1:] + y[:-1]) * np.diff(x)) / 2)


L, c4, d = np.log(2.0), np.log(2.0) / 2, 1e-3
blocks = [(100, 200), (200, 400), (400, 800), (800, 1600)]
for div in (1000, 2000):
    sol = {}
    for Lx in (L, L - d, L - 2 * d):
        Q, h, side, R1, R2 = assemble(Lx, model='weil', s=0.0, h0=Lx / div, rho=1.5, rmin=1e-40)
        if Lx == L:
            ab = xcoords(L, side, R1, R2); geo = (side, R1, R2)
            sol[Lx] = {p: eig(Q, h, k=1, parity=p)[0][:2] for p in ('e', 'o')}
        else:
            sol[Lx] = {'e': eig(Q, h, k=1, parity='e')[0][:2]}
        del Q
    a, b = ab
    lam_e, fe = sol[L]['e']; lam_o, fo = sol[L]['o']
    lp = (3 * lam_e - 4 * sol[L - d]['e'][0] + sol[L - 2 * d]['e'][0]) / (2 * d)
    print(f"\n=== h0=L/{div} N={len(geo[1])}  lambda_e={lam_e:+.6e} lambda_e'(bwd)={lp:+.5e}  lambda_o={lam_o:+.6e}")
    for par, f, lam in (('e', fe, lam_e), ('o', fo, lam_o)):
        coef, resid, _, _ = edge_fit(f, *geo)
        t = np.linspace(800, 1600, 32001); at = a_sym(t)
        shell = np.mean(t ** 2 * (at - lam) * np.abs(Ft(t, f, a, b)) ** 2)
        print(f"  {par}: 2A_fit^2={2*coef[0]**2:.4e} (resid {resid:.1e})  shell[800,1600]={shell:.4e}")
    Fz = {'e': Ft(gam, fe, a, b), 'o': Ft(gam, fo, a, b)}
    print("   block       Ze/P1   Ze/ZMMq1>=  Ze/Ee   Zo/Eo   split  2c4<1/a>  <delta_U,q=1>")
    for T1, T2 in blocks:
        sel = (gam > T1) & (gam <= T2)
        t = np.linspace(T1, T2, int(40 * (T2 - T1)) + 1); at = a_sym(t)
        r = {}
        for par, f, lam in (('e', fe, lam_e), ('o', fo, lam_o)):
            Zi = 2 * np.sum(np.abs(Fz[par][sel]) ** 2)
            Ei = trap(at * np.abs(Ft(t, f, a, b)) ** 2, t) / np.pi
            r[par] = (Zi, Ei)
        mu = 1 + lam_e - C
        sq = 1 + at - C
        dU = mu ** 2 / (4 * sq * (at - lam_e))
        P0 = abs(lp) / np.pi * trap(at / (t ** 2 * (at - lam_e)), t)
        P1 = abs(lp) / np.pi * trap((at + c4) / (t ** 2 * (at - lam_e)), t)
        P0d = abs(lp) / np.pi * trap(at * dU / (t ** 2 * (at - lam_e)), t)
        ia = trap(1 / (t ** 2 * at), t) / trap(1 / t ** 2, t)
        Ze, Ee = r['e']; Zo, Eo = r['o']
        print(f"   [{T1},{T2}]  {Ze/P1:.4f}  {Ze/(P1+P0d):.4f}     {Ze/Ee:.4f}  {Zo/Eo:.4f}  {np.log(Ze/Ee)-np.log(Zo/Eo):+.4f}  "
              f"{2*c4*ia:+.4f}   {P0d/P0:.4f}")
    sys.stdout.flush()
