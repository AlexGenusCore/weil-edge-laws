"""Referee check (not in the attempt): (H) lam'(L) = -2A^2 for the first TWO eigenvalues of each sector of Q_L
(attempt only tested ground states), incl. an L just above the activation of p=2 (2L - log 2 = 0.027).
Reuses boundary-clue/hpfem.py and the attempt's edgetools.Edge (A fit).  Usage: ref_excited_hadamard.py L h"""
import sys
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # supplement: edgetools.py and hpfem.py are in this folder
import numpy as np
from edgetools import Edge
import hpfem

L0, hh = float(sys.argv[1]), float(sys.argv[2])
K, S = 2, (0.0, 1.0)
lam = {}
for j in (-2, -1, 1, 2, 0):
    M = hpfem.Model(L0 + j * hh, p=8, sig=0.25, dmin=1e-14, H=0.05)
    for s in S:
        lam[j, s] = (M.even(s, K)[0], M.odd(s, K)[0])
E = Edge(M, 1e-14)
print(f"Q_L L={L0} h={hh} N={M.N} primes={[float(a) for a, c in hpfem.primes_list(L0)]}")
for s in S:
    for sec, f in ((0, M.even), (1, M.odd)):
        w, V = f(s, K)
        for k in range(K):
            d = (-lam[2, s][sec][k] + 8 * lam[1, s][sec][k] - 8 * lam[-1, s][sec][k] + lam[-2, s][sec][k]) / (12 * hh)
            a4, _ = E.A(V[:, k], 1e-6, 4)
            print(f" s={s} {'eo'[sec]} k={k}: lam={w[k]: .9g} lam'={d: .6g}  -lam'/(2A^2)={-d / (2 * a4 * a4):.5f}")
