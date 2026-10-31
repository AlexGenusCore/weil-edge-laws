"""Renewal function V of the ladder-height process of X (Phi(xi) = Re psi(1/4 + i xi/2) - psi(1/4)), computed
from the KMR Prop 4.5 spectral representation, made explicit for our f:

    V'(x) = b0 + sum_k w_k exp(-xi_k x),   V(x) = b0 x + sum_k w_k (1 - exp(-xi_k x)) / xi_k,

with b0 = f'(0)^{-1/2}, xi_k in (a_k, a_{k+1}) (a_k = 2k + 1/2) the zeros of F(xi) := f(-xi^2), and
w_k = kappa(xi_k) / (-F'(xi_k)).  (Im(-1/f(-xi^2 + i0)) is a sum of point masses at the zeros of f on (-inf, 0).)
kappa(s) = exp((1/pi) int_0^{pi/2} log Phi(s tan th) dth)  (BGR (2.14), GR 2012 normalisation kappa(q,0) = sqrt q).
Sum exact for k < K, Euler-Maclaurin integral with the asymptotic weight beyond.  numpy only, float64.
Self-check (run as script): Laplace transform b0/s + sum w_k/(s+xi_k) against 1/kappa(s), and V(a) l(a)^{1/2} -> 1."""
import numpy as np
import mpmath as mp

B2K = np.array([1 / 6, -1 / 30, 1 / 42, -1 / 30, 5 / 66, -691 / 2730, 7 / 6])


def digamma(z):
    z = np.asarray(z, complex)
    s = np.zeros_like(z)
    for j in range(12):
        s -= 1 / (z + j)
    w = z + 12
    out = np.log(w) - 1 / (2 * w)
    for k, b in enumerate(B2K, 1):
        out -= b / (2 * k * w ** (2 * k))
    return out + s


PSI14 = float(mp.digamma(0.25))
CINF = -np.log(2) - PSI14
ZET = np.array([float(mp.zeta(2 * j + 1, 0.25)) for j in range(1, 26)])
FP0 = ZET[0] / 4
B0 = FP0 ** -0.5


def logPhi(logxi):
    """log Phi(xi) given log xi (any size)."""
    logxi = np.atleast_1d(np.asarray(logxi, float))
    out = np.empty_like(logxi)
    sm, lg = logxi < np.log(0.2), logxi > np.log(1e8)
    md = ~(sm | lg)
    lam4 = np.exp(2 * logxi[sm]) / 4                      # lambda/4, lambda = xi^2
    j = np.arange(1, 26)
    ser = np.sum((-1.0) ** (j - 1) * ZET * lam4[:, None] ** j, axis=1)  # f(lambda) = sum (-1)^{j-1}(lambda/4)^j zeta(2j+1,1/4)
    out[sm] = np.log(ser)
    xi = np.exp(logxi[md])
    out[md] = np.log(digamma(0.25 + 0.5j * xi).real - PSI14)
    out[lg] = np.log(logxi[lg] + CINF)
    return out


# tanh-sinh nodes on (0, pi/2): theta and its complement computed without cancellation
_t = np.arange(-4.5, 4.5 + 1e-12, 1 / 64)
_e = np.exp(np.pi * np.sinh(_t))
TH = (np.pi / 2) * _e / (1 + _e)
THc = (np.pi / 2) / (1 + _e)
WT = (np.pi ** 2 / 2) * np.cosh(_t) * _e / (1 + _e) ** 2 / 64
LOGTAN = np.log(np.sin(TH)) - np.log(np.sin(THc))


def logkappa(logs):
    logs = np.atleast_1d(np.asarray(logs, float))
    return np.array([np.sum(WT * logPhi(ls + LOGTAN)) / np.pi for ls in logs])


def Lt(xi):  # Lambda~(xi) = (psi(3/4+xi/2) + psi(1/4+xi/2))/2 - psi(1/4)
    return (digamma(0.75 + xi / 2).real + digamma(0.25 + xi / 2).real) / 2 - PSI14


