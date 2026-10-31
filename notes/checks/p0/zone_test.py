"""Does grading at the prime images change A when primes are switched OFF? (should not, beyond mesh error)"""
import sys; sys.path.insert(0, '.')
import numpy as np, p0_edge as P, p0_anchor as A
L = 0.4; h0 = L / 500; rho = float(sys.argv[1]) if len(sys.argv) > 1 else 1.5
pu = P.primes_upto
for zones in (True, False):
    for primes in (False, True):
        if zones:
            C, taus, cnt = A.build(L, h0, rho)
        else:
            P.primes_upto = lambda N: []
            C, taus, cnt = A.build(L, h0, rho)
            P.primes_upto = pu
        bsave = A.build
        A.build = lambda *a, **k: (C, taus, cnt)
        if not primes:
            P.primes_upto = lambda N: []
        Q, h, X, o1, o2, va, vb, _ = A.assemble(L, h0, rho)
        P.primes_upto = pu; A.build = bsave
        for par in ('e', 'o'):
            lam, f, _ = P.eig(Q, h, k=1, parity=par)[0]
            print(f'zones={zones} primes={primes} N={len(h)} {par}: lam={lam:.9f} A={A.edge_fit(f, X, o1, o2, L):.6f}', flush=True)
