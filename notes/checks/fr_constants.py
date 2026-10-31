"""Final referee (laws): independent recomputation of the decisive constants.

mpmath + numpy, light. Run: python3 -I fr_constants.py > fr_constants.out
Shares no code with the write-ups or the laws note.

A  symbol constants: c, c_a, c + c_a + log 2pi, a_1, D_0; a(t) = 2 theta'(t) (Riemann-Siegel theta).
B  T6(a) moments via the Mellin closed form d^k/ds^k [Gamma(s) sin(pi s/2)] at s = 0 (no oscillatory quadrature).
C  (R2) on the true symbol: 2R(x) = (2/pi) int Si(x t) d(-1/sigma_1(t)); 1/(2R) - l -> a_1 = 3.957091,
   (2R - 1/(l + a_1)) l^3 -> pi^2/12.
D  Lemma T: arg K(it) = (1/pi) int log(sigma(t e^v)/sigma(t)) dv/(2 sinh v) vs pi/(4L) + pi^3/(24 L^3).
E  Lemma P / Lemma O on the exact model kernel R(x) = 1/(2(l(x)+b)): side constants (2a+1)/(2a+2), -1/(2a+2);
   jump = 2R(d) Phi(d) + O(l^{-a-3}); report the l^{a+3} residual.
F  Landau sign on actual zeros (numerics/zeros.txt): sum_{0<g<=T} cos(g log X) vs -(T/2pi) Lambda(X)/sqrt(X).
G  Prime-power boost beta_n = Omega_2(y_n)/(c_n A_+) by direct enumeration of length-2 chains (generic L).
"""
import math
import mpmath as mp
import numpy as np

mp.mp.dps = 25
g = mp.euler
print("== A. symbol constants")
c = mp.digamma(mp.mpf(1) / 4) - mp.log(mp.pi)
c_a = g + mp.pi / 2 + 2 * mp.log(2)
print("c =", mp.nstr(c, 10), " c_a =", mp.nstr(c_a, 10), " c+c_a+log2pi =", mp.nstr(c + c_a + mp.log(2 * mp.pi), 3))
print("a_1 = 1 + pi/2 + 2log2 =", mp.nstr(1 + mp.pi / 2 + 2 * mp.log(2), 10), " D_0 = log2pi + gamma =", mp.nstr(mp.log(2 * mp.pi) + g, 10))
Psi_a = lambda t: mp.re(mp.digamma(mp.mpf(1) / 4 + 0.5j * t)) - mp.digamma(mp.mpf(1) / 4)
for t in (1e3, 1e6):
    print(f"  t={t:g}: Psi_a(t)-log t = {mp.nstr(Psi_a(t) - mp.log(t), 10)} (-> c_a);"
          f"  a(t) - 2 theta'(t) = {mp.nstr(Psi_a(t) + c - 2 * mp.siegeltheta(t, derivative=1), 3)};"
          f"  a(t) - log(t/2pi) = {mp.nstr(Psi_a(t) + c - mp.log(t / (2 * mp.pi)), 3)}")

print("\n== B. cosine moments from f(s) = Gamma(s) sin(pi s/2) = int_0^inf sin(u) u^{s-1} du")
ser = lambda s: mp.gamma(1 + s) * (mp.pi / 2) * (mp.sinc(mp.pi * s / 2))
J0, J1, J2 = ser(0), mp.diff(ser, 0, 1), mp.diff(ser, 0, 2)
print("  int sin u/u =", mp.nstr(J0, 12), " int sin u log u/u =", mp.nstr(J1, 12), " (-pi gamma/2 =", mp.nstr(-mp.pi * g / 2, 12), ")")
print("  int sin u log^2 u/u =", mp.nstr(J2, 12), " ((pi/2)(gamma^2+pi^2/12) =", mp.nstr(mp.pi / 2 * (g**2 + mp.pi**2 / 12), 12), ")")
mu1 = 2 / mp.pi * (J1 + J0)                 # by parts: int (1-cos u) log u/u^2 = int sin u (log u + 1)/u
mu2 = 2 / mp.pi * (J2 + 2 * J1 + 2 * J0)
print("  mu1 =", mp.nstr(mu1, 15), " 1-gamma =", mp.nstr(1 - g, 15))
print("  mu2 - mu1^2 =", mp.nstr(mu2 - mu1**2, 15), " 1+pi^2/12 =", mp.nstr(1 + mp.pi**2 / 12, 15))
# direct check of mu1 by quadrature (independent of the by-parts step)
h = lambda u: (1 - mp.cos(u)) * mp.log(u) / u**2
mu1q = 2 / mp.pi * (mp.quad(h, [0, 1]) + mp.quad(lambda u: mp.log(u) / u**2, [1, mp.inf])
                     - mp.quadosc(lambda u: mp.cos(u) * mp.log(u) / u**2, [1, mp.inf], omega=1))
