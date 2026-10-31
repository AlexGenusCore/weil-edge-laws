"""Zeta zeros 1..NMAX at 30 digits (Arb via python-flint), cross-checked against
mpmath.zetazero (dps=30) at indices 1..50 and every 50th index.  Writes zeros.txt
(one ordinate per line, 30 significant digits) and zeros_check.out."""
import sys, time
import flint, mpmath as mp
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 10500
flint.ctx.dps = 30
mp.mp.dps = 30
t0 = time.time()
out = []
for a in range(1, NMAX + 1, 1000):
    k = min(1000, NMAX + 1 - a)
    for z in flint.acb.zeta_zeros(a, k):
        assert abs(z.real - flint.arb(0.5)) < 1e-25
        out.append(z.imag.mid().str(30, radius=False))
print('arb zeros', len(out), 'time %.0fs' % (time.time() - t0), flush=True)
with open('zeros.txt', 'w') as f:
    f.write('\n'.join(out) + '\n')
idx = list(range(1, 51)) + list(range(100, NMAX + 1, 50))
worst = 0
with open('zeros_check.out', 'w') as f:
    for n in idx:
        g = mp.zetazero(n).imag
        d = abs(g - mp.mpf(out[n - 1]))
        worst = max(worst, d)
        f.write('%d %s %s\n' % (n, mp.nstr(g, 30), mp.nstr(d, 3)))
    f.write('checked %d indices, max |mpmath - arb| = %s, time %.0fs\n' % (len(idx), mp.nstr(worst, 3), time.time() - t0))
print('checked', len(idx), 'max diff', worst, flush=True)
