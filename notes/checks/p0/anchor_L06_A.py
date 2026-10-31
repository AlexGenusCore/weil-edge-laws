"""L=0.6, s=0: edge trace A at finer meshes (lambda' is mesh-robust: -4.911216 e, -0.1361423 o)."""
import sys; sys.path.insert(0, '.')
import numpy as np, p0_anchor as A
L = 0.6
lp = {'e': -4.911216, 'o': -0.1361423}
for NH, rho in ((500, 1.25), (1000, 1.5), (2000, 1.5)):
    out, N, _ = A.run(L, L / NH, rho, svals=(0.0,))
    print(f'NH={NH} rho={rho} N={N}: ' + '  '.join(
        f'{p}: lam={out[(0.0,p)][0]:.9f} A={out[(0.0,p)][1]:.6f} ratio={-lp[p]/(2*out[(0.0,p)][1]**2):.5f}' for p in 'eo'), flush=True)
