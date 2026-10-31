"""Synthesis checks (laptop, mpmath, light).

1. Constants: c, c_a, b_0 = log 2pi + gamma, c + c_a = -log 2pi.
2. Cosine moments mu_k = (2/pi) int_0^inf (1 - cos u) log^k u / u^2 du:
   mu_0 = 1, mu_1 = 1 - gamma (claimed), mu_2 (reported).
3. Smoothed edge x edge factor
     I_s(z, lam) = (2/pi) int_{z t0}^inf (1 - cos u) / (u^2 (a(u/z) - lam)) du
   against 1/(l - b_lam + 1), l = log(1/z), b_lam = log 2pi + gamma + lam.
   Claim (tail_kink_laws_note.md, T6(b)): the difference is O(l^-3), coefficient ~ (mu_2 - mu_1^2).
4. Sharp edge x edge factor
     I_T(T, lam) = T int_T^inf dt / (t^2 (a(t) - lam))
   against 1/(log(T/2pi) - lam + 1); difference O(l^-3), coefficient ~ (2 - 1) = 1.
a(t) = Re digamma(1/4 + i t/2) - log pi (exact symbol).
Run: python -I denominators_check.py > denominators_check.out
"""
import mpmath as mp

mp.mp.dps = 30
g = mp.euler
c = mp.digamma(mp.mpf(1) / 4) - mp.log(mp.pi)
c_a = g + mp.pi / 2 + 2 * mp.log(2)
b0 = mp.log(2 * mp.pi) + g
print(f"c = {mp.nstr(c, 10)}   c_a = {mp.nstr(c_a, 10)}   c + c_a + log(2pi) = {mp.nstr(c + c_a + mp.log(2*mp.pi), 3)}")
print(f"b_0 = log(2pi) + gamma = {mp.nstr(b0, 10)}   1 + c_a - gamma = {mp.nstr(1 + c_a - g, 10)}")
print(f"pi^2/12 = {mp.nstr(mp.pi**2/12, 8)}   pi^3/24 = {mp.nstr(mp.pi**3/24, 8)}")


def mom(k):
    f = lambda u: (1 - mp.cos(u)) * mp.log(u) ** k / u ** 2
    head = mp.quad(f, [0, 1])
    tail = mp.quad(lambda u: mp.log(u) ** k / u ** 2, [1, mp.inf]) - \
        mp.quadosc(lambda u: mp.cos(u) * mp.log(u) ** k / u ** 2, [1, mp.inf], omega=1)
    return 2 / mp.pi * (head + tail)


mu = [mom(k) for k in range(3)]
print(f"mu_0 = {mp.nstr(mu[0], 12)} (expect 1)")
print(f"mu_1 = {mp.nstr(mu[1], 12)}   1 - gamma = {mp.nstr(1 - g, 12)}   diff = {mp.nstr(mu[1] - (1 - g), 3)}")
print(f"mu_2 = {mp.nstr(mu[2], 12)}   var = mu_2 - mu_1^2 = {mp.nstr(mu[2] - mu[1]**2, 8)}"
      f"   1 + pi^2/12 = {mp.nstr(1 + mp.pi**2/12, 8)}")


def a_sym(t):
    return mp.re(mp.digamma(mp.mpf(1) / 4 + 0.5j * t)) - mp.log(mp.pi)


def I_smooth(z, lam, t0=20):
    u0 = z * t0
    f = lambda u: 1 / (u ** 2 * (a_sym(u / z) - lam))
    head = mp.quad(lambda u: (1 - mp.cos(u)) * f(u), [u0, 1])
    tail = mp.quad(f, [1, mp.inf]) - mp.quadosc(lambda u: mp.cos(u) * f(u), [1, mp.inf], omega=1)
    return 2 / mp.pi * (head + tail)


def I_sharp(T, lam):
    # substitute t = T u, so the integrand lives on [1, inf) at every T
    return mp.quad(lambda u: 1 / (u ** 2 * (a_sym(T * u) - lam)), [1, 10, 100, mp.inf])


print("\nSmoothed factor I_s(z,lam) vs 1/(l - b_lam + 1):  columns l, I_s, pred, (I_s-pred)*l^3")
for lam in (0, -2, -4.5):
    for l in (20, 40, 80):
        z = mp.e ** (-l)
        Is = I_smooth(z, lam)
        pred = 1 / (l - (b0 + lam) + 1)
        print(f"  lam={lam:5}: l={l:3d}  I_s={mp.nstr(Is, 10)}  pred={mp.nstr(pred, 10)}  diff*l^3={mp.nstr((Is - pred) * l**3, 5)}")

print("\nSharp factor I_T(T,lam) vs 1/(log(T/2pi) - lam + 1):  columns logT, I_T, pred, (I_T-pred)*log(T/2pi)^3")
for lam in (0, -2, -4.5):
    for lt in (20, 40, 80):
        T = mp.e ** lt
        It = I_sharp(T, lam)
        lp = mp.log(T / (2 * mp.pi))
        pred = 1 / (lp - lam + 1)
        print(f"  lam={lam:5}: logT={lt:3d}  I_T={mp.nstr(It, 10)}  pred={mp.nstr(pred, 10)}  diff*l'^3={mp.nstr((It - pred) * lp**3, 5)}")
