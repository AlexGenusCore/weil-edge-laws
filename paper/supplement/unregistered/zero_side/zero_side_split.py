"""Referee 1 (tail-explicit): direct zero-side test of Cor C3 and of the per-sector term (Prop E.4 / Pred F)
on the first 1500 zeta zeros (t <= 1981, all on the line), at prime-power X = e^{2L} = 2 and 3.

The attempt's own checks of Prop E are position-side only (Z_cos evaluated through Theorem A).  Here the
eigenfunction is solved independently (final referee's P0 code, imported unchanged, h0 = L/1000, rho = 1.5,
rmin = 1e-40), its transform is evaluated at the actual zeros, and dyadic block sums
    Zinc(T1,T2) = 2 sum_{T1 < gamma <= T2} |F(gamma)|^2
are compared with
    P_F    : Z(T) = (2A^2/(pi T)) tau(T),  tau = 1 + (lam + eps c_X)/(log(T/2pi) + 1 - lam)   (Pred. F)
    P_noX  : same with c_X = 0  (lambda term only)
    P_lead : (2A^2/pi)(1/T1 - 1/T2)                                                      (Cor C3 leading)
A is the edge-fit trace; lambda'_left (one-sided 2nd-order difference) is printed as a check of -2A^2.
Usage: OMP_NUM_THREADS=2 python -I zero_side_split.py > zero_side_split.out   (laptop, a few min, < 1 GB)
"""
import json
import sys
import numpy as np

import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "p0"))  # supplement: P0 code
from p0_edge import assemble, eig, xcoords, edge_fit  # noqa: E402

ZF = os.path.join(os.path.dirname(os.path.abspath(__file__)), "zeros.json")  # supplement: the 1500 zeros
zz = json.load(open(ZF))
gam = np.array([float(zz[str(i)]) for i in range(1, len(zz) + 1)])


def solve(L, s, h0):
    Q, h, side, R1, R2 = assemble(L, model='weil', s=s, h0=h0, rho=1.5, rmin=1e-40)
    out = {}
    for lam, f, par in eig(Q, h, k=6):
        out.setdefault(par, (lam, f))
    return out, (side, R1, R2)


def Ft(t, f, a, b, chunk=500):
    out = np.empty(len(t), complex)
    for i in range(0, len(t), chunk):
        tt = t[i:i + chunk]
        out[i:i + chunk] = ((np.exp(1j * np.outer(tt, b)) - np.exp(1j * np.outer(tt, a))) @ f) / (1j * tt)
    return out


def tau(T, lam, ecX):
    return 1 + (lam + ecX) / (np.log(T / (2 * np.pi)) + 1 - lam)


blocks = [(125, 250), (250, 500), (500, 1000), (1000, 1981), (250, 1981)]
cases = [(0.5 * np.log(2), 1.0, np.log(2) / np.sqrt(2)), (0.5 * np.log(2), 0.0, np.log(2) / np.sqrt(2)),
         (0.5 * np.log(3), 0.0, np.log(3) / np.sqrt(3)), (0.4, 0.0, 0.0)]
for L, s, cX in cases:
    h0 = L / 1000
    sol, (side, R1, R2) = solve(L, s, h0)
    d = 1e-3
    s1, _ = solve(L - d, s, h0)
    s2, _ = solve(L - 2 * d, s, h0)
    a, b = xcoords(L, side, R1, R2)
    print(f"\nL={L:.6f} X={np.exp(2*L):.4f} s={s} c_X={cX:.5f}")
    for par in ('e', 'o'):
        lam, f = sol[par]
        coef, resid, *_ = edge_fit(f, side, R1, R2, lmin=8.0, nterm=4)
        A = abs(coef[0])
        lpl = (3 * lam - 4 * s1[par][0] + s2[par][0]) / (2 * d)
        eps = 1 if par == 'e' else -1
        print(f" [{par}] lam={lam:+.6e} A={A:.6f} (fit resid {resid:.1e})  -lam'_left/(2A^2)={-lpl/(2*A*A):.4f}")
        print("   [T1,T2]      Zinc/P_F  Zinc/P_noX  Zinc/P_lead   pred tau_F  pred tau_noX")
        Fz = Ft(gam, f, a, b)
        for T1, T2 in blocks:
            sel = (gam > T1) & (gam <= T2)
            Zinc = 2 * np.sum(np.abs(Fz[sel]) ** 2)
            K = 2 * A * A / np.pi
            PF = K * (tau(T1, lam, eps * cX) / T1 - tau(T2, lam, eps * cX) / T2)
            PN = K * (tau(T1, lam, 0) / T1 - tau(T2, lam, 0) / T2)
            PL = K * (1 / T1 - 1 / T2)
            Tm = np.sqrt(T1 * T2)
            print(f"   [{T1},{T2}]  {Zinc/PF:8.4f}  {Zinc/PN:9.4f}  {Zinc/PL:10.4f}   {tau(Tm,lam,eps*cX):9.4f}  {tau(Tm,lam,0):9.4f}")
        sys.stdout.flush()