print("  mu1 by quadrature =", mp.nstr(mu1q, 15))

print("\n== C. (R2) on the true symbol, q = 1")
q = 1
sig = lambda t: q + Psi_a(t)
dsig = lambda t: -0.5 * mp.im(mp.psi(1, mp.mpf(1) / 4 + 0.5j * t))   # d/dt Re psi(1/4+it/2)
a1 = q + c_a - g
def twoR(l):
    x = mp.e**(-l)
    U = l + 40                                # x e^U = e^40: Si = pi/2 to e^-40
    integrand = lambda u: mp.si(x * mp.e**u) * mp.e**u * dsig(mp.e**u) / sig(mp.e**u)**2
    pts = [-40, -10, 0, l - 5, l, l + 5, U]
    I = mp.quad(integrand, pts) + (mp.pi / 2) / sig(mp.e**U)
    return 2 / mp.pi * I
for l in (10, 20, 40, 80):
    tR = twoR(l)
    print(f"  l={l:3d}: 1/(2R)-l = {mp.nstr(1/tR - l, 8)}  (a_1 = {mp.nstr(a1, 8)});"
          f"  (2R - 1/(l+a_1)) l^3 = {mp.nstr((tR - 1/(l + a1)) * l**3, 6)}  (pi^2/12 = 0.822467)")

print("\n== D. Lemma T: theta(t) = arg K(it), q = 1")
def theta(lt):
    t = mp.e**lt
    st = sig(t)
    F = lambda v: mp.log(sig(t * mp.e**v) / st) / (2 * mp.sinh(v)) if v != 0 else dsig(t) * t / st / 2
    return (mp.quad(F, [-lt - 30, -lt, -5, 0]) + mp.quad(F, [0, 5, 60])) / mp.pi
for lt in (10, 20, 40, 80):
    L_ = lt + q + c_a
    th = theta(lt)
    print(f"  log t={lt:3d}: (theta - pi/(4L)) L^3 = {mp.nstr((th - mp.pi / (4 * L_)) * L_**3, 6)}  (pi^3/24 = 1.291928)")

print("\n== E. Lemma P / Lemma O on the model kernel R(x) = 1/(2(l(x)+b)), germ phi = l^{-a} on (0, delta)")
def model(a, b, l, beta=0):
    d = mp.e**(-l)
    R = lambda x: 1 / (2 * (mp.log(1 / x) + b)) if x > 0 else mp.mpf(0)
    phi = lambda tau: (mp.log(1 / tau) + beta) ** (-a)
    dphi = lambda tau: a / tau * (mp.log(1 / tau) + beta) ** (-a - 1)
    ldel = 6.0                                   # delta = e^-6
    # T1 = int_0^d phi' R ; T2 = int_0^d phi'(tau) R(d - tau); T2p = int_0^d phi'(tau) R(d + tau)
    # tau = d e^{-s}, s in (0, inf): phi'(tau) dtau = a (l + s + beta)^{-a-1} ds  (the mass of phi' sits at tau << d,
    # so the integral must be taken in s; tanh-sinh on u = tau/d in [0,1] misses it)
    w = lambda s: a * (l + s + beta) ** (-a - 1)
    br = [0, 1, 10, 100, 1000, 10000, mp.inf]
    T1 = mp.quad(lambda s: w(s) * R(d * mp.e**(-s)), br)
    T2 = mp.quad(lambda s: w(s) * R(-d * mp.expm1(-s)), br)
    T2p = mp.quad(lambda s: w(s) * R(d * (1 + mp.e**(-s))), br)
    # tau = d e^s on (d, delta)
    smax = l - ldel
    T3 = mp.quad(lambda s: dphi(d * mp.e**s) * d * mp.e**s * (R(d * mp.e**s) - R(d * (mp.e**s - 1))), [0, 1, 5, smax])
    T3p = mp.quad(lambda s: dphi(d * mp.e**s) * d * mp.e**s * (R(d * (mp.e**s + 1)) - R(d * mp.e**s)), [0, 1, 5, smax])
    left = T1 + T2 + T3            # w(-d) - w(0), up to O(d)
    right = T1 - T2p - T3p         # w(d) - w(0)
    return left, right, R(d), phi(d)
