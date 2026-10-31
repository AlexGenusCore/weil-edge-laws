"""Constants entering the registered predictions (no solver output used)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import p1weil as W
import kink_analyze as K
print('log(2 pi) + gamma =', np.log(2 * np.pi) + W.EG)
for L in (0.6, 0.8, 1.0):
    c = K.cn_table(L)
    print(f'L={L}: X={np.exp(2*L):.4f}  c_n: ' + ', '.join(f'{n}:{v:.6f}' for n, v in c.items()))
    for n in c:
        print(f'    y_{n} = {L-np.log(n):+.6f}   beta_{n} = W2/c_n = {K.W2(L, n)/c[n]:.6f}')
    cp = W.chain_points(L)
    for p, (g, w) in sorted(cp.items()):
        if g == 2:
            print(f'    gen2 point {p:+.6f}  (L - log {np.exp(L-p):.6f})  W2 = {w:.6f}')
for X in (6, 8, 10):
    pp = W.prime_powers(X)
    s2 = sum((lam / np.sqrt(n)) ** 2 for n, lam in pp)
    cx = [lam / np.sqrt(n) for n, lam in W.prime_powers(X + 1) if n == X]
    pairs = sum((l1 / np.sqrt(n1)) * (l2 / np.sqrt(n2)) for n1, l1 in pp for n2, l2 in pp if n1 * n2 == X)
    print(f'X={X}: L={np.log(X)/2:.6f}  c_X={cx[0] if cx else 0:.6f}  2c_X={2*(cx[0] if cx else 0):.6f}'
          f'  sum_(n<X) c_n^2={s2:.4f}  sum_(nm=X) c_n c_m={pairs:.4f}')
