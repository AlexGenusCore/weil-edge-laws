# Pre-registration: independent numerical test of the kink-law and tail-law constants

Role: `numerics`. Registered 2026-10-31 04:30 SAST, before any production run. The md5 of this file is recorded in `PREREG.md5`, written right after this file was saved.

## 0. Method, and what I had already seen

**Solver.** `p1weil.py` is new code. It shares only the form definition with the project's solvers and with the final referee's P0 code.
- Method: continuous piecewise-linear (P1) Galerkin.
- Nodes are stored as (anchor, offset), so meshes can be graded geometrically down to offsets of 1e-40.
- The jump form is assembled element pair by element pair, with closed forms for the 1/(2u) part.
- Prime shifts use exact hat overlaps. The pole enters as a rank-2 term.

**Gates, all passed before registration (`p1weil.py`, `selfcheck`).**
- E_J agrees with an independent autocorrelation formula to ≤ 1.1e-9.
- R_f(log n) and the pole term agree with fine-grid quadrature to ≤ 6e-11.
- The whole form at s = 1 satisfies Weil's explicit formula with 10 500 zeta zeros: Q_1(f) = 2 Σ|F(γ)|² to 2e-10 – 1.1e-9, which equals the estimated tail, at L = 0.45, 0.9 and 1.15.
- At L = 0.4 it reproduces the referee's P0 values: λ_e = −1.5400, A_e = 1.5694 (referee 1.5696), A_o = 0.4508 (0.4510), s = 1 A_e = 0.0620 (0.0621).

**Zeros.** Arb (python-flint `acb.zeta_zeros`, 30 digits), n = 1 … 10 500, with γ ≤ 10 303.2.
- Cross-checked against `mpmath.zetazero` (dps 30) at 259 indices (1–50, then every 50th). The largest difference is 4.7e-26 (`zeros_check.out`).

**Seen before registration** (honest list):
1. Kink smoke and convergence runs at L = 0.6, s = 0, right side, n = 2, 3 and L − log 1.5. These printed the fitted constants next to the predictions; the values are in `out/kconv_*.json`.
2. Hadamard-type comparisons λ' versus 2A² at X = 8 (`out/tconv_*.npz`, `conv_batch.log`).

**Not seen before registration.** No tail statistic (Z/P, Z/E, sector split, τ) was compared with any prediction. `tail_analyze.py conv` prints mesh-to-mesh differences only.

## 1. Convergence study (basis for the tolerances)

**Kink, L = 0.6, s = 0** (`kink_conv.py`). Meshes: grading ratio ρ = 1.5, 1.25, 1.15 with r_min = 1e-40, and H = L/40 versus L/80. Fit window ℓ ∈ [20, ℓ_max − 6].

| state | quantity | \|ρ1.25 − ρ1.15\| | \|H/40 − H/80\| | fit window ℓ ≥ 12 vs ≥ 20 |
|---|---|---|---|---|
| e0 (A = 1.567) | jump κ0, cusp σ0, side ratio | ≤ 1e-5 | ≤ 1e-9 | ≤ 4e-4 |
| o0 (A = 0.26) | κ0, σ0 | ≤ 2.5e-5 | ≤ 2e-9 | ≤ 8e-3 |
| generation 2 | κ0, σ0, side ratio | ≤ 9e-5 | ≤ 3e-9 | ≤ 3e-2 (A = 0.26) |

The edge offset D_fit and the K5 offset b0 carry a P1 resolution shift. It follows δ = δ∞ + c (log ρ)² with c ≈ ±0.084: the extrapolations from (1.5, 1.25) and from (1.25, 1.15) agree to 2e-5. The calibration-free combination b0 + D_fit is mesh-independent to 1e-4.

Lesson learned: every generation-1 point coupled to the edge being fitted, and generation-2 points coupled to a tested kink, must be graded at least as deep as the fit window. Otherwise the profile shows a feature at the truncation depth (`out/xcheck.out`).

**Tail, X = 8** (`out/tail_conv.out`).
- For the ground states E0 (s = 0) and O5 (s = 5), the base mesh (N = 2777) and the fine mesh (N = 4209) agree to:
  - 1.3e-4 in every block sum Z_k and E_k;
  - 1e-4 in λ';
  - 1e-6 in A.
- Without generation-2 grading the block sums change by up to 5e-3.
- The excited s = 1 states E1 and O1 are **not** converged: up to 5% in blocks and up to 8% in λ'. E1 also shows strong curvature, with λ'(d) and λ'(2d) differing by 1–6%.

