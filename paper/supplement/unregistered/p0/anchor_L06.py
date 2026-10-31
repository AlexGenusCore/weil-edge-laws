"""L=0.6 (primes 2 and 3 active), rho=1.5 only; rho-shift taken from the L=0.4 run."""
import sys, time; sys.path.insert(0, '.')
import numpy as np, p0_anchor as A
L0, NH, d, rho = 0.6, 500, 1e-3, 1.5
t = time.time()
mid, N, cnt = A.run(L0, L0 / NH, rho)
lo, _, _ = A.run(L0 - d, L0 / NH, rho, counts=cnt)
hi, _, _ = A.run(L0 + d, L0 / NH, rho, counts=cnt)
print(f'L={L0} NH={NH} rho={rho} N={N} ({time.time()-t:.0f}s)')
for key in mid:
    lp = (hi[key][0] - lo[key][0]) / (2 * d)
    Aa = mid[key][1]
    print(f'  s={key[0]} {key[1]}: lam={mid[key][0]:.10f} lam\'={lp:+.6e} A(rho=1.5)={Aa:.6f}  -lam\'/(2A^2)={-lp/(2*Aa*Aa):.5f}', flush=True)
