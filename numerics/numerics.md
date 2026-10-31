# Independent numerical test of the kink-law and tail-law constants

*Johann Alexander Botha (GenusCore, info@genuscore.com), 2026-10-31. Part of the research notes in this repository: not peer-reviewed, produced largely with an AI assistant (Anthropic's Claude, via Claude Code), checked only by AI referees; see the status header in [`../README.md`](../README.md). Pre-registration: `PREREG.md` (md5 `b880e0faf068419f8ec59d230f66265f`, registered 04:27:15 SAST; the text says 04:30, the md5 file has the exact time). Float64 Galerkin numerics on one Linux VM. Nothing here is certified, and nothing here is a statement about RH.*

*Labels.* [KW], [KL] (kink) and [TA], [TE] (tail) are the two independent internal write-ups per law described in [`../notes/tail_kink_laws_note.md`](../notes/tail_kink_laws_note.md); they are not included here. `PREREG.md` is kept byte-for-byte (so its md5 still matches) and calls them kink-wienerhopf, kink-levy, tail-abelian and tail-explicit. Theorem numbers K0′, K1, K2, K5 below are those of the write-ups; in the laws note they are K1(c), K3 (generations 1 and 2) and K5.

## 0. Verdict

The solver is new code: a continuous piecewise-linear (P1) Galerkin method. It shares only the form definition with the project's hp-FEM, with the final referee's P0 code, and with the write-ups' scripts, which all used the referee's P0 code. Before any production run it passed three gates:
- Weil's explicit formula against 10 500 zeta zeros, to the size of the estimated tail (≤ 1.1e-9);
- an independent position-side formula for the jump form;
- the referee's L = 0.4 values.

**Kink law (Theorems K1, K2, K5, K0′ of [KW], [KL]).**

| Predicted constant | Where tested | Measured | Registered verdict |
|---|---|---|---|
| jump coefficient κ = 1 (generation 1) | L = 0.6, 0.8, 1.0; n = 2, 3, 4 (and 5, 7 at L = 1.0); 50 graded rows | 0.9986–1.0019 | **PASS 50/50** |
| cusp coefficient 1/3 | same rows | 0.3322–0.3346 | **PASS 50/50** |
| side ratio −2, larger excursion on the source side, sign of A | same rows | −1.9969 … −2.0035 | **PASS 50/50** |
| generation 2: jump 1, cusp 1/5, side −3/2 (L − log 1.5, L − log(4/3), and L − log 6 at L = 1.0) | 20 graded rows | jump 0.9912–1.0054, cusp 0.1967–0.2018, side −1.4940 … −1.5025 | **PASS 20/20** |
| K5 offset 1/ρ_n − ℓ → −D − β_n, with boosts β₂ = 0.347 and β₄ = 0.693 at L = 0.8 (no boost is active at L = 0.6, where X = 3.32) | L = 0.6, 0.8 | deviation −0.0025 … −0.0005 after ρ-extrapolation | **PASS** |
| | L = 1.0, registered meshes | +0.011 … +0.061 for n = 3, 4, 5, 7 | **FAIL**: 17 of the 50 graded K5 rows fail, all at L = 1.0 (mesh defect, §3.4); overall 33/50 |
| | L = 1.0, all coupled generation-2 points graded deep (post-registration diagnostic) | −0.0040 … −0.0007 for all n | consistent with K5 (not a registered verdict) |
| K0′ edge law ψ(L − r) = A(ℓ − D)^{−1/2}, D = λ + log 2π + γ | L = 0.6, 0.8, 1.0 | D_fit − D = +0.0013 … +0.0049 after ρ-extrapolation | **PASS 40/50** (the 10 fails are the L = 1.0 sensitivity mesh, §3.4) |

**Tail law ([TA] Prop E1 / Conjecture L; [TE] Pred F).** There are four clean states per X, two per sector, at X = 6, 8 and 10. Eleven of the twelve passed the validity gate; X = 6 O5 failed it narrowly and was reported but not graded. All 11 are graded.

| Predicted item | Measured | Registered verdict |
|---|---|---|
| T1: zero-side tail Z = (\|λ'\|/π)∫(a + εc_X)/(t²(a − λ)) up to kink terms O(Σc_n²/a²) | Z/P1 = 0.80–1.00 at T ≥ 100, rising to 0.968–1.000 on [6400, 10300]. The registered tolerance was generous; on blocks with T₁ ≥ 400 the actual deviations are −8.7% … +0.03% (§4.2). | **PASS 11/11** |
| T1-full: πT Z(T)/\|λ'\| = T∫_T^∞(a + εc_X)/(t²(a − λ)) ≈ Pred F | τ/τ_pred − 1 between −6.9% and +0.1% at T ≥ 400; the largest gap is O5 at X = 10, T = 400 | **PASS 11/11** |
| T1-λ: the λ-shift is present | without it, Z/P drops to 0.20–0.87; with it, 0.80–1.00 | **PASS 11/11** |
| T2: sector split at X = 8 has α = 2c₈ = 0.490 | α = 0.51, 0.66, 0.52, 0.67 (±0.06–0.07) | **PASS 4/4** (two pairs 2.5σ high) |
| T2: control X = 6, α = 0 | α = +0.018 ± 0.072, +0.012 ± 0.068 | **PASS 2/2** |
| T2: control X = 10, α = 0 | α = +0.32 … +0.44 (±0.18–0.19) | **PASS 4/4 on the registered rule only.** 1.8–2.3σ from 0; not informative. |
| Leading law πT Z(T) → \|λ'\| (Theorem C / Corollary D) | τ(6400) = 0.47–0.81 for these large-\|λ\| states | asymptotic only; not gradable, as both tail write-ups already said |

**In one paragraph.**
- Every leading kink constant predicted by [KW] and [KL] is confirmed: to ≤ 0.4% at generation 1 and ≤ 1.6% at generation 2, on states with A from 0.26 to 1.64, in both sectors, at pole strengths 0 and 5. This covers κ = 1, the 2/3 : −1/3 split, the 3/5 : −2/5 split at generation 2, and the chain weights 2c₂c₃, c₂c₃ and c₃c₄. P1 needs no cell-average correction.
- The next-order K5 offset, with its prime-power boosts, holds to ≤ 0.004 wherever every coupled chain point is graded through the fit window. My registered L = 1.0 mesh violated that condition, so the registered verdict there is FAIL.
- The tail law's λ-shifted second-order form is confirmed by a wide margin: the unshifted form misses by a factor of 2–5.
- The c_X term at X = 8 is consistent with the data, and so is a clean zero at X = 6. The X = 10 control is too noisy to exclude a spurious 1/a split of size ~0.4. So the c_X term is supported, not established, at T ≤ 1e4. A post-hoc cross-X comparison (§4.4) supports it more directly.

---

## 1. Method

### 1.1 The form

All quantities follow the edge-law note ([`../notes/edge_hadamard_note_v2.md`](../notes/edge_hadamard_note_v2.md)) and the referee's position-side check:

$$Q^{(s)}_L(f)=\mathcal E_J(f)+c\|f\|^2-2\sum_{n<X}c_nR_f(\log n)+2s\,F(\tfrac i2)F(-\tfrac i2),\qquad \mathcal E_J(f)=\tfrac12\iint_{\mathbb R^2}(f(x)-f(y))^2J(|x-y|)\,dx\,dy,$$

where:
- $J(u)=e^{-u/2}/(1-e^{-2u})$ and $c=\psi(\frac14)-\log\pi$;
- $c_n=\Lambda(n)/\sqrt n$, $X=e^{2L}$, and $R_f(\tau)=\int f(y)f(y+\tau)\,dy$;
- $f$ is supported in $[-L,L]$.

The symbol of $\mathcal E_J$ is $\Psi_a(t)=\operatorname{Re}\psi(\frac14+\frac{it}2)-\psi(\frac14)$, so $a=\Psi_a+c$.

### 1.2 Discretisation: P1 with anchored nodes

**Space.** $V_h$ is the continuous piecewise-linear functions on a mesh $-L=x_0<\dots<x_M=L$ with $f(\pm L)=0$. This matches the regularity of eigenfunctions, which are continuous on $\mathbb R$ and vanish at $\pm L$ ([EH] Thm 1).

**Node storage.** Each node is stored as (anchor, offset). The anchors are:
- the edges $\pm L$;
- the generation-1 points $\pm(L-\log n)$;
- the generation-2 points.

Offsets are exact to relative 1e-16, so elements down to 1e-40 can be handled.

**Mesh.** Geometric zones $r_j=r_{\min}\rho^j$ on both sides of every anchor (one side at the edges), filled out to $\min(H/(\rho-1),\,0.45\cdot\text{gap})$, with uniform filler of size $\le H$ between zones.

**Lemma 1 (derivative representation; why P1 is natural).** Let $f$ be continuous and piecewise $C^1$ with bounded derivative and support in $[-L,L]$. Then
$$\mathcal E_J(f)=\iint f'(s)f'(s')\,K(|s-s'|)\,ds\,ds',\qquad K(w)=\int_w^\infty(u-w)J(u)\,du=\sum_{k\ge0}\frac{e^{-(2k+\frac12)w}}{(2k+\frac12)^2}.$$

*Proof.*
- Write $f(x)-f(y)=\int f'(s)\,[\mathbf 1_{y<s<x}-\mathbf 1_{x<s<y}]\,ds$ and square.
- For $s,s'$ with $m=\min$ and $M=\max$, the set of $(x,y)$ with $y<m\le M<x$ has $J$-mass $\int_0^\infty\!\int_0^\infty J(M-m+p+q)\,dp\,dq=K(M-m)$. The case $x<y$ gives the same.
- Since $K(0)=\sum(2k+\frac12)^{-2}<\infty$, the integrand is absolutely integrable and Fubini applies. Hence $\mathcal E_J=\frac12\cdot2\iint f'f'K$. ∎

Consequences:
- $V_h$ is conforming: $\mathcal E_J(f)\le K(0)\|f'\|_1^2$.
- $\hat K(t)=\Psi_a(t)/t^2$, which is consistent with the symbol.
- For $f\in V_h$, $F(t)=-t^{-2}\sum_k\Delta s_k\,e^{itx_k}$, where $\Delta s_k$ is the jump in slope at node $x_k$. So a P1 function has no jump artefacts in its Fourier tail. A P0 step function does: there $|F|^2\sim(\text{jumps})^2/t^2$. This matters for the zero-side tail sums.

**Lemma 2 (the decomposition that is actually assembled).** Let $e_k=[x_k,x_{k+1}]$ and let $N_k=[x_{\max(k-1,0)},x_{\min(k+2,M)}]$ be its near zone. Then
$$\mathcal E_J(f)=\sum_k\int_{e_k}f^2W_k\;-\sum_{|k-j|\ge2}\iint_{e_k\times e_j}f(x)f(y)J+\tfrac12\sum_k\iint_{e_k^2}(f(x)-f(y))^2J+\sum_k\iint_{e_k\times e_{k+1}}(f(x)-f(y))^2J,$$
with $W_k(x)=\int_{\mathbb R\setminus N_k}J(|x-y|)\,dy=T(x-\min N_k)+T(\max N_k-x)$ and $T(r)=\operatorname{artanh}e^{-r/2}+\arctan e^{-r/2}$.

*Proof.*
- Split $\mathbb R^2$ into the element pairs inside $\Omega=[-L,L]$, plus $\Omega\times\Omega^c$ and $\Omega^c\times\Omega$; $f=0$ off $\Omega$.
- For non-adjacent pairs, expand $(f(x)-f(y))^2$. The $f(x)^2$ and $f(y)^2$ parts of all far pairs, together with the exterior, collect into $\int f^2W_k$. ∎

**Quadrature.**
- Self pairs: $P(h)=h^3/6+2\int_0^h(h-u)u^2J_r(u)\,du$, where $J_r=J-\frac1{2u}$ (Bernoulli series near 0).
- Adjacent pairs: closed forms in $a=h_2/h_1$, for example $\iint u^2/(2(u+v))=\frac{h_1^3}2[\int_0^1\xi^2\log(\xi+a)\,d\xi+\frac19]$, plus 6×6 Gauss for $J_r$.
- Far pairs at distance ≤ 4 element lengths: the 1/(2u) part is integrated analytically over the larger element, with 12-point Gauss over the smaller one.
- Far pairs at larger distance: 6×6 or 3×3 Gauss product on the full $J$.
- Weights: 12-point Gauss, with the $\log$ singularity of the boundary elements done exactly.
- Prime shifts: exact overlaps $\int\phi_i(y)\phi_j(y+\log n)\,dy$, computed in anchored coordinates (Simpson's rule is exact for the quadratic products).
- Pole: the rank-2 term $s(v_av_b^T+v_bv_a^T)$ with $v_{a,b}=\int\phi_k e^{\mp y/2}$.

**Eigen-solve.**
- Diagonally scaled generalised problem; bidiagonal Cholesky of the tridiagonal mass matrix; LAPACK `evr` for the lowest k states.
- Three steps of inverse iteration on the row-scaled system, which gives accurate values on 1e-40 elements. Residuals are ≤ 6e-13.

**Fourier transform.** $F(t)$ is computed exactly element by element, with phases in anchored coordinates.

Code: `p1weil.py` (solver and self-check), `runlib.py` (anchors, edge fits), `kink_run.py`, `tail_run.py`.

### 1.3 Gates (passed before registration; `p1weil.py`, `pilot_L04.py`)

| Gate | Result |
|---|---|
| $\mathcal E_J$ against an independent autocorrelation formula $2\int_0^\infty J(u)(g(0)-g(u))\,du$ (FFT, 2e5 points) | ≤ 1.1e-9 at L = 0.45, 0.9, 1.15 |
| $R_f(\log n)$ for all $n<X$, and the pole term, against fine-grid quadrature | ≤ 6e-11 |
| **Weil's explicit formula** $Q_1(f)=2\sum_{\gamma>0}\lvert F(\gamma)\rvert^2$ with 10 500 zeros, for a test P1 function | difference 2.2e-10, 7.8e-10, 1.1e-9 at L = 0.45, 0.9, 1.15; the estimated tails beyond γ₁₀₅₀₀ are 2.5e-10, 7.7e-10, 1.1e-9 |
| Referee's P0 values at L = 0.4 | λ_e = −1.5400081 (−1.5400); A_e = 1.56943 (1.5696); A_o = 0.45082 (0.4510); s = 1 A_e = 0.062001 (0.0621) |
| Zeros | Arb (python-flint `acb.zeta_zeros`, 30 digits); against `mpmath.zetazero` (dps 30) at 259 indices, max difference 4.7e-26 (`zeros_check.out`) |

**Deviation on the zeros.** The task asked for zeros from mpmath.zetazero. mpmath needs about 1 s per zero near n = 10⁴, which is about 3 hours of VM time for 10 500 zeros. I computed them with Arb and verified a sample with mpmath. They are the same numbers to 26 digits.

---

## 2. Convergence study and a numerical lesson

**Kink** (`kink_conv.py`; L = 0.6, s = 0; ρ = 1.5, 1.25, 1.15; H = L/40 and L/80).
- The leading constants change by ≤ 2.5e-5 between ρ = 1.25 and 1.15, and by ≤ 2e-9 under H refinement. This holds for A = 1.567 and for A = 0.26.
- The fit window (ℓ ≥ 12 versus ℓ ≥ 20) moves them by 4e-4 (A = 1.567) to 8e-3 (A = 0.26). This finite-ℓ remainder, not the mesh, is the limiting systematic.

**P1 resolution shift.** P1 nodal values on a geometric zone behave as if sampled at an effective offset θr. This is analogous to the write-ups' P0 "cell-average shift" δu.
- Model: $D_{\rm fit}-D$ and $-(b_0+D+\beta)$ both equal $\delta_\infty+0.084\,(\log\rho)^2$.
- The extrapolations from (1.5, 1.25) and from (1.25, 1.15) agree to 2e-5. The calibration-free combination $b_0+D_{\rm fit}$ is mesh-independent to 1e-4.
- P1 needs this ρ-extrapolation, but no model of the discretisation.

**Lesson: grading must cover the whole fit window at every coupled point** (`xcheck.py`, `out/xcheck.out`).
- Through the shift $c_n\psi(x-\log n)$, the edge profile at depth ℓ is fed by $\psi(y_n-r)$ at the same depth. Likewise, a kink at $y_n$ is fed by the zones at $y_n\pm\log m$ (the generation-2 points).
- If a coupled zone is truncated at $r_0$, the profile shows a step at $\ell=\log(1/r_0)$. With a 1e-9 truncation, the edge profile at X = 8 has a step of about 0.2% near ℓ ≈ 21.
- This is the mechanism behind the final referee's caveat that fitted A is biased unless the mesh is graded at $\pm(L-\log n)$. It extends to generation 2 for kink measurements.

**Tail** (`out/tail_conv.out`, X = 8; meshes base N = 2777, fine N = 4209, and one without generation-2 grading).
- For the ground states E0 and O5: blocks agree to ≤ 1.3e-4, λ' to ≤ 1e-4, A to ≤ 1e-5.
- Without generation-2 grading, blocks change by ≤ 5e-3.
- The excited s = 1 states are not converged (up to 5% in blocks, 8% in λ'). They also sit near avoided crossings: λ'(d) and λ'(2d) differ by 1–6%. They were registered as exploratory only.

---

## 3. Kink law

### 3.1 Statements tested

From [KW] (Thms K0′, K1, K2, K5) and [KL] (Thm C, Thm F).

Generic L. At a generation-k point q reached from the right edge with chain weight W:
$$\psi(q-r)-\psi(q)=\tfrac{k+1}{2k+1}WA_+\ell^{-k-1/2},\qquad\psi(q+r)-\psi(q)=-\tfrac{k}{2k+1}WA_+\ell^{-k-1/2},$$
both up to $O(\ell^{-k-3/2})$. Hence:
- the jump coefficient is 1;
- the cusp coefficient is $1/(2k+1)$;
- the side ratio is $-(k+1)/k$.

At mirror points, swap the sides and use $A_-$. At generation 1:
$$1/\rho_n=\ell-D-\beta_n+O(1/\ell),\qquad \rho_n=\mathsf J/(c_n\psi(L-r)),\quad D=\lambda+\log2\pi+\gamma,\quad\beta_n=W_2^+(y_n)/c_n .$$

### 3.2 Fitting (registered)

- Window ℓ ∈ [20, ℓ_max − 6], three-term expansions in 1/ℓ.
- The cusp fit uses $\psi(q-r)+\psi(q+r)=2\psi(q)+WA\ell^{-k-1/2}(\sigma_0+\sigma_1/\ell+\sigma_2/\ell^2)$, with $\psi(q)$ free. The node value at q is truncated by $r_{\min}$; in my smoke test it biased σ₀ to 1.27 instead of 0.33.
- A comes from $\psi(L-r)^{-2}=a_0\ell+a_1+a_2/\ell+a_3/\ell^2$.
- Graded states have |A| ≥ 0.2.

### 3.3 Results (finest mesh; full tables in `out/kink_table.out`, verdicts in `out/kink_summary.out`)

| L | state (s, sector, λ, A) | point | gen | κ₀ (1) | σ₀ (1/3 or 1/5) | side (−2 or −1.5) | K5: b₀ + D + β (extrap.) |
|---|---|---|---|---|---|---|---|
| 0.6 | 0, e, −2.4170, 1.5671 | y₃ = −0.4986 | 1 | 1.00014 | 0.33344 | −2.0003 | −0.0005 |
| 0.6 | same | y₂ = −0.0931 | 1 | 1.00014 | 0.33345 | −2.0003 | −0.0005 |
| 0.6 | same | L − log 1.5 | 2 (W = c₂c₃) | 1.00047 | 0.20015 | −1.5002 | — |
| 0.6 | 0, o, +0.0031, 0.2611 | y₃, y₂ | 1 | 1.00146, 1.00140 | 0.33459, 0.33455 | −2.0035, −2.0034 | −0.0018, −0.0018 |
| 0.6 | 5, o, −0.2481, 0.7285 | y₃, y₂ | 1 | 1.00116, 1.00110 | 0.33427, 0.33424 | −2.0025, −2.0024 | −0.0016, −0.0015 |
| 0.6 | mirror points −y₃, −y₂, −(L − log 1.5); all three states | | 1, 2 | equal to the right-side values to ≤ 2e-5, with A₋ | | | |
| 0.8 | 0, e, −3.3154, 1.4250 | y₄ = −0.5863 | 1 (β₄ = 0.693) | 1.00012 | 0.33343 | −2.0003 | −0.0007 |
| 0.8 | same | y₃ = −0.2986 | 1 (β₃ = 0) | 1.00000 | 0.33340 | −2.0003 | −0.0005 |
| 0.8 | same | y₂ = +0.1069 | 1 (β₂ = 0.347) | 1.00007 | 0.33342 | −2.0003 | −0.0006 |
| 0.8 | same | L − log 1.5, L − log(4/3) | 2 | 1.00006, 1.00028 | 0.20012, 0.20015 | −1.5003, −1.5003 | — |
| 0.8 | 5, o, −0.6567, 1.4374 | y₄, y₃, y₂ | 1 | 1.0019, 1.0013, 1.0015 | 0.3345, 0.3342, 0.3343 | −2.002 | −0.0025, −0.0021, −0.0023 |
| 0.8 | same | the two generation-2 points | 2 | 1.0041, 1.0054 | 0.2010, 0.2013 | −1.5005, −1.5006 | — |
| 1.0 | 0, e, −4.3060, 1.6448 | y₂ … y₇ (n = 2, 3, 4, 5, 7) | 1 | 0.9986–0.9996 | 0.3322–0.3330 | −1.997 … −1.999 | n = 2: −0.0003; n = 3, 4, 5, 7: **+0.011, +0.018, +0.036, +0.060** |
| 1.0 | same | L − log 6 (W = 2c₂c₃ = 0.6218) | 2 | 0.9912 | 0.1967 | −1.4953 | — |
| 1.0 | 5, o, −1.3522, 1.3787 | y₂ … y₇ | 1 | 0.9999–1.0010 | 0.3331–0.3340 | −1.999 … −2.002 | n = 2: −0.0017; others **+0.010 … +0.061** |
| 1.0, diagnostic (§3.4) | 0, e | y₂ … y₇ | 1 | 0.9993–0.9997 | 0.3329–0.3331 | −1.999 | **−0.0010 … −0.0007** |
| 1.0, diagnostic | 0, e | L − log 6 | 2 | 0.9987 | 0.1996 | −1.4995 | — |
| 1.0, diagnostic | 5, o | y₂ … y₇ | 1 | 1.0012–1.0016 | 0.3343–0.3344 | −2.002 | **−0.0040 … −0.0035** |

Notes:
- **Sign and side** are right in all 70 graded rows: κ₀ > 0, so the jump $\psi(q-r)-\psi(q+r)$ has the sign of $A$ on the source side, and |side| > 1.
- **Chain weights.** At L = 0.6, [KL] predicted odd parts $0.7683\,\ell^{-3/2}$ at y₂, $0.9943\,\ell^{-3/2}$ at y₃ and $0.4874\,\ell^{-5/2}$ at L − log 1.5. These are $c_nA$ and $c_2c_3A$ with A = 1.5676. Mine are $c_nA\kappa_0$ = 0.7682, 0.9941 and 0.4874.
- **Boosts.** K5 with the prime-power boosts β₂ = c₄ = 0.347 and β₄ = c₂²/c₄ = 0.693 is confirmed at L = 0.8 to ≤ 0.0007 in the even state and ≤ 0.0025 in the odd state.
- **Small-A states.** For |A| ≈ 0.002 (the near-zero cluster states at L = 0.8 and 1.0), fitted κ₀ is off by up to 5% and the generation-2 values are erratic. These states were not graded. This is what Theorem C's caveat allows: the remainder does not scale with A.

### 3.4 The L = 1.0 K5 failure, and the diagnosis

**Registered result.** On the registered L = 1.0 mesh, the other generation-2 points were graded only to 1e-16 (ℓ = 36.8), which lies inside the fit window [20, 63]. By §2, the kink profile at $y_n$ is fed by the zones at $y_n\pm\log m$, so it has a resolution step mid-window. The K5 offset fails for n = 3, 4, 5, 7 (not n = 2), with errors that grow with the number of coupled generation-2 points. K0′ passes on this mesh (+0.0035, +0.0047), because the edge couples only to the deep generation-1 zones.

**Sensitivity run** (registered). With those points truncated at 1e-8, below the window, the calibrated offsets are −0.0057 … +0.0034. The single-ρ "extrapolated" ones are −0.013 … −0.0006.

**Diagnostic** (post-registration, `diag_batch.sh`): every right-side generation-2 point graded like the generation-1 points (ρ = 1.5 with r_min = 1e-30; ρ = 1.35 with r_min = 1e-24).
- The raw offsets become identical for all n: −0.01424 for n = 2 and for n = 7 at ρ = 1.5.
- The ρ-extrapolated deviations are −0.0010 … −0.0007 (even state) and −0.0040 … −0.0035 (odd s = 5 state).

So K5 holds at L = 1.0 as well. The registered FAIL stands as a failure of my mesh design, not of K5.

In the diagnostic, the calibrated statistic at ρ = 1.35 (+0.0098) and the two-point K0′ extrapolation (+0.019) are not usable. That run's shorter window (ℓ ≤ 49) moves the edge D-fit by 0.003, and the extrapolation mixes two windows. At ρ = 1.5 with the full window, the calibrated statistic is +0.0033.

---

## 4. Tail law

### 4.1 Setup (registered)

**States.** Ground states of their sector at a fixed pole strength:
- even: E0 (s = 0) and Em1 (s = −1);
- odd: O5 (s = 5) and O20 (s = 20).

Their λ range from −0.9 to −10.3, and their A from 1.3 to 3.8.

Why not the true form at s = 1 with small λ? For L ≈ 0.9–1.15, the s = 1 and s = 0 spectra contain a cluster of 10+ eigenvalues in 1e-8 … 1e-4 with A ≤ 0.05. [TA] itself flags these as not edge-dominated at T ≤ 1e4. The s = 1 excited states E1 and O1 (|A| ≥ 1) were added as exploratory; they are not converged.

**Zero side.**
- $Z_k=2\sum_{T_1<\gamma\le T_2}|F(\gamma)|^2$ on the blocks [100,200], …, [6400,10300].
- Full tail $Z(T)=Q_1(f)-2\sum_{\gamma\le T}|F|^2$, exact for the discrete function by the explicit formula.
- $\tau(T)=\pi TZ(T)/|\lambda'|$. For s = 1 states this is $\pi T(1-S(T))\lambda/|\lambda'|$.

**Derivative.** λ' comes from second-order backward differences (d = 1e-3 and 2e-3, then Richardson). At X = 6, 8 and 10 a chain (2·3, 2·4 and the shift 8, 2·5) reaches the opposite edge exactly at L₀.

**Predictions.**
- $P1_k=(|\lambda'|/\pi)\int(a+\varepsilon c_X)/(t^2(a-\lambda))$; $P0_k$ is the same without $c_X$.
- $\tau_{\rm pred}=T\int_T^\infty(\cdot)$; Pred F is $1+(\lambda+\varepsilon c_X)/(\log\frac T{2\pi}+1-\lambda)$.
- $E_k=\frac1\pi\int a|F|^2$.

### 4.2 T1: second-order law (`out/tail_summary.out`)

Z/P1 by block, fine mesh:

| X | state | λ | [100,200] | [400,800] | [1600,3200] | [6400,10300] | Z/P_lead (no λ-shift), first → last block |
|---|---|---|---|---|---|---|---|
| 6 | E0 | −3.803 | 0.981 | 0.995 | 0.997 | 1.000 | 0.44 → 0.65 |
| 6 | Em1 | −7.632 | 0.975 | 0.994 | 0.993 | 0.997 | 0.28 → 0.48 |
| 6 | O20 | −4.591 | 0.886 | 0.934 | 0.967 | 0.977 | 0.36 → 0.59 |
| 6 | O5 (gate failed narrowly: \|λ'(d)/λ'(2d) − 1\| = 3.1e-3; reported only) | −0.920 | 0.869 | 0.944 | 0.972 | 0.980 | 0.67 → 0.87 |
| 8 | E0 | −4.515 | 0.951 | 0.959 | 0.982 | 0.990 | 0.42 → 0.63 |
| 8 | Em1 | −9.063 | 0.963 | 0.962 | 0.982 | 0.988 | 0.26 → 0.45 |
| 8 | O5 | −1.523 | 0.821 | 0.938 | 0.969 | 0.980 | 0.50 → 0.78 |
| 8 | O20 | −7.409 | 0.869 | 0.944 | 0.964 | 0.975 | 0.23 → 0.46 |
| 10 | E0 | −5.119 | 0.934 | 0.966 | 0.985 | 0.993 | 0.35 → 0.58 |
| 10 | Em1 | −10.263 | 0.954 | 0.972 | 0.984 | 0.990 | 0.22 → 0.41 |
| 10 | O5 | −2.097 | 0.797 | 0.914 | 0.954 | 0.968 | 0.47 → 0.75 |
| 10 | O20 | −10.205 | 0.888 | 0.932 | 0.959 | 0.971 | 0.21 → 0.40 |

**Full tail.** τ against τ_pred, for example X = 8, E0:
- τ = 0.459, 0.538, 0.602, 0.650 at T = 100, 400, 1600, 6400;
- τ_pred = 0.478, 0.554, 0.611, 0.655;
- Pred F = 0.484, 0.558, 0.614, 0.657.

In all 11 graded states, τ/τ_pred − 1 lies in [−0.069, +0.001] for T ≥ 400 and shrinks with T.

**Reading.**
- The λ-shifted edge×edge law of Prop E1(a), equivalently Pred F, describes the zero-side tail to within 9% on blocks with T₁ ≥ 400, and to within 1.8% for the even states at T ≥ 1600. The unshifted law misses by factors of 2–5.
- The remainder is always negative in Z/P1. It has the order of the heuristic kink scale Σ_{n<X} c_n²/a² ([TA] §8.3 item 1), with a state-dependent coefficient:
  - k_eff = (Z/P1 − 1)/(−Σc_n²⟨a⁻²⟩) = 0.0–0.4 for the even states and 0.6–1.0 for the odd states (`out/tail_posthoc.out`);
  - it is roughly constant in T, which is consistent with an O(a⁻²) remainder.
- The registered tolerance 2Σc_n²⟨a⁻²⟩ + 0.005 was generous: 0.19 on [400,800]. Every state is inside it by a factor of 2–10.
- **What this does and does not test.** It tests the second-order form, plus Conjecture L at the ~1/a² level, on kink-resolved eigenfunctions. Theorem C's leading law πTZ → |λ'| is not testable at T ≤ 1e4 for these λ: τ(6400) = 0.47–0.81.

**Hadamard by-product.** |λ'|/2A² = 0.996–1.010 across all 12 primary states. The 2A² edge fit there is limited by the 1e-9 generation-1 grading (§2).

### 4.3 T2: the prime-power split

Fit $S_k=\ln(Z_e/E_e)_k-\ln(Z_o/E_o)_k=\alpha\langle1/a\rangle_k+\beta\langle a^{-2}\rangle_k$ on six blocks (T₁ ≥ 200):

| X | 2c_X | (E0, O5) | (E0, O20) | (Em1, O5) | (Em1, O20) |
|---|---|---|---|---|---|
| 6 | 0 | α = −0.06 ± 0.09, β = 3.1 (O5 not graded) | α = **+0.018 ± 0.072**, β = 1.38 | (−0.07, 3.4) | α = **+0.012 ± 0.068**, β = 1.65 |
| 8 | 0.490 | α = **0.512 ± 0.067**, β = 1.9 | α = **0.658 ± 0.064**, β = −0.67 | α = **0.525 ± 0.063**, β = 2.4 | α = **0.671 ± 0.061**, β = −0.20 |
| 10 | 0 | α = 0.32 ± 0.18, β = 1.1 | α = 0.43 ± 0.18, β = −1.9 | α = 0.33 ± 0.19, β = 1.6 | α = 0.44 ± 0.19, β = −1.4 |

Block by block, the X = 8 pair (E0, O20) follows 2c₈⟨1/a⟩ almost exactly with β ≈ 0: 0.130/0.131, 0.105/0.110, 0.110/0.095, 0.096/0.084, 0.084/0.075, 0.077/0.069.

**Reading.**
- X = 8 agrees with α = 2c₈ in all four pairs. Two pairs are high by about 2.5σ, and the β terms differ by pair.
- The X = 6 control is a clean zero (|α| ≤ 0.02 ± 0.07). There β ≈ 1.4–1.7, which matches the size of [TA]'s edge×opposite-kink resonance term 2Σ_{nm=6}c_nc_m = 1.24; its sign was not derived there and is positive here.
- **The X = 10 control is not informative.** α ≈ 0.3–0.4 ± 0.18 lies between 0 and 2c₈, the fit is nearly collinear, and the block scatter is larger. "PASS" there means only "not excluded".

So the registered T2 tests pass, but at T ≤ 1e4 the 1/a split cannot be separated cleanly from the a⁻² kink-resonance terms. This repeats [TA]'s own X = 8 conclusion, now on kink-resolved vectors.

### 4.4 Post-hoc (not registered): cross-X comparison

Compare Z/P0 (no c_X term) across X for the same kind of state (`out/tail_posthoc.out`, blocks [400,800] … [6400,10300]).

| state type | X = 6 and X = 10, Z/P0 | X = 8, Z/P0 | X = 8, Z/P1 |
|---|---|---|---|
| even (E0, Em1) | 0.966–1.0003 | **1.012–1.024**; the only values clearly above 1 | 0.959–0.990, in line with the controls |
| odd (O5, O20) | 0.91–0.98 | **0.887–0.946** | 0.938–0.980, in line with the controls |

Near T ≈ 4000 the X = 8 even excess and odd deficit relative to the controls are about +0.03 and −0.03. The prediction is ±c₈⟨1/a⟩ = ±0.037. This parity-antisymmetric offset is exactly what the c_X term predicts, and it is the most direct evidence here for Prop E1(a)'s Landau term. It is post-hoc, and the states differ in λ across X.

### 4.5 Exploratory: the literal share at s = 1

These excited states are not converged (§2) and are reported only. For s = 1 states, π T (1 − S(T)) λ/|λ'|:

| state | T = 400 | 1600 | 6400 | τ_pred (6400) |
|---|---|---|---|---|
| O1, X = 8 (λ = 0.0888) | 0.962 | 0.967 | 0.970 | 0.980 |
| E1, X = 8 (λ = 0.455) | 1.198 | 1.138 | 1.108 | 1.095 |

Both move toward the prediction. The finite-difference λ' of these states carries 1–8% mesh error.

---

## 5. What this means for each write-up's predictions

**[KW] (kink, Wiener–Hopf).**
- Confirmed: (a) jump 1, cusp 1/3, side −2; (b) generation 2: 1, 1/5, −3/2; (c) the K5 offset; (d) the boosts β₂ = 0.347 and β₄ = 0.693 at L = 0.8 and 1.0; (f) the edge law with D = λ + log 2π + γ (K0′, ρ-extrapolated, +0.001 … +0.005).
- The precision now comes from an independent P1 solver with no cell-average correction; P1 has its own resolution shift, which is removed by ρ-extrapolation.
- (e) The O(1/ℓ) remainder is implicit in the stable three-term fits. It was not tested separately.

**[KL] (kink, Lévy/renewal).**
- Confirmed: the generation-1 profiles 2/3 and −1/3 (σ₀ = 1/3 and side −2 are equivalent); the generation-2 profile 3/5 and −2/5, including L − log 6 at L = 1.0 with W = 2c₂c₃; and its concrete L = 0.6 amplitudes (§3.3).
- Not tested: Lemmas T, V2 and R2. They are internal to [KL] and were checked by its referees.

**[TA] (tail, Fourier/Abelian).**
- Prop E1(a) with the λ-shift is confirmed on kink-resolved eigenfunctions at X = 6, 8, 10, T up to 1e4.
- Conjecture L is supported at the ~a⁻² level: the remainder is negative, with coefficient k_eff ∈ [0, 1] times Σc_n²/a².
- The c_X term at X = 8 is consistent (α = 0.51–0.67 against 0.49) but not separable at the registered precision. The X = 6 control is clean; the X = 10 control is uninformative.
- Item P6 (E/Z − 1 ≈ 2Σc_n²/a² ± c_X/a) has the right order of magnitude only for the odd states; for the even states E/Z − 1 is 2.5–20× smaller.
- Its "next decisive test" (kink-resolved, T up to 1e4, fit with κ₂ free) has now been run at X = 8, with controls at 6 and 10. X = 4 was not run.

**[TE] (tail, explicit formula).**
- Pred F matches the measured τ to within 7% at T ≥ 400 for all 11 graded states, at |λ| up to 10, and the gap shrinks with T.
- The split table (τ_e − τ_o ≈ 2c_X/(log(T/2π) + 1)) refers to small-λ s = 1 ground states, which are not resolvable in float64 at X = 8. My ln(Z/E) split tests the same c_X term in a normalisation-free way.
- The edge germ with b_λ = D (its (1)) is confirmed through K0′.

**Not touched:**
- the true-form ground states at L ≥ 0.6 (λ ~ 1e-6 or smaller, A ~ 1e-4), which are beyond float64 P1;
- certification of anything;
- any statement about RH.

---

## 6. Deviations from the registration, in full

1. The PREREG text says "04:30"; the md5 file records 04:27:15, which is the true registration time.
2. `kink_analyze.py` was changed after registration (md5 8404f5dc… → 87a74c8b…). The two sides of an anchor are now matched by common offsets instead of by prefix. The old code crashed on symmetric meshes, where filler nodes are stored with the left anchor; values for the right-side runs are unchanged.
3. New scripts written after registration, which only apply the registered criteria or produce tables: `kink_summary.py`, `tail_summary.py`, `kink_table.py`, `tail_posthoc.py`. §4.4 and the diagnostic (`diag_batch.sh`, §3.4) are post-registration and labelled as such.
4. The kink criterion "widen the tolerance by the mesh difference if that exceeds half the tolerance" never triggered.
5. **X = 6, O5** failed the validity gate narrowly (|λ'(d)/λ'(2d) − 1| = 3.1e-3 against 3e-3), so it is reported but not graded.

---

## 7. Credits

- **Eberwein** (Zenodo 23177438, §13) found the locations of the weak singular points, log n and L − log n.
- **mathia** (github.com/murillo128/mathia, prime_lattice, PL-306, PL-319–338) had the edge law (E) in substance.
- **The final referee** provided the anchored-offset idea and the caveat about grading at the prime images; the P0 code was not reused.
- **The four internal write-ups and their (AI) referees** supplied every predicted constant tested here.

---

## 8. Files

| File | Contents |
|---|---|
| `numerics.md` | this report |
| `PREREG.md`, `PREREG.md5` | registration, with code checksums |
| `p1weil.py` | P1 solver and gates (`python p1weil.py zeros.txt`) |
| `runlib.py` | anchors, solves, edge fits |
| `zeros_make.py`, `zeros.txt`, `zeros_check.out` | 10 500 zeros (Arb) and the mpmath cross-check |
| `pilot_L04.py`, `pilot_prof.py`, `prof_x8.py`, `xcheck.py`, `survey_tail.py`, `survey2.py`, `survey3.py` | pilots and surveys |
| `kink_run.py`, `kink_analyze.py`, `kink_conv.py`, `kink_summary.py`, `kink_table.py` | kink runs and analysis |
| `tail_run.py`, `tail_analyze.py`, `tail_summary.py`, `tail_posthoc.py` | tail runs and analysis |
| `prereg_table.py`, `prereg_table.out` | constants c_n, β_n, chain weights |
| `conv_batch.sh`, `prod_batch.sh`, `diag_batch.sh` | batch scripts (one process at a time, ulimit −v 4 GB, nice 15) |
| `out/kink_summary.out`, `out/kink_table.out` | kink verdicts and tables |
| `out/tail_summary.out`, `out/tail_posthoc.out`, `out/tail_conv.out` | tail verdicts, cross-X comparison, convergence |
| `out/*batch.log`, `out/xcheck.out` | logs (the raw `out/*.json` and `out/*.npz`, about 27 MB, are not included; the batch scripts regenerate them) |
| `out/final_md5.txt` | checksums of the final code |
