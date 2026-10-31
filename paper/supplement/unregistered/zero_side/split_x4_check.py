"""repair-tail-abelian: zero-side test of the main x main decomposition (proof.md, Prop E1).

Proved (proof.md Prop E1): the edge x edge part of the zero sum is
    pi T Z_MM(T) = 2A^2 [1 + (lambda + sigma c_X)/a(T)] + O(A^2/log^2 T),
c_X = Lambda(X)/sqrt X, X = e^{2L}, sigma = sign(A_+ A_-) (+1 even, -1 odd).
Unproved (Conjecture L): the edge x remainder cross terms are o(1/log T).
So at prime-power X the sector ratio Zinc/P0 should be ~ 1 + sigma c_X <1/a> if Conjecture L holds.

Cases: L = log 2 (X = 4, c_4 = 0.3466; prime-power), L = 0.4 (X = 2.2255, control, c_X = 0),
L = log(8)/2 (X = 8, c_8 = 0.2451).  s = 0 and s = 1, both sectors, P0 solver (final referee), h0 = L/1000.
lambda' by 2nd-order BACKWARD difference (d = 1e-3): at prime-power X the n = X shift activates just
to the right of L, and lambda' has only a log modulus there ([EH] N6), so central differences are biased.
Per block [T1,T2] (zeros 1..1500, all on the line, h = |F|^2):
  Zinc = 2 sum |F(t_rho)|^2 ;  Einc = (1/pi) int a|F|^2 (smooth density, no zeros)
  P0 = (|lam'|/pi) int a/(t^2(a-lam)) ;  P1 = (|lam'|/pi) int (a + sigma c_X)/(t^2(a-lam))
Derivative-free: ln(Zinc/Einc), whose even-odd difference should be ~ 2 c_X <1/a> (E has no Landau term).
Float64, uncertified.  Usage: python -I split_x4_check.py > split_x4_check.out
"""
import json
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
P0DIR = os.path.join(HERE, "..", "p0")  # supplement: P0 code
for p in (HERE, P0DIR):
    if os.path.exists(p + "/p0_edge.py"):
        sys.path.insert(0, p)
        break
from p0_edge import assemble, eig, xcoords  # noqa: E402

ZF = HERE + "/zeros.json"  # supplement: the 1500 zeros
z = json.load(open(ZF))
gam = np.array([float(z[str(i)]) for i in range(1, len(z) + 1)])


def a_sym(t):
    w = 0.25 + 0.5j * t
    return (np.log(w) - 1 / (2 * w) - 1 / (12 * w ** 2) + 1 / (120 * w ** 4)).real - np.log(np.pi)


def Ft(t, f, a, b, chunk=2000):
    out = np.empty(len(t), complex)
    for i in range(0, len(t), chunk):
        tt = t[i:i + chunk]
        out[i:i + chunk] = ((np.exp(1j * np.outer(tt, b)) - np.exp(1j * np.outer(tt, a))) @ f) / (1j * tt)
    return out


def trap(y, x):
    return float(np.sum((y[1:] + y[:-1]) * np.diff(x)) / 2)


def ground_pair(L, s):
    Q, h, side, R1, R2 = assemble(L, model='weil', s=s, h0=L / 1000, rho=1.5, rmin=1e-40)
    ab = xcoords(L, side, R1, R2)
    return {par: eig(Q, h, k=1, parity=par)[0][:2] for par in ('e', 'o')}, ab


def vonmangoldt(n):
    for p in range(2, n + 1):
        if n % p == 0:
            m = n
            while m % p == 0:
                m //= p
            return np.log(p) if m == 1 else 0.0
    return 0.0


blocks = [(100, 200), (200, 400), (400, 800), (800, 1600), (100, 1980)]
cases = [(np.log(2.0), 4), (0.4, None), (np.log(8.0) / 2, 8)]
d = 1e-3
for L, Xint in cases:
    X = np.exp(2 * L)
    cX = vonmangoldt(Xint) / np.sqrt(Xint) if Xint else 0.0
    # Landau check: E_X(T) = Re sum_{t<=T} X^{i t} + c_X T/(2 pi) should be O(log T)
    ph = np.cumsum(np.cos(gam * np.log(X)))
    print(f"\n=== L={L:.6f}  X=e^(2L)={X:.6f}  c_X={cX:.4f}")
    print("  Landau remainder Re sum_{t_rho<=T} X^{it} + c_X T/2pi at T=200,500,1000,1980: "
          + " ".join(f"{ph[np.searchsorted(gam, T) - 1] + cX * T / (2 * np.pi):+.2f}" for T in (200, 500, 1000, 1980)))
    for s in (0.0, 1.0):
        g0, (a, b) = ground_pair(L, s)
        g1, _ = ground_pair(L - d, s)
        g2, _ = ground_pair(L - 2 * d, s)
        stats = {}
        for par in ('e', 'o'):
            lam, f = g0[par]
            lp = (3 * lam - 4 * g1[par][0] + g2[par][0]) / (2 * d)
            sig = 1 if par == 'e' else -1
            D = abs(lp)
            Fz = Ft(gam, f, a, b)
            print(f" s={s:.0f} {par}: lambda={lam:+.6e}  lambda'(backward)={lp:+.6e}")
            print("   [T1,T2]      Zinc/P0   Zinc/P1   Einc/P0   Zinc/Einc  | 1+sig*cX<1/a>  -sum_{n<X}c_n^2<1/a^2>")
            rows = []
            for T1, T2 in blocks:
                sel = (gam > T1) & (gam <= T2)
                Zinc = 2 * np.sum(np.abs(Fz[sel]) ** 2)
                t = np.linspace(T1, T2, int(40 * (T2 - T1)) + 1)
                F = Ft(t, f, a, b)
                at = a_sym(t)
                P0 = D / np.pi * trap(at / (t ** 2 * (at - lam)), t)
                P1 = D / np.pi * trap((at + sig * cX) / (t ** 2 * (at - lam)), t)
                Einc = trap(at * np.abs(F) ** 2, t) / np.pi
                w = 1 / t ** 2
                inv_a = trap(w / at, t) / trap(w, t)
                inv_a2 = trap(w / at ** 2, t) / trap(w, t)
                cn2 = sum(vonmangoldt(n) ** 2 / n for n in range(2, int(X) + 1) if np.log(n) < 2 * L - 1e-12)
                rows.append((Zinc, Einc, P0, inv_a))
                print(f"   [{T1},{T2}]  {Zinc/P0:.4f}    {Zinc/P1:.4f}    {Einc/P0:.4f}    {Zinc/Einc:.4f}     | "
                      f"{1+sig*cX*inv_a:.4f}         {-cn2*inv_a2:+.4f}")
            stats[par] = rows
            sys.stdout.flush()
        print(f"  s={s:.0f} sector split (pred. 2 c_X <1/a> under Conjecture L, plus O(1/log^2) kink terms):")
        print("   [T1,T2]      ln(Ze/Zo)-ln(P0e/P0o)   ln(Ze/Ee)-ln(Zo/Eo) [derivative-free]   2cX<1/a>")
        for k, (T1, T2) in enumerate(blocks):
            Ze, Ee, Pe, ia = stats['e'][k]
            Zo, Eo, Po, _ = stats['o'][k]
            print(f"   [{T1},{T2}]   {np.log(Ze/Zo)-np.log(Pe/Po):+.4f}                 {np.log(Ze/Ee)-np.log(Zo/Eo):+.4f}"
                  f"                                 {2*cX*ia:+.4f}")
        sys.stdout.flush()