## 2. Kink law: predictions and pass criteria

**Source:** attempts kink-wienerhopf and kink-levy (repairs), Theorems K1, K2, K5, K0′.

**Notation.**
- At a generation-k point q reached from the right edge, with chain weight W:
  - J(r) = ψ(q − r) − ψ(q + r);
  - Σ(r) = ψ(q − r) + ψ(q + r) − 2ψ(q);
  - side ratio = [ψ(q − r) − ψ(q)] / [ψ(q + r) − ψ(q)].
- At mirror points, swap the sides and use A_−.
- Fits are on ℓ ∈ [20, ℓ_max − 6], with three-term expansions in 1/ℓ:
  - J ℓ^{k+1/2}/(W A) = κ0 + κ1/ℓ + κ2/ℓ²;
  - ψ(q − r) + ψ(q + r) = 2ψ(q) + W A ℓ^{−k−1/2}(σ0 + σ1/ℓ + σ2/ℓ²), with ψ(q) fitted. The P1 node value at q is truncated by r_min and is not used.
  - side0 = (κ0 + σ0)/(σ0 − κ0).
- A is the edge trace from ψ(L − r)^{−2} = a0 ℓ + a1 + a2/ℓ + a3/ℓ², on the same window; D_fit = −a1/a0.

**Graded states:** |A| ≥ 0.2. Others are reported only, because of Theorem C's caveat that the remainder does not scale with A.

| ID | Prediction | Pass if |
|---|---|---|
| K1-κ | generation 1: κ0 = 1, with κ0 > 0, i.e. the jump has the sign of A on the source side | \|κ0 − 1\| ≤ 0.005 |
| K1-σ | generation 1: σ0 = 1/3 | \|σ0 − 1/3\| ≤ 0.003 |
| K1-side | generation 1: side ratio −2; the larger excursion is on the source side | \|side0 + 2\| ≤ 0.015 |
| K2 | generation 2 (L − log 1.5 at L = 0.6, 0.8; L − log(4/3) at L = 0.8; L − log 6 at L = 1.0, W = 2c₂c₃ = 0.621762): κ0 = 1, σ0 = 1/5, side ratio −3/2 | \|κ0 − 1\| ≤ 0.01, \|σ0 − 0.2\| ≤ 0.004, \|side0 + 1.5\| ≤ 0.015 |
| K5 | 1/ρ_n − ℓ → −D − β_n, where D = λ + log 2π + γ, β_n = W₂⁺(y_n)/c_n (L = 0.8 and 1.0: β₂ = 0.346574, β₃ = 0, β₄ = 0.693147), and ρ_n = J/(c_n ψ(L − r)) | ρ-extrapolated \|b0 + D + β_n\| ≤ 0.005, **and** calibration-free \|b0 + D_fit + β_n\| ≤ 0.005 at every ρ |
| K0′ | D_fit = λ + log 2π + γ | ρ-extrapolated \|D_fit − D\| ≤ 0.005 |

**Tolerance rationale.** Each tolerance is at least 10× the largest mesh effect seen at L = 0.6 for |A| ≥ 0.2. It also covers the fit-window effect seen with ℓ ≥ 20.

**Additional rule for L = 0.8 and 1.0.** If two meshes of the same L differ by more than half the tolerance, the tolerance is widened by that difference, and this is reported.

**Runs** (`prod_batch.sh`):
- L = 0.6:
  - right side, ρ = 1.5, 1.25, 1.15, r_min = 1e-40;
  - symmetric mesh (mirror points), ρ = 1.5 and 1.25.
- L = 0.8: right side, deep at all generation-1 points and at L − log 1.5 and L − log(4/3); ρ = 1.5, 1.25, 1.15; r_min = 1e-30.
- L = 1.0: right side, deep at all generation-1 points and at L − log 6; other generation-2 points at (1e-16, 1.6); ρ = 1.5 and 1.25; r_min = 1e-30. A sensitivity run has the other generation-2 points at (1e-8, 2).
- States: s = 0 (k = 3) and s = 5 (k = 3).

## 3. Tail law: predictions and pass criteria

**Source:** attempts tail-abelian (Prop E1, Conj. L, §8.3) and tail-explicit (Pred F).

