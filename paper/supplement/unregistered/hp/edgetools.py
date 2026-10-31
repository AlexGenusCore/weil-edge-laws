"""Shared helpers for the hp-FEM (boundary-clue/hpfem.py) eigenvectors in parity bases:
edge-coefficient fit A and the exact distributional pairing <u_o, u_e'> of the discrete functions."""
import sys
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # supplement: hpfem.py is in this folder
import numpy as np, mpmath as mp
from hpfem import legn


class Edge:
    def __init__(self, M, dmin):
        p, ne = M.el['p'], M.el['ne']; h = ne // 2
        self.p, self.dmin = p, dmin
        self.r = np.array(M.el['r'][h:])
        self.dc = np.array([float(mp.mpf(M.L) - M.el['m'][i]) for i in range(h, ne)])
        self.ts = np.linspace(-1, 1, 17); self.P = legn(p, self.ts)
        xg, wg = np.polynomial.legendre.leggauss(p + 4)
        Pg, dPg = legn(p, xg), np.zeros((p + 1, len(xg)))
        for q in range(p + 1):
            cq = np.zeros(q + 1); cq[q] = 1
            dPg[q] = np.polynomial.legendre.legval(xg, np.polynomial.legendre.legder(cq)) * np.sqrt((2 * q + 1) / 2)
        self.Dm = (Pg * wg) @ dPg.T                      # int Pbar_a Pbar_b'
        self.Pl, self.Pr = legn(p, [-1.0])[:, 0], legn(p, [1.0])[:, 0]

    def coef(self, v):  # right-half cell coefficients of the full-line L^2-normalised function
        return v.reshape(-1, self.p + 1) / np.sqrt(2)

    def A(self, v, dmax=1e-4, nt=3):
        """fit psi(L-d) = sum_j c_j l^(-1/2-j), j < nt, on 10 dmin < d < dmax; returns (A, max residual)"""
        ps = (self.coef(v) @ self.P) / np.sqrt(self.r)[:, None]
        d = (self.dc[:, None] - self.r[:, None] * self.ts[None, :]).ravel(); y = ps.ravel()
        m = (d > 10 * self.dmin) & (d < dmax); d, y = d[m], y[m]; l = np.log(1 / d)
        X = np.stack([l ** (-.5 - j) for j in range(nt)], 1)
        c, *_ = np.linalg.lstsq(X, y, rcond=None)
        return c[0], np.abs(X @ c - y).max()

    def pair_deriv(self, vo, ve):
        """<u_o, u_e'> on R (odd u_o, even u_e): within-cell part + jumps of u_e paired with the average of u_o,
        including the jump to 0 at x = L.  u_e is even, so it has no jump at x = 0."""
        Co, Ce, r = self.coef(vo), self.coef(ve), self.r
        tot = sum(Co[k] @ self.Dm @ Ce[k] / r[k] for k in range(len(r)))
        for k in range(len(r) - 1):
            ue_l, ue_r = Ce[k] @ self.Pr / np.sqrt(r[k]), Ce[k + 1] @ self.Pl / np.sqrt(r[k + 1])
            uo_l, uo_r = Co[k] @ self.Pr / np.sqrt(r[k]), Co[k + 1] @ self.Pl / np.sqrt(r[k + 1])
            tot += (ue_r - ue_l) * (uo_l + uo_r) / 2
        tot += -(Ce[-1] @ self.Pr / np.sqrt(r[-1])) * (Co[-1] @ self.Pr / np.sqrt(r[-1])) / 2
        return 2 * tot