for a in (0.5, 1.5):
    for l in (20, 80, 320, 1280):
        left, right, Rd, phid = model(a, 0, l)
        s = mp.mpf(l) ** (-a - 1)
        jump = left - right
        print(f"  a={a}: l={l:5d}  left/l^-a-1 = {mp.nstr(left/s, 6)} (pred {mp.nstr((2*a+1)/(2*a+2), 6)})"
              f"  right/l^-a-1 = {mp.nstr(right/s, 6)} (pred {mp.nstr(-1/(2*a+2), 6)})"
              f"  (jump - 2R(d)phi(d)) l^(a+3) = {mp.nstr((jump - 2*Rd*phid) * mp.mpf(l)**(a+3), 5)} (a pi^2/12 = {mp.nstr(a*mp.pi**2/12, 5)})")
left, right, Rd, phid = model(0.5, 2, 1280, beta=-1)
print(f"  a=0.5, b=2, beta=-1, l=1280: (jump - 2R phi) l^3.5 = {mp.nstr((left-right-2*Rd*phid)*mp.mpf(1280)**3.5, 5)}")

print("\n== F. Landau sign on actual zeros: S_X(T) = sum_{0<g<=T} cos(g log X)  vs  -(T/2pi) Lambda(X)/sqrt(X)")
import os
zf = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "numerics", "zeros.txt")
gam = np.loadtxt(zf)
def Lam(n):
    for p in range(2, n + 1):
        if n % p == 0:
            m = n
            while m % p == 0:
                m //= p
            return math.log(p) if m == 1 else 0.0
    return 0.0
for X in (2, 3, 4, 5, 6, 8, 10):
    out = []
    for T in (2000.0, 5000.0, float(gam[-1])):
        S = np.cos(gam[gam <= T] * math.log(X)).sum()
        out.append(f"T={T:7.0f}: S={S:9.2f} pred={-T/(2*math.pi)*Lam(X)/math.sqrt(X):9.2f}")
    print(f"  X={X:2d}: " + "  ".join(out))

print("\n== G. boost beta_n = (sum of length-2 chain weights from +L to y_n) / c_n, generic L")
cn = lambda n: Lam(n) / math.sqrt(n)
def beta_table(L):
    NL = [n for n in range(2, 200) if Lam(n) > 0 and math.log(n) < 2 * L]
    res = {}
    for n in NL:
        y = L - math.log(n)
        tot = 0.0
        for n1 in NL:
            z1 = L - math.log(n1)               # first step from +L must go down
            if not (-L < z1 < L):
                continue
            for n2 in NL:
                for e in (+1, -1):
                    z2 = z1 + e * math.log(n2)
                    if abs(z2 - y) < 1e-12 and -L < z2 < L:
                        tot += cn(n1) * cn(n2)
        res[n] = tot / cn(n)
    return res
for L in (1.0, 1.19, 1.5):
    bt = beta_table(L)
    print(f"  L={L}: " + "  ".join(f"b{n}={bt[n]:.3f}" for n in sorted(bt) if n <= 16))
print("  2 c2 c3 =", round(2 * cn(2) * cn(3), 5), "  c_n:", {n: round(cn(n), 5) for n in (2, 3, 4, 5, 7, 8, 9)})
