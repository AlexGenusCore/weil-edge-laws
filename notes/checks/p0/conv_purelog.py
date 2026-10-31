"""Pure log, L=0.5: convergence of the fitted edge trace A in the mesh parameters.
Theorem 4 predicts A^2 = 1/(2L) = 1 for every eigenfunction."""
import sys, time
sys.path.insert(0, '.')
import numpy as np
import p0_edge as P

L = 0.5
rows = []
for nh in (250, 500):
    for rho in (2.0, 1.5, 1.25):
        t = time.time()
        Q, h, side, R1, R2 = P.assemble(L, 'log', h0=L / nh, rho=rho, rmin=1e-150)
        res = P.eig(Q, h, k=3)
        out = []
        for lam, f, par in res:
            coef, resid, ell, y = P.edge_fit(f, side, R1, R2, lmin=30.0, nterm=4)
            out.append((par, lam, coef[0]))
        rows.append((nh, rho, out))
        print(f'h0=L/{nh} rho={rho} N={len(h)} ({time.time()-t:.0f}s): ' +
              '  '.join(f'{p} lam={l:.7f} A={a:.6f}' for p, l, a in out), flush=True)
        del Q
# extrapolate rho -> 1 assuming error ~ (log rho)^2, at each h0
print('extrapolation in (log rho)^2 using rho=1.5,1.25:')
for nh in (250, 500):
    r = {rho: out for n, rho, out in rows if n == nh}
    for k in range(3):
        a1, a2 = r[1.5][k][2], r[1.25][k][2]
        x1, x2 = np.log(1.5) ** 2, np.log(1.25) ** 2
        a0 = a2 - (a1 - a2) * x2 / (x1 - x2)
        print(f'  h0=L/{nh} {r[1.5][k][0]}{k}: A(rho->1) = {a0:.6f}  2L*A^2 = {2*L*a0*a0:.6f}')
