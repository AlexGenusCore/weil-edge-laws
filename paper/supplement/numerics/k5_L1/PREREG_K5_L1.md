# Pre-registration: K5 rerun at L = 1.0 with every coupled chain point graded through the fit window

Role: numerics for the weil-edge paper. Written 2026-10-31 (SAST), before any production run of this design. The md5 of this file and of every script, with the registration time, is in `PREREG_K5_L1.md5`, written right after this file was saved and before the batch was started. Float64 Galerkin numerics on [VM]. Nothing here is certified, and nothing here bears on RH.

## 0. Purpose

The original pre-registration (`scratch_archive/proof_laws/numerics/PREREG.md`, md5 `b880e0faf068419f8ec59d230f66265f`, registered 2026-10-31 04:27:15 SAST; "[NUM]") graded the K5 offset
1/ρ_n − ℓ → −D − β_n,  D = λ + log 2π + γ,  β_n = W₂⁺(y_n)/c_n,  ρ_n = J/(c_n ψ(L − r)),
at L = 0.6, 0.8 and 1.0. At L = 1.0 it **failed** on 17 of the 20 graded rows there (8 on the registered mesh, 9 on the registered sensitivity mesh). [NUM] §3.4 attributed this, after the fact, to the mesh: generation-2 chain points coupled to the measured kinks were graded only to 1e-16 (ℓ = 36.8), inside the fit window ℓ ∈ [20, 63.1].

This rerun tests that diagnosis under a registered rule. **The original FAIL stays in the record whatever this rerun gives.** A PASS here would say that K5 holds at L = 1.0 on a mesh that obeys the rule; it does not turn the original verdict into a pass.

## 1. What I had seen before writing this (honest list)

1. All of [NUM], including the 17 failing rows (table in §2) and the passing rows.
2. The post-registration diagnostic of [NUM] §3.4 (`out/k10d_r1.5.json`, `out/k10d_r1.35.json`): L = 1.0 with every right-side generation-2 point graded at (1e-30, 1.5) and at (1e-24, 1.35). Reported there: raw ρ = 1.5 offsets the same for every n (−0.01424); two-mesh extrapolated deviations −0.0010 … −0.0007 (even state) and −0.0040 … −0.0035 (odd s = 5 state), with the caveat that the two meshes had different fit windows; calibrated statistic about +0.0033 at ρ = 1.5.
   - **Consequence.** The ρ = 1.5 mesh registered below differs from that diagnostic's ρ = 1.5 mesh only by one extra graded anchor (the generation-3 point L − log(6/5), §3). Its numbers are therefore essentially already known. The new information is at ρ = 1.25 and 1.15.
3. Mesh sizes from dry runs of `k5_run.py` (mesh construction only, no solve): N = 6676 (ρ = 1.5), 11013 (1.25), 16775 (1.15).
4. The wrapper `k5_summary.py` was smoke-tested on the already-seen diagnostic file `k10d_r1.5.json`, only to check that it runs.

## 2. Cases

**Graded states** (same rule as [NUM]: |A| ≥ 0.2; at L = 1.0 these are two states):
- E: s = 0, even, λ ≈ −4.30605, A ≈ 1.645;
- O: s = 5, odd, λ ≈ −1.35219, A ≈ 1.379.

The near-zero cluster states (λ ~ 1e-7, |A| ~ 1e-3) are computed and reported but not graded, as in [NUM].

**The 17 registered failing rows** (from `numerics/out/kink_summary.out`; "dev" = ρ-extrapolated b0 + D + β_n; "cal" = b0 + D_fit + β_n at each ρ; tolerance 0.005 for both):

| # | mesh in [NUM] | state | n (β_n) | dev | cal by ρ |
|---|---|---|---|---|---|
| 1 | registered (ρ 1.5, 1.25; gen-2 at 1e-16) | E | 7 (0) | +0.05963 | +0.06425, +0.06348 |
| 2 | registered | E | 5 (0) | +0.03546 | +0.03963, +0.03917 |
| 3 | registered | E | 4 (0.693147) | +0.01832 | +0.02216, +0.02193 |
| 4 | registered | E | 3 (0) | +0.01105 | +0.01477, +0.01462 |
| 5 | registered | O | 7 | +0.06089 | +0.06681, +0.06595 |
| 6 | registered | O | 5 | +0.03572 | +0.04114, +0.04063 |
| 7 | registered | O | 4 | +0.01759 | +0.02264, +0.02238 |
| 8 | registered | O | 3 | +0.01022 | +0.01513, +0.01497 |
| 9 | sensitivity (ρ 1.25 only; gen-2 at 1e-8) | E | 7 | −0.01380 | −0.00565 |
| 10 | sensitivity | E | 5 | −0.01002 | −0.00188 |
| 11 | sensitivity | E | 4 | −0.00726 | +0.00088 |
| 12 | sensitivity | E | 3 | −0.00634 | +0.00180 |
| 13 | sensitivity | O | 7 | −0.01716 | −0.00776 |
| 14 | sensitivity | O | 5 | −0.01252 | −0.00311 |
| 15 | sensitivity | O | 4 | −0.00945 | −0.00005 |
| 16 | sensitivity | O | 3 | −0.00806 | +0.00134 |
| 17 | sensitivity | O | 2 (0.346574) | −0.00619 | +0.00321 |

(On the sensitivity mesh "dev" is the single-ρ raw value; no extrapolation was possible.)

**Other L = 1.0 rows in [NUM]:** K5 PASS for n = 2 on the registered mesh (E −0.00029, O −0.00168) and for E, n = 2 on the sensitivity mesh (−0.00476); K0′ PASS 10/10 on the registered mesh and FAIL 10/10 on the sensitivity mesh; generation-1 κ₀, σ₀, side and sign PASS 20/20; generation 2 at L − log 6 (W = 2c₂c₃ = 0.621762) PASS 4/4.

