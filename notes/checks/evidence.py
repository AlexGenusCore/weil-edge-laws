"""Evidence table for edge_hadamard_note_v2.md (section 13.1).

Part 1 recomputes the derived ratios quoted in the note from the numbers printed by the
final referee's independent P0 code (p0/*.out); file and line are named
next to each number.
Part 2 reruns two cheap pure-log cases of the referee's code (p0_edge.py, imported read-only)
and checks that they reproduce conv_purelog.out.

Run: python3 -I evidence.py   (about 15 s, < 0.5 GB)
"""
import os, sys
import numpy as np

REF = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'p0')
X1, X2 = np.log(1.5) ** 2, np.log(1.25) ** 2      # referee's rho -> 1 extrapolation variable


def rho_extrap(a15, a125):
    return a125 - (a15 - a125) * X2 / (X1 - X2)


def ratio(lp, A):
    return -lp / (2 * A * A)


print('Part 1: derived ratios -lambda\'/(2A^2) from the referee outputs')
# L = 0.4, s = 0, mesh graded at the prime images (anchor_L0.4_NH500.out, h0 = L/500)
lp = {'e': -4.926140, 'o': -4.063344e-01}                      # lam'(rho=1.25)
A15 = {'e': 1.570850, 'o': 0.451604}
A125 = {'e': 1.569987, 'o': 0.451197}
A_NH2000_15 = {'e': 1.570498, 'o': 0.451265}                  # anchor_conv_L0.4.out, h0 = L/2000, rho = 1.5
for p in 'eo':
    a0 = rho_extrap(A15[p], A125[p])
    a_ref = A_NH2000_15[p] + (a0 - A15[p])                     # additive rho-shift taken from h0 = L/500
    print(f'  L=0.4 s=0 {p}: h0=L/500 rho->1: A={a0:.6f} ratio={ratio(lp[p], a0):.5f};'
          f'  h0=L/2000 (+rho shift): A={a_ref:.6f} ratio={ratio(lp[p], a_ref):.5f};'
          f'  sqrt(-lam\'/2)={np.sqrt(-lp[p] / 2):.5f}')

# L = 0.6, s = 0 (anchor_L0.6.out, anchor_L0.6_A.out); lam' from the h0 = L/500, rho = 1.5 run only
lp6 = {'e': -4.911216, 'o': -0.1361423}
r = {'e': (0.99824, 0.99925, 0.99862), 'o': (0.99391, 0.99623, 0.99610)}   # (NH500 rho1.5, NH500 rho1.25, NH2000 rho1.5)
for p in 'eo':
    r15, r125, r2000 = r[p]
    r_rho = r125 + (r125 - r15) * X2 / (X1 - X2)               # ratio ~ A^-2, linearised rho -> 1
    print(f'  L=0.6 s=0 {p}: NH500 rho->1: {r_rho:.5f};  + h0 shift (NH500 -> NH2000 at rho=1.5): '
          f'{r_rho + (r2000 - r15):.5f}')

print('\nPart 2: rerun of two pure-log cases (L = 0.5, h0 = L/250) of the referee code')
sys.path.insert(0, REF)
import p0_edge as P                                            # noqa: E402

expect = {2.0: (1.002685, 1.003949, 1.004835), 1.5: (1.001130, 1.001806, 1.002322)}  # conv_purelog.out lines 1-2
L = 0.5
for rho, want in expect.items():
    Q, h, side, R1, R2 = P.assemble(L, 'log', h0=L / 250, rho=rho, rmin=1e-150)
    got = [P.edge_fit(f, side, R1, R2, lmin=30.0, nterm=4)[0][0] for lam, f, par in P.eig(Q, h, k=3)]
    print(f'  rho={rho} N={len(h)}: A = ' + ', '.join(f'{a:.6f}' for a in got)
          + '   (file: ' + ', '.join(f'{a:.6f}' for a in want) + ')')
    assert np.allclose(got, want, atol=2e-6), 'referee output not reproduced'
    del Q
print('  reproduced to 2e-6')
