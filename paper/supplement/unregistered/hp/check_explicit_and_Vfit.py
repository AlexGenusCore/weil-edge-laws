"""Referee-2 checks that use the exact renewal function V (renewal_V.py, validated against 1/kappa to ~1e-6).

(T1) Explicit formula (6.1) / Silverstein normalisation k = 1, flux identity and Lemma 10.2, on the torsion function
     u = G_D 1 of the ARCHIMEDEAN part only (hpfem with primes off, s = 0, constant c_0 removed):
         A_pred = V(2L) - int_0^inf V'(2L + eta) Nu(L + eta) d eta     vs     A_fit = lim u / V  (fit in V, V^2, V^3).
(T2) (H) with A fitted in powers of the exact V instead of l^{-1/2}:  ratio lambda'/(-2A^2), lambda' = referee-1
     Richardson values.  Usage: check_explicit_and_Vfit.py L"""
import re
import sys
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # supplement: hpfem.py, renewal_V.py are in this folder
import numpy as np
import mpmath as mp
import hpfem
from renewal_V import Renewal

L0 = float(sys.argv[1])
KW = dict(p=8, sig=0.25, dmin=1e-14, H=0.05)
C0 = float(mp.digamma(0.25) - mp.log(mp.pi))
RN = Renewal()
nu = lambda u: np.exp(-u / 2) / (-np.expm1(-2 * u))
kap0 = lambda d: 0.5 * np.log((1 + np.exp(-d / 2)) / -np.expm1(-d / 2)) + np.arctan(np.exp(-d / 2))  # int_d^inf nu = artanh(e^{-d/2}) + arctan(e^{-d/2})
xg, wg = np.polynomial.legendre.leggauss(24)


def cells(M, Cfull):
    el = M.el
    r = np.array(el["r"]); dm = np.array([float(mp.mpf(M.L) - mm) for mm in el["m"]])
    return dict(C=Cfull.reshape(el["ne"], el["p"] + 1), r=r, dm=dm, lo=dm - r, p=el["p"])


def N_out(c, eta):  # (N u)(L + eta) = int_0^{2L} nu(eta + d) u(L - d) dd
    out = 0.0
    for i in range(len(c["r"])):
        lo, h = c["lo"][i], 2 * c["r"][i]
        s, ws = hpfem.graded_nodes(h, sig=0.5, K=60, n=8) if eta + lo < 4 * h else (h * (xg + 1) / 2, wg * h / 2)
        d = lo + s
        out += np.sum(ws * nu(eta + d) * (c["C"][i] @ hpfem.legn(c["p"], (c["dm"][i] - d) / c["r"][i])) / np.sqrt(c["r"][i]))
    return out


def int_cells(c, fun_of_d):  # int_D u(x) F(L - x) dx
    tot = 0.0
    for i in range(len(c["r"])):
        lo, h = c["lo"][i], 2 * c["r"][i]
        s, ws = hpfem.graded_nodes(h, sig=0.5, K=60, n=8) if lo < 4 * h else (h * (xg + 1) / 2, wg * h / 2)
        d = lo + s
        tot += np.sum(ws * fun_of_d(d) * (c["C"][i] @ hpfem.legn(c["p"], (c["dm"][i] - d) / c["r"][i])) / np.sqrt(c["r"][i]))
    return tot


def fitV(M, vec, powers):
    d, y = M.evalright(vec, ts=np.linspace(-1, 1, 17))
    d, y = d.ravel(), y.ravel()
    m = (d > 1e-13) & (d < 1e-4); d, y = d[m], y[m]
    Vd = RN.V(d)
    X = np.c_[[Vd ** q for q in powers]].T
    c, *_ = np.linalg.lstsq(X, y, rcond=None)
    return c[0], np.sqrt(np.mean((X @ c - y) ** 2)) / np.abs(y).max()