**Rows of this rerun.** Every one of the above is one of these cases, recomputed on the new meshes:
- K5 and K0′: 2 states × 5 generation-1 points (n = 2, 3, 4, 5, 7) = 10 graded rows each;
- K1 (κ₀, σ₀, side, sign): the same 10 rows;
- K2 (κ₀, σ₀, side, sign) at L − log 6: 2 graded rows.

## 3. Mesh rule (the only change from the registered L = 1.0 design)

**Rule.** Every chain point coupled to a measured point by one prime-power shift log m (m < X = e² ≈ 7.389, so m ∈ {2, 3, 4, 5, 7}) is graded exactly like the measured points: geometric zones r_j = r_min ρ^j on both sides with the same (r_min, ρ). So no coupled zone is truncated inside the fit window.

**Measured points:** the right edge +L; every right-side generation-1 point y_n = L − log n (n = 2, 3, 4, 5, 7); and L − log 6.

**Resulting graded set** (from the dry run; `k5_run.py` prints it in every log): −0.945910, −0.791759, −0.609438, −0.386294, −0.252763, −0.098612, +0.083709, +0.152702, +0.306853, +0.440384, +0.489174, +0.594535, +0.663528, +0.712318, +0.776856, +0.817678, and the edge +1.
- This is every right-side generation-1 and generation-2 point, plus the generation-3 point L − log(6/5) = +0.817678, which is coupled to L − log 6 by log 5.
- No coupled point lands on a left-side (mirror) chain point or on −L, because X is not rational.

**Unchanged from the registered L = 1.0 runs:** H = L/40; r_min = 1e-30 at every graded zone; left edge (1e-12, 1.5); mirror chain points (1e-10, 1.6); right side measured only (`mirror = 0`); s = 0 and 5; k = 3 lowest states per s.
- With r_min = 1e-30 at every graded zone and every ρ, the fit window is the same, ℓ ∈ [20, 63.08], on every mesh. This avoids the mixed-window defect of the ρ = 1.35 diagnostic.

**Meshes:**
- **primary:** ρ = 1.5 and 1.25, the ρ set registered for L = 1.0 in [NUM];
- **supplementary:** ρ = 1.15 in addition, as was done at L = 0.6 and 0.8.

## 4. Pass criteria (unchanged from [NUM] §2, as implemented)

The verdicts are computed by `kink_summary.main()` (md5 `f62e6b7780186ff35d925b9d2ba8cd1f`) and `kink_analyze.analyse()` (md5 `87a74c8b1d528caf845383d8825f3759`), both unchanged. `k5_summary.py` only points them at the new files. They are applied to the window ℓ ∈ [20, ℓ_max − 6].

| ID | Pass if |
|---|---|
| K5 (per graded generation-1 row) | ρ-extrapolated \|b0 + D + β_n\| ≤ 0.005 **and** calibration-free \|b0 + D_fit + β_n\| ≤ 0.005 at every ρ in the set |
| K0′ | ρ-extrapolated \|D_fit − D\| ≤ 0.005 |
| K1 | \|κ0 − 1\| ≤ 0.005, \|σ0 − 1/3\| ≤ 0.003, \|side0 + 2\| ≤ 0.015, κ0 > 0 and \|side0\| > 1 |
| K2 (L − log 6) | \|κ0 − 1\| ≤ 0.01, \|σ0 − 0.2\| ≤ 0.004, \|side0 + 1.5\| ≤ 0.015, sign as K1 |

- ρ-extrapolation: least squares v = v∞ + c (log ρ)² over the meshes in the set.
- As in [NUM]'s code, a K1/K2 tolerance is widened by the mesh spread when that spread exceeds half the tolerance; this is reported if it triggers. It is not applied to K5 or K0′.

**Primary verdict:** the meshes ρ ∈ {1.5, 1.25}.

**Supplementary verdict:** ρ ∈ {1.5, 1.25, 1.15}. The extrapolation then uses three meshes, and the calibrated statistic must also pass at ρ = 1.15.

**What counts as resolving the FAIL.**
- The registered L = 1.0 K5 FAIL counts as resolved by this rerun **only if all 10 graded K5 rows pass in the primary verdict and, if ρ = 1.15 completes, also in the supplementary verdict**.
- Anything less is reported row by row. K5 at L = 1.0 is then described as not confirmed by the numerics.

**Limits, fixed in advance.**
- One process at a time; 3 BLAS threads; `ulimit -v` 12 GB; nice 10; timeout 3 h per run (`k5_batch.sh`).
- If the ρ = 1.15 run fails for memory or time, it is reported as "not run (resource limit)". The supplementary verdict is then absent; the primary verdict stands alone, and this is said.
- If ρ = 1.25 does not complete, there is no verdict. That is reported, not replaced by a single-ρ value.
- If the graded states are not found as in §2 (different λ or |A| < 0.2), this is reported, and the rows are graded under the |A| ≥ 0.2 rule as written.

## 5. Code

All of the following are in this folder and on [VM] in `[workdir]/`; md5 values are in `PREREG_K5_L1.md5`.
- `p1weil.py`, `runlib.py`, `kink_analyze.py`, `kink_summary.py`: copied unchanged from [NUM]. Their md5 values match `numerics/out/final_md5.txt`.
- `kink_run.py`: copied for reference only; not used.
- `k5_run.py` (new): the driver. It is `kink_run.py` with `mirror = 0` plus the rule of §3, and it writes the same JSON format.
- `k5_summary.py` (new): runs `kink_summary.main()` on given file patterns.
- `k5_batch.sh` (new): the batch.

Any change after registration will be listed, with its reason and a new md5.