**States** (rule fixed now; `tail_run.py`):
- primary, ground states of their sector at fixed pole strength:
  - E0 (s = 0, even), Em1 (s = −1, even);
  - O5 (s = 5, odd), O20 (s = 20, odd);
- exploratory: E1, O1, the lowest s = 1 even and odd states with |A| ≥ 1. These are not converged (§1) and not graded.

**Runs.** Fine mesh at X = 6, 8, 10: generation 1 at (1e-9, 1.15), generation 2 at (1e-8, 1.5), H = L/120, edges at (1e-40, 1.25). Base mesh at X = 6, 8, 10 as the convergence check.
- λ' comes from second-order **backward** differences with d = 1e-3 and 2d, then Richardson.
- Backward differences are used because at X = 6, 8, 10 a chain or shift (2·3, 2·4 and 8, 2·5) reaches the opposite edge exactly at L0.

**Quantities.** All use zeros γ ≤ 10 303.
- Z_k = 2 Σ_{T1<γ≤T2} |F(γ)|² on the blocks [100,200], [200,400], …, [3200,6400], [6400,10300].
- E_k = (1/π) ∫ a |F|².
- Full tail Z(T) = Q₁(f) − 2 Σ_{γ≤T} |F(γ)|². By the explicit formula, this is the tail of the zero sum of the discrete eigenfunction.
- τ(T) = π T Z(T)/|λ'|. For the s = 1 states this is π T (1 − S(T)) λ/|λ'|.
- Predictions, with ε = +1 for even states and −1 for odd states:
  - P1_k = (|λ'|/π) ∫ (a + ε c_X)/(t²(a − λ)) (Prop E1(a));
  - P0_k without the c_X term;
  - τ_pred(T) = T ∫_T^∞ (a + ε c_X)/(t²(a − λ)), which equals Pred F, 1 + (λ + ε c_X)/(log(T/2π) + 1 − λ), up to O(a⁻²);
  - c₈ = 0.245065, c₆ = c₁₀ = 0;
  - kink scale Σ_{n<X} c_n² = 1.2807 (X = 6), 1.8217 (X = 8), 2.0158 (X = 10).

**Validity gate** for a primary state; the state is reported but not graded if it fails:
- |λ'(d)/λ'(2d) − 1| ≤ 3e-3;
- fine-versus-base block differences ≤ 3e-3 for T1 ≥ 200.

| ID | Prediction | Pass if |
|---|---|---|
| T1 | second-order edge law (Prop E1 + Conj. L; kink terms of order Σc_n²/a²) | for every block with T1 ≥ 400: \|Z_k/P1_k − 1\| ≤ 2 Σ_{n<X} c_n² ⟨a⁻²⟩_k + 0.005 |
| T1-full | the same for the full tail | for T ∈ {400, …, 6400}: \|τ(T)/τ_pred(T) − 1\| ≤ 2 Σ c_n²/a(T)² + 0.005 |
| T1-λ | the λ-shift is present | the alternative without it, 1 + ε c_X/a, must fail the T1 criterion for the states with \|λ\| ≥ 1 |
| T2 | sector split at prime-power X | see below |
| T3 | leading law (Thm C / Cor D): τ → 1 with an additive error O(1/log T) | asymptotic only; not gradable at T ≤ 1e4; report τ(T) |

**T2, the sector split.** For each pair (even primary, odd primary):
- S_k = ln(Z_e/E_e)_k − ln(Z_o/E_o)_k on the blocks with T1 ≥ 200;
- fit S_k = α⟨1/a⟩_k + β⟨a⁻²⟩_k.

| | Pass if |
|---|---|
| X = 8 | \|α − 2c₈\| ≤ max(0.10, 3σ_α), with 2c₈ = 0.490129 |
| X = 6, 10 (controls) | \|α\| ≤ max(0.10, 3σ_α) |

I also report the β = 0 comparison S_k versus 2c_X⟨1/a⟩_k block by block, and E_k/P0_k, where Prop E1(c) predicts no c_X term.

**Reported only, not graded:**
- the P6 heuristic E/Z − 1 ≈ 2Σc_n²/a² + εc_X/a;
- the tail-explicit split table (τ_e − τ_o ≈ 2c_X/(log(T/2π) + 1));
- the Hadamard ratio |λ'|/2A², whose edge fit is limited by the 1e-9 grading at generation 1.

## 4. Reporting

- Every graded item is reported as PASS or FAIL against the tolerance above.
- Any change to code after registration will be listed with the reason and a new md5.