# ---------------- (T1) torsion function of the archimedean part ----------------
saved = hpfem.primes_list, hpfem.anchors
hpfem.primes_list = lambda L: []
hpfem.anchors = lambda L: [-mp.mpf(L), mp.mpf(L)]
M0 = hpfem.Model(L0, **KW)
hpfem.primes_list, hpfem.anchors = saved
el = M0.el
load = np.zeros(M0.N); load[::el["p"] + 1] = np.sqrt(2 * np.array(el["r"]))
x = np.linalg.solve(M0.Ae - C0 * np.eye(M0.Ae.shape[0]), M0.E.T @ load)
c = cells(M0, M0.E @ x)
eta, weta = hpfem.graded_nodes(1.0, sig=0.5, K=60, n=8)
e2 = 1 + 59 * (xg + 1) / 2; w2 = wg * 59 / 2
eta = np.r_[eta, e2]; weta = np.r_[weta, w2]
Nv = np.array([N_out(c, e) for e in eta])
A_pred = RN.V(2 * L0)[0] - np.sum(weta * RN.Vp(2 * L0 + eta) * Nv)
flux = 2 * int_cells(c, lambda d: kap0(np.maximum(d, 1e-300)))  # u even: int u kappa_D = 2 int u(x) kappa_0(L - x)
print(f"(T1) L={L0}: torsion u = G_D 1 (archimedean part).  flux int u kappa_D = {flux:.8f}  vs  int h = 2L = {2*L0:.8f}")
print(f"     explicit (6.1): A_pred = V(2L) - int V' N u = {RN.V(2*L0)[0]:.8f} - {RN.V(2*L0)[0]-A_pred:.8f} = {A_pred:.8f}"
      f"   Lemma 10.2 lower bound V'(2L) L = {RN.Vp(2*L0)[0]*L0:.8f}")
for pw in ((1, 2), (1, 2, 3), (1, 3), (1, 3, 5)):
    A, rms = fitV(M0, x, pw)
    print(f"     fit u = sum c_q V^q, q in {pw}: A_fit = {A:.8f}  (rms {rms:.1e})   A_fit/A_pred = {A/A_pred:.6f}")

# ---------------- (T2) (H) with V-basis fits, true Weil model (primes on) ----------------
M = hpfem.Model(L0, **KW)
REF = os.path.dirname(os.path.abspath(__file__)) + "/"  # supplement: ref_hadamard_central_L0.4.out is in this folder
pat = re.compile(r"L=(\S+) p=8 sector=(\w) s=(\S+): .*?A_fit3=(\S+) .*?ratio lam'/\(-2A\^2\)=(\S+)")
lamp = {}
for line in open(REF + f"ref_hadamard_central_L{L0}.out"):
    g = pat.search(line)
    if g:
        lamp[(g.group(2), float(g.group(3)))] = float(g.group(5)) * (-2 * float(g.group(4)) ** 2)
for sec in ("e", "o"):
    for s in (0.0, 1.0):
        lam, v = (M.even(s) if sec == "e" else M.odd(s))
        row = []
        for pw in ((1,), (1, 2), (1, 3), (1, 2, 3), (1, 3, 5)):
            A, rms = fitV(M, v[:, 0], pw)
            row.append(f"V^{pw}: ratio {lamp[(sec, s)] / (-2 * A * A):.5f} (rms {rms:.0e})")
        print(f"(T2) L={L0} {sec} s={s}: lam'={lamp[(sec, s)]:+.6e} | " + " | ".join(row), flush=True)
        d, y = M.evalright(v[:, 0], ts=np.linspace(-1, 1, 17)); d, y = d.ravel(), y.ravel()
        if np.median(y[(d > 1e-13) & (d < 1e-4)]) < 0: y = -y
        dd = np.array([1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-13]); yy = np.array([y[np.argmin(np.abs(np.log(d / q)))] for q in dd])
        print("      psi/V at d=1e-4..1e-13: " + " ".join(f"{q:.5f}" for q in yy / RN.V(dd)) +
              "   psi*l^1/2: " + " ".join(f"{q:.5f}" for q in yy * np.sqrt(np.log(1 / dd))), flush=True)