def zeros(K):
    """xi_k, w_k for k = 0..K-1; F(a_k + d) = Lt(a_k + d) + (pi/2) cot(pi d/2), d in (0, 2)."""
    a = 2 * np.arange(K) + 0.5
    lo, hi = np.full(K, 1e-15), np.full(K, 2 - 1e-15)
    for _ in range(80):
        mid = (lo + hi) / 2
        val = Lt(a + mid) + (np.pi / 2) / np.tan(np.pi * mid / 2)
        lo = np.where(val > 0, mid, lo); hi = np.where(val > 0, hi, mid)
    d = (lo + hi) / 2; xi = a + d
    h = 1e-6 * xi
    dLt = (Lt(xi + h) - Lt(xi - h)) / (2 * h)
    Fp = dLt - (np.pi ** 2 / 4) / np.sin(np.pi * d / 2) ** 2
    w = np.exp(logkappa(np.log(xi))) / (-Fp)
    return xi, w


class Renewal:
    def __init__(self, K=200000):
        self.xi, self.w = zeros(K)
        # tail: k >= K, xi from xi_K-1 + 1 on; integrate in u = log xi; asymptotic weight kappa/(pi^2/4 + Lt^2 - Lt')
        X0 = self.xi[-1] + 1.0
        u = np.log(X0) + np.concatenate([np.linspace(0, 40, 4001)[:-1], 40 + np.geomspace(1e-3, 1e5, 4000)])
        self.tu = u
        self.far = (u[-1] + CINF) ** -0.5  # int_{u_max}^inf (1/2) kappa/(Lt^2 + pi^2/4) du, kappa ~ sqrt(u + c_inf), rel. err O(u^-2)
        xi = np.exp(np.minimum(u, 700))
        Ltv = u - np.log(2) - PSI14
        Ltv[u < 30] = Lt(xi[u < 30])
        self.tw = np.exp(logkappa(u)) / (np.pi ** 2 / 4 + Ltv ** 2 - np.exp(-u))  # asymptotic w(xi); dk = dxi/2 = xi du/2

    def V(self, x):
        x = np.atleast_1d(np.asarray(x, float))
        out = B0 * x + np.array([np.sum(self.w * (-np.expm1(-self.xi * xx)) / self.xi) for xx in x])
        for i, xx in enumerate(x):  # tail: (1/2) w (1-e^{-x xi})/xi * xi du = (1/2) w (1-e^{-x xi}) du
            out[i] += np.trapezoid(0.5 * self.tw * -np.expm1(-xx * np.exp(np.minimum(self.tu, 700))), self.tu) + self.far
        return out

    def Vp(self, x):
        x = np.atleast_1d(np.asarray(x, float))
        out = B0 + np.array([np.sum(self.w * np.exp(-self.xi * xx)) for xx in x])
        for i, xx in enumerate(x):
            g = np.exp(np.minimum(self.tu, 700))
            out[i] += np.trapezoid(0.5 * self.tw * g * np.exp(-xx * g), self.tu)
        return out

    def laplace_Vp(self, s):
        g = np.exp(np.minimum(self.tu, 700))
        return B0 / s + np.sum(self.w / (s + self.xi)) + np.trapezoid(0.5 * self.tw * g / (s + g), self.tu) + self.far


if __name__ == "__main__":
    import time
    t0 = time.time()
    Rn = Renewal()
    print(f"b0 = {B0:.10f}, f'(0) = {FP0:.10f}, c_inf = {CINF:.10f}; first zeros {Rn.xi[:4]}, weights {Rn.w[:4]}"
          f"  ({time.time()-t0:.1f}s)")
    for s in (0.1, 1.0, 10.0, 1e2, 1e4, 1e8):
        lk = logkappa(np.log(s))[0]
        print(f"  s={s:8.0e}: Laplace(V') = {Rn.laplace_Vp(s):.12f}   1/kappa(s) = {np.exp(-lk):.12f}   "
              f"rel.diff {Rn.laplace_Vp(s)*np.exp(lk)-1:+.1e}   kappa/sqrt(Phi) = {np.exp(lk - logPhi(np.log(s))[0]/2):.8f}")
    for a in (0.8, 0.1, 1e-2, 1e-4, 1e-8, 1e-13, 1e-30):
        print(f"  a={a:7.0e}: V={Rn.V(a)[0]:.10f}  V'={Rn.Vp(a)[0]:.6e}  V*l^1/2={Rn.V(a)[0]*np.sqrt(max(np.log(1/a),1e-300)):.8f}")
    assert abs(Rn.laplace_Vp(1.0) * np.exp(logkappa(0.0)[0]) - 1) < 1e-6
