# Numerics for the weil-edge paper: consolidated evidence, one new pre-registered rerun, one figure

*Folder `papers/weil-edge/numerics/`, 2026-10-31. Author of the paper: Johann Alexander Botha (GenusCore, info@genuscore.com). Everything here is uncertified float64 Galerkin numerics, written and checked with AI assistance and reviewed so far only by internal AI referees; no human expert has checked the code or the numbers. Nothing here is a statement about the Riemann hypothesis, for or against.*

## 0. Summary

| Item | Result | Status |
|---|---|---|
| Constant 2 in (H), $-\lambda'/(2A^2)=1$ | independent P0 code, 13 cases: within $3\cdot10^{-3}$ (base meshes), within $6\cdot10^{-4}$ after refinement; P1: $0.9960$–$1.0097$ over 12 states | supports $\kappa=1$; the exact identities N1–N5 cannot detect a wrong constant |
| Kink, generation 1: jump $1$, split $\frac23:-\frac13$ | $\kappa_0=0.9986$–$1.0019$, $\sigma_0=0.3322$–$0.3346$, side $-1.9969$ to $-2.0035$; systematic band $\le0.002$ for $\kappa_0,\sigma_0$ ($\le0.0043$ on the $L=1.0$ sensitivity mesh), $\le0.0053$ for the side ratio | registered PASS 50/50 |
| Kink, generation 2: $\frac35:-\frac25$ | $\kappa_0=0.9912$–$1.0054$, $\sigma_0=0.1967$–$0.2018$ | registered PASS 20/20 |
| Jump-ratio offset with boosts (K6; registered "K5") | $L=0.6,0.8$: deviation $-0.0025$ to $-0.0005$ (band $\le0.006$) | registered PASS |
| same, $L=1.0$, registered meshes | $+0.010$ … $+0.061$ / $-0.017$ … $-0.006$ | **registered FAIL, 17 of 20 rows; stays in the record** |
| same, $L=1.0$, **new pre-registered rerun** (every coupled chain point graded through the fit window) | $-0.0019$ … $-0.0003$ (band $\le0.003$); calibrated $\le0.0035$ | **PASS 10/10** (primary and supplementary) |
| Edge offset $D=\lambda+\log2\pi+\gamma$ (K1; registered "K0′") | $+0.0013$ to $+0.0049$ on the registered main meshes; rerun $+0.0039$ (even), $+0.0051$ (odd) | registered PASS 40/50 (10 fails: $L=1.0$ sensitivity mesh); **rerun: odd state FAILS by $1\cdot10^{-4}$** |
| Tail law, second order, $\lambda$-shifted (T4 / Pred. F) | $Z/P_1=0.80$–$1.00$; $-8.7\%$ to $+0.03\%$ for $T\ge400$; without the shift $0.20$–$0.87$ | registered PASS 11/11 (generous tolerance) |
| $c_X$ term | $X=2,3$: $0.968$–$1.014$ with it, $0.86$–$0.91$ / $1.09$–$1.13$ without; $X=4$ even: $0.989$–$0.994$ vs $1.06$–$1.10$; $X=8$: $\alpha=0.51$–$0.67$ vs $0.490$; control $X=6$: $\alpha=0.02\pm0.07$; $X=10$ uninformative | supported, not established; not cleanly separated at $X=8$ |

## 1. Sources

All numbers except those of §5 and the error bands of §4 are copied from earlier internal work. Paths are relative to `weil-mechanism/scratch_archive/proof_laws/`.

- **[NUM]** `numerics/`: the independent P1 solver (`p1weil.py`) and its pre-registration (`PREREG.md`, md5 `b880e0faf068419f8ec59d230f66265f`, registered 2026-10-31 04:27:15 SAST), results in `numerics.md`, `out/kink_summary.out`, `out/kink_table.out`, `out/tail_summary.out`, `out/tail_posthoc.out`, `out/tail_conv.out`.
  - Gates before registration: Weil's explicit formula against 10 500 zeta zeros (Arb, 30 digits; cross-checked against mpmath at 259 indices to $4.7\cdot10^{-26}$) to the size of the estimated tail, $2\cdot10^{-10}$–$1.1\cdot10^{-9}$; an independent position-side formula for the jump form; the referee's $L=0.4$ values.
- **[N]** `note-v2/note_v2.md` §13 and §13.1, `note-v2/evidence.out`: the (E)/(H) evidence, including the final internal referee's independent P0 code (`proof_EH/final-referee/`).
- **ref1-TE** `referee1-tail-explicit/zero_side_split.out`: zero-side $c_X$ test at $X=2,3$ and the $L=0.4$ control (P0 eigenfunctions, zeros 1–1500).
- **TA / ref2-TA** `repair-tail-abelian/split_x4_check.out`, `referee2-tail-abelian/mesh_x4_check.out`, `report_recovered.md`: the $X=4$ test and its caveats.
- **[S]** `synthesis/laws_note.md` §6 and **[FR]** `final-referee/final_referee_report.md`: statement labels and must-fix items.

**Statement labels.** The tables use the synthesis labels; the pre-registration used the route labels.

| synthesis [S] | registered [NUM] | statement |
|---|---|---|
| K1 | K0′ | edge law to second order, $\psi(L-r)=A(\ell-D)^{-1/2}+O(\ell^{-5/2})$, $D=\lambda+\log2\pi+\gamma$ |
| K3 ($k=1$, $k=2$) | K1, K2 | first-order kink profile: split $\frac{k+1}{2k+1}:-\frac{k}{2k+1}$, jump coefficient 1, chain weight $W$ |
| K6 | K5 | jump ratio $1/\rho_n=\ell-D-\beta_n+O(1/\ell)$ with prime-power boosts. [FR]: proved for exact point values; the reading for Galerkin traces is heuristic |
| K7 | — | second-order even part: **a conjecture** ([FR]); not tested here |
| T4 / Pred. F | T1, T1-full, T1-$\lambda$ | $\lambda$-shifted second-order sharp tail law. The full sharp law also needs Conjecture L (open), so the numerics test it only at the $a^{-2}$ level |
| (part of T4) | T2 | sector split $2c_X$ |
| T2 | T3 | first-order law $\pi TZ\to|\lambda'|$; asymptotic, not gradable at $T\le10^4$ |

**Scope.** The laws are asymptotic. They are vacuous where $A=0$, and the kink law is tested only on states with $|A|\ge0.2$. The true-form ground states at $L\ge0.6$ ($A\le10^{-4}$, $\lambda\le10^{-6}$) are beyond float64 and are not tested. The tail tests use large-$|\lambda|$ states (pole strengths $s=-1,0,5,20$), not the true $s=1$ form at small $\lambda$.

## 2. Which checks can detect a wrong constant

Table `tab_detect.tex`. The logic, from [N] §13.1 and [FR]:

- Suppose the layer integral of Lemma 8.3 were $\kappa A^{(1)}A^{(2)}\delta$ instead of $A^{(1)}A^{(2)}\delta$.
  - The exact cross identity (N1, N2) still holds, since no edge trace appears in it.
  - The edge-free identity (N3) still holds, since both sides scale by $\kappa^2$.
  - The pure-log mixed identity (N4) and Theorem 4 still hold: $A^2=1/(2\kappa L)$, and the mixed identity reads $2\kappa A_eA_o$.
  - The sector ratio (N5) still holds.
- **Only an absolute $A$ compared with $\lambda'$ sees $\kappa$.** Those checks are in `tab_H.tex`: the independent P0 code gives $\kappa=1$ to $3\cdot10^{-3}$ (base meshes) and $6\cdot10^{-4}$ (refined, where run). So $\kappa=\sqrt2$ or $2$ is excluded by orders of magnitude.
- **Kink.**
  - $\kappa_0$ sees the jump constant to about 0.2% (0.4% on the worst mesh).
  - $\sigma_0$ sees the split: a one-sided germ would give $\sigma_0=1$ and a purely odd one $\sigma_0=0$; measured $0.3322$–$0.3346$.
  - The K6 offset resolves the boosts $\beta_2=0.347$ and $\beta_4=0.693$ to about $\pm0.003$.
- **Tail.**
  - T1 sees the $\lambda$-shift (factor 2–5) but cannot see a constant error below about 10% at $T\le10^4$, because the unmodelled $O(a^{-2})$ remainder is that large.
  - The $c_X$ tests fix the coefficient of $c_X$ only to about $\pm30\%$, though they exclude its absence and its wrong sign.

## 3. (E) and (H): absolute checks of the constant

Table `tab_H.tex`, copied from [N] §13.1 and `note-v2/evidence.out`; the P1 row is from [NUM] `out/tail_summary.out`.

- **P0** is the final internal referee's piecewise-constant Galerkin code. It shares no code, discretisation or fitting with the project's hp-FEM.
  - Edge mesh down to $r=10^{-150}$; $A$ fitted on $\ell\in[30,345]$ and extrapolated in the grading ratio; $\lambda'$ by central differences.
- **Error bars.** The base-to-refined change is the honest uncertainty: $3.8\cdot10^{-4}$ to $2.2\cdot10^{-3}$, the largest for $L=0.6$ odd, the weakest entry. The refinement column assumes smooth, additive mesh errors.
- **Prime-image bias.** Fitted amplitudes with active primes carry an extra 0.15–0.3% bias unless the mesh is graded at $\pm(L-\log n)$ ([N] §13.1, `zone_test.out`). This affects N5, N9 and the P1 tail-state ratios (graded only to $10^{-9}$ at generation 1).
- **Pure log.** The pure-log case ($A^2=1/(2L)$, simplicity) belongs to the companion paper (*Boundary trace and simplicity of the Dirichlet spectrum of the logarithmic Laplacian on an interval*, same author, not yet public); it is listed only as one of the absolute checks and is not repeated.
- **Edge law (E) itself.**
  - Tested through the second-order offset K1 ($D_{\rm fit}-D$, `tab_k0.tex`) and through the explicit formula of Theorem 1(3) (N7: $A_{\rm pred}=0.57290615$ against the edge fit to $(1$–$3)\cdot10^{-5}$ at $L=0.4$, for the archimedean torsion function).
  - $D_{\rm fit}-D$ is positive in every row ($+0.0013$ … $+0.0049$ on the registered main meshes). A small systematic offset of the fit model of that size cannot be excluded; it is of the size of the fit-window band.

## 4. Kink law: tables and error bars

Tables `tab_kink_gen1.tex`, `tab_kink_gen2.tex`, `tab_k5.tex`, `tab_k0.tex` are generated by `make_tables.py` from `kink_errors.json`. That file is written by `consolidate_kink.py`, which calls the registered analysis code `kink_analyze.py` unchanged.

**Error bands (post hoc; they do not change any verdict).** For every graded row:
- the **mesh** term is the spread over the grading ratios ρ of the group. For K6 and K1 with three gradings, it is the spread between the extrapolations from (1.5, 1.25) and (1.25, 1.15); with two gradings the extrapolation is exactly determined and has no internal check, which is flagged;
- the **window** term is the change when the fit window starts at ℓ = 15 or 25 instead of the registered 20;
- the **band** is mesh + window. It is a systematic band, not a standard deviation.

What the bands show:
- They are $\le2\cdot10^{-4}$ for the large-$A$ even states.
- They reach $2\cdot10^{-3}$ for the odd states.
- They reach $6\cdot10^{-3}$ for the K6 offset of the small-$A$ ($0.26$) odd state at $L=0.6$, which is about the size of the 0.005 tolerance. That row passed, but it does not test K6 at the 0.005 level.
- On the registered $L=1.0$ meshes the window term is large ($0.007$–$0.04$), which is the signature of the mid-window grading step diagnosed in [NUM] §3.4.

Key numbers (finest grading):

| $L$ | state | gen-1 $\kappa_0$ | $\sigma_0$ | side | K6 dev | K1 $D_{\rm fit}-D$ |
|---|---|---|---|---|---|---|
| 0.6 | $s=0$ even, $A=1.567$ | $1.0001\pm0.0002$ | $0.3334\pm0.0001$ | $-2.0003\pm0.0003$ | $-0.0005\pm0.0006$ | $+0.0013\pm0.0008$ |
| 0.6 | $s=0$ odd, $A=0.261$ | $1.0014\pm0.0019$ | $0.3346\pm0.0016$ | $-2.0035\pm0.0047$ | $-0.0018\pm0.0062$ | $+0.0025\pm0.0015$ |
| 0.8 | $s=0$ even, $A=1.425$ | $1.0000$–$1.0001\pm0.0002$ | $0.3334\pm0.0001$ | $-2.0003\pm0.0002$ | $-0.0007$ … $-0.0005\pm0.0007$ | $+0.0033\pm0.0037$ |
| 0.8 | $s=5$ odd, $A=1.437$ | $1.0013$–$1.0019\pm0.0019$ | $0.3342$–$0.3345\pm0.0013$ | $-2.002\pm0.003$ | $-0.0025$ … $-0.0021\pm0.0032$ | $+0.0049\pm0.0029$ |
| 1.0 | $s=0$ even, $A=1.645$ (reg. mesh) | $0.9986$–$0.9996\pm0.0012$ | $0.3322$–$0.3330$ | $-1.999$ … $-1.997$ | **$+0.011$ … $+0.060$ (FAIL, $n\ne2$)** | $+0.0035\pm0.0031$ |
| 1.0 | $s=5$ odd, $A=1.379$ (reg. mesh) | $1.0000$–$1.0010\pm0.0011$ | $0.3331$–$0.3340$ | $-2.002$ … $-1.999$ | **$+0.010$ … $+0.061$ (FAIL, $n\ne2$)** | $+0.0047\pm0.0025$ |

The boosts: at $L=0.8$, $\beta_2=c_4=0.347$ and $\beta_4=c_2^2/c_4=0.693$ are confirmed to $\le0.003$. At $L=0.6$ the prime power 4 is not active ($X=3.32$), so every boost is $0$ there ([FR] item 6).

## 5. New pre-registered rerun: K6 ("K5") at $L=1.0$

**Registration.** `k5_L1/PREREG_K5_L1.md`, md5 `695c14d574e320147e112383f86b1262`, registered 2026-10-31 06:31:23 SAST.
- `PREREG_K5_L1.md5` holds the md5 of every script and was written before anything ran.
- All checksums were verified on [VM] at 06:31:24. The batch started at 06:31:26 (`k5_batch.log`).

**What was already seen.** The prereg lists it, and the most important item bears repeating: the post-registration diagnostic of [NUM] had already run the $\rho=1.5$ member of this design (minus one generation-3 anchor). So the new information is at $\rho=1.25$ and $1.15$.

**Rule (the only change from the registered $L=1.0$ design).**
- Every chain point coupled to a measured point by one prime-power shift $\log m$, $m<X=e^2$, is graded with the measured points' $(r_{\min},\rho)=(10^{-30},\rho)$.
- The measured points are the edge, all $y_n$, and $L-\log6$.
- So 16 interior points are graded: every right-side generation-1 and generation-2 point, plus $L-\log\frac65$.
- The fit window is $[20,63.08]$ on every mesh.

**Cases.**
- The 17 registered failing rows: 8 on the registered mesh, 9 on the sensitivity mesh.
- All other $L=1.0$ rows: K6 at $n=2$, K1, generation-1 K3, generation-2 K3 at $L-\log6$.
- Together they make 10 graded K6 rows: 2 states × $n\in\{2,3,4,5,7\}$.

**Runs** ([VM]; 3 BLAS threads, `ulimit -v` 12 GB, nice 10, one process at a time):

| $\rho$ | $N$ | wall | max RSS | residuals |
|---|---|---|---|---|
| 1.5 | 6676 | 96 s | 1.8 GB | $\le6\cdot10^{-13}$ |
| 1.25 | 11013 | 335 s | 4.9 GB | $\le1.7\cdot10^{-12}$ |
| 1.15 | 16775 | 1125 s | 11.1 GB | $\le10^{-12}$ |

The graded states were found as registered:
- $s=0$ even: $\lambda=-4.306045$, $A=1.6448$;
- $s=5$ odd: $\lambda=-1.352190$, $A=1.3787$.

**Result, exactly as registered** (`k5_L1/out/k5_summary_primary.out`, `k5_summary_supp.out`; verdict code `kink_summary.main`, unchanged):

| registered item | primary, $\rho\in\{1.5,1.25\}$ | supplementary, $\rho\in\{1.5,1.25,1.15\}$ |
|---|---|---|
| **K5 (= K6), 10 graded rows** | **PASS 10/10** | **PASS 10/10** |
| extrapolated $b_0+D+\beta_n$, even | $-0.0005$ … $-0.0003$ | $-0.0005$ … $-0.0004$ |
| extrapolated, odd | $-0.0019$ … $-0.0017$ | $-0.0019$ … $-0.0017$ |
| calibrated $\lvert b_0+D_{\rm fit}+\beta_n\rvert$, every $\rho$ | $0.0032$–$0.0035$ | $0.0030$–$0.0035$ |
| K0′ (= K1), per state | even $+0.0039$ PASS; **odd $+0.00510$ FAIL** | even $+0.0037$ PASS; **odd $+0.005005$ FAIL** |
| K1 (= K3, gen 1): $\kappa_0,\sigma_0$, side, sign | PASS 10/10 | PASS 10/10 |
| K2 (= K3, gen 2) at $L-\log6$ | PASS 2/2 | PASS 2/2 |

Row by row (dev = extrapolated $b_0+D+\beta_n$; band = fit-window band of §4, post hoc; cal = largest calibrated value over the gradings):

| state | $n$ | registered mesh: dev / cal | sensitivity: raw / cal | rerun primary: dev ± band / cal | rerun suppl.: dev ± band / cal | verdict: reg. / sens. → rerun |
|---|---|---|---|---|---|---|
| E | 7 | +0.0596 / 0.0643 | −0.0138 / 0.0057 | −0.0005 ± 0.0002 / 0.0034 | −0.0005 ± 0.0003 / 0.0034 | FAIL / FAIL → PASS |
| E | 5 | +0.0355 / 0.0396 | −0.0100 / 0.0019 | −0.0004 ± 0.0004 / 0.0035 | −0.0004 ± 0.0004 / 0.0035 | FAIL / FAIL → PASS |
| E | 4 | +0.0183 / 0.0222 | −0.0073 / 0.0009 | −0.0003 ± 0.0004 / 0.0035 | −0.0004 ± 0.0004 / 0.0035 | FAIL / FAIL → PASS |
| E | 3 | +0.0111 / 0.0148 | −0.0063 / 0.0018 | −0.0004 ± 0.0004 / 0.0035 | −0.0004 ± 0.0004 / 0.0035 | FAIL / FAIL → PASS |
| E | 2 | −0.0003 / 0.0032 | −0.0048 / 0.0034 | −0.0005 ± 0.0005 / 0.0034 | −0.0005 ± 0.0005 / 0.0034 | PASS / PASS → PASS |
| O | 7 | +0.0609 / 0.0668 | −0.0172 / 0.0078 | −0.0019 ± 0.0027 / 0.0032 | −0.0019 ± 0.0027 / 0.0032 | FAIL / FAIL → PASS |
| O | 5 | +0.0357 / 0.0411 | −0.0125 / 0.0031 | −0.0017 ± 0.0020 / 0.0034 | −0.0017 ± 0.0020 / 0.0034 | FAIL / FAIL → PASS |
| O | 4 | +0.0176 / 0.0226 | −0.0094 / 0.0000 | −0.0019 ± 0.0019 / 0.0032 | −0.0019 ± 0.0020 / 0.0032 | FAIL / FAIL → PASS |
| O | 3 | +0.0102 / 0.0151 | −0.0081 / 0.0013 | −0.0017 ± 0.0020 / 0.0034 | −0.0018 ± 0.0020 / 0.0034 | FAIL / FAIL → PASS |
| O | 2 | −0.0017 / 0.0030 | −0.0062 / 0.0032 | −0.0019 ± 0.0021 / 0.0032 | −0.0019 ± 0.0022 / 0.0032 | PASS / FAIL → PASS |

**Reading.**
- *K6 at $L=1.0$.* By the registered rule (§4 of the prereg: all 10 rows pass in both verdicts), the $L=1.0$ K5 FAIL is resolved by this rerun. On meshes that grade every coupled chain point through the fit window, the offset holds at $L=1.0$ to $\le0.002$ (fit-window band $\le0.003$), with the boost $\beta_4=0.693$ and $\beta_2=0.347$, for all five chain points and both states.
  - The $n$-dependence of the registered failure is gone: the raw $\rho=1.5$ offsets agree across $n$ to $2\cdot10^{-4}$.
  - The $\rho=1.5$ member reproduces the post-registration diagnostic (calibrated $+0.00335$ in both, for E, $n=7$), as expected.
- *The original FAIL is not erased.* It stays in the record as "FAIL under the original registration" (17 of 20 rows), a failure of that mesh design.
- *A new, narrow registered failure.* K0′, the edge offset $D_{\rm fit}-D$ (= K1), fails for the odd $s=5$ state: $+0.00510$ (primary) and $+0.005005$ (supplementary) against the tolerance $0.005$.
  - The fit-window band is $\pm0.0027$, and the same state passed on the registered mesh ($+0.0047$).
  - Read together with §3: $D_{\rm fit}-D$ sits at $+0.0035$ to $+0.0051$ for both $L=1.0$ states on the registered and the rerun meshes. So the second-order edge law with $D=\lambda+\log2\pi+\gamma$ is supported to about $\pm0.008$ (value plus band) at $L=1.0$, **not** to the registered $\pm0.005$. A residual positive bias of the four-term edge fit is the likely cause, but that is not shown.
- K6 is the statement that [FR] accepts "for exact point values"; reading it off Galerkin nodal values is heuristic, which is why the mesh rule matters.

**Deviations from the registration.**
1. **Empty summary files.** `k5_batch.sh` passed titles containing "=" to `k5_summary.py`, which splits its argument at the first "=". The batch's two summary files were therefore empty; they are kept as `out/*_EMPTY_title_bug.out`.
   - The summaries were rerun on [VM] right after the batch, with the same code (md5 unchanged), the same file patterns and titles without "=".
   - No code or data changed. A local rerun of the primary summary with the same code gives the same numbers.
2. **Clock.** The registration time is from the laptop clock; [VM]'s clock agreed to 1 s.
3. **Error bands are post hoc.** The window bands in the row table were computed after the run (§4) and play no part in the verdict.

## 6. Tail law and the $c_X$ term

Tables `tab_tail_T1.tex` and `tab_tail_T2.tex` are generated from [NUM] `out/tail_summary.out`; `tab_cX.tex` is copied from the sources in §1.

**T1 (second-order law, $\lambda$-shifted).**
- 11 of 12 primary states passed the validity gate. X = 6 O5 missed it narrowly ($|\lambda'(d)/\lambda'(2d)-1|=3.1\cdot10^{-3}$ against $3\cdot10^{-3}$) and is reported only.
- $Z/P_1$ rises from $0.80$–$0.98$ on $[100,200]$ to $0.968$–$1.000$ on $[6400,10300]$. The mesh error of $Z$ (fine vs base) is $\le10^{-3}$, so the deviations from 1 are not numerical: they are the unmodelled remainder, always negative, of the order of $\sum_{n<X}c_n^2/a^2$ (post-hoc coefficient $k_{\rm eff}$ between $-0.01$ and $0.44$ for even states and between $0.56$ and $1.04$ for odd states, roughly constant in $T$).
- Without the $\lambda$-shift, $Z/P$ is $0.20$–$0.87$.
- The registered tolerance $2\sum c_n^2\langle a^{-2}\rangle+0.005$ was generous: $0.13$–$0.21$ on $[400,800]$. Every graded state passed inside it by at least a factor 2. **This test can see the $\lambda$-shift; it cannot see a constant error below about 10% at $T\le10^4$.**
- The first-order law $\pi TZ\to|\lambda'|$ is not testable here: $\tau(6400)=0.47$–$0.81$.

**T2 and the $c_X$ term.**
- $X=8$ ($2c_8=0.490$): $\alpha=0.512\pm0.067$, $0.658\pm0.064$, $0.525\pm0.063$, $0.671\pm0.061$.
  - Two pairs are high, by $2.6\sigma$ (E0, O20) and $3.0\sigma$ (Em1, O20; $2.96\sigma$). The second passes the registered $3\sigma$ rule by less than 0.003.
  - **Correction:** [NUM] and [FR] say "about $2.5\sigma$"; the recomputed values are 2.6σ and 3.0σ.
- Controls:
  - $X=6$: $+0.018\pm0.072$ and $+0.012\pm0.068$, a clean zero;
  - $X=10$: $0.32$–$0.44\pm0.18$–$0.19$, which lies between $0$ and $2c_8$. It passes the registered rule but is **uninformative**.
- $X=2,3$ (ref1-TE, P0 eigenfunctions, zeros 1–1500). This is the cleanest test, since there is no $nm=X$ competition.
  - With the $c_X$ term, $Z/P_F$ is $0.968$–$1.014$ on the three blocks of $[250,1981]$.
  - Without it, $1.086$–$1.127$ (even) and $0.859$–$0.910$ (odd), i.e. the sector sign is right.
  - Control $L=0.4$ ($c_X=0$): $0.971$–$0.999$.
  - $-\lambda'/2A^2=0.995$–$0.999$ for these states.
- $X=4$ (TA, rerun by ref2-TA), even, $s=0$: $Z/P_1=0.989$–$0.994$ ($h_0=L/1000$) and $0.991$–$0.993$ ($L/2000$), against $1.060$–$1.104$ without $c_4$.
  - Caveats from ref2-TA: the odd state has $|A|\approx0.02$ and $\lambda_o$ is not mesh-converged; the derivative-free split matches $2c_4\langle1/a\rangle$ only within 10–30%, and only in one case of four.
- Post hoc ([NUM] §4.4): at $X=8$ the even $Z/P_0$ is $1.012$–$1.024$ (the only values clearly above 1), and the odd values are below the $X=6,10$ controls. Near $T\approx4000$ the offsets are $\approx\pm0.03$, against $\pm c_8\langle1/a\rangle=\pm0.037$. The states differ in $\lambda$ across $X$.
- **Reading:** the $c_X$ term is supported at $X=2,3,4,8$ but not established. At $X=8$ it is not separated cleanly from the $\ell^{-2}$ kink terms at $T\le10^4$.

## 7. Figure

`fig_kink_split.pdf` (vector; black and grays, distinguished by line and marker shape, so readable in grayscale), made by `fig_kink_split.py` from the pre-registered run `numerics/out/k06_r1.15.json`.
- **State:** $L=0.6$, $s=0$, even ground state, $\lambda=-2.417$, $A=1.567$.
- **Plotted:** the one-sided excursions $[\psi(q\mp r)-\psi(q)]\,\ell^{3/2}/(c_nA)$ at $y_2$ and $y_3$ against $\ell$, with the predicted $+\frac23$ and $-\frac13$ (K3, $k=1$). The fit window is shaded.
- **Fitted limits:** $0.66679$ and $-0.33335$ at both points ($\kappa_0=1.00014$, $\sigma_0=0.33344$/$0.33345$). The script asserts that it reproduces the registered table values.
- **Why the curves are flat:** $D=-0.002$ and $\beta=0$ here, so the $O(1/\ell)$ correction nearly vanishes.

## 8. Disclosures

1. **[NUM] post-registration code change.** `kink_analyze.py` was changed after registration (md5 `8404f5dc…` → `87a74c8b…`). It is a pairing fix for symmetric meshes; the right-side values are unchanged. The new rerun uses `87a74c8b…` unchanged.
2. **[NUM] post-registration items.** The $L=1.0$ diagnostic (`diag_batch.sh`) and the cross-$X$ comparison are post hoc and are labelled so in every table.
3. **The error bands of §4 are post hoc.** They are computed with the registered code at other fit-window starts, and they change no verdict.
4. **Tolerances.** The tail T1 tolerance was generous (§6). Two $X=8$ split pairs are 2.6σ and 3.0σ high (§6).
5. **The original $L=1.0$ K5 FAIL stands.** The rerun of §5 is a separate registered test and does not convert it. The rerun's deviations are listed in §5: empty batch summaries caused by a title-parsing slip, rerun with unchanged code. The rerun also produced a new narrow registered failure, K0′ for the odd state.
6. **Scope.** Not tested: K7 (a conjecture), the smoothed cross term T5, and the true-form ground states at $L\ge0.6$.
7. **Grids.** The rerun ran on [VM] within the stated limits (3 BLAS threads, `ulimit -v` 12 GB, nice 10, one process at a time).

## 9. Files

| File | Contents |
|---|---|
| `numerics.md` | this report |
| `tables.tex` | table and figure environments with captions; `\input{numerics/tables}` from `papers/weil-edge/` (needs booktabs, array, amsmath, graphicx) |
| `tab_detect.tex`, `tab_H.tex`, `tab_cX.tex` | hand-copied tabulars (sources in §1) |
| `tab_kink_gen1.tex`, `tab_kink_gen2.tex`, `tab_k5.tex`, `tab_k0.tex`, `tab_tail_T1.tex`, `tab_tail_T2.tex` | generated tabulars |
| `preview.tex`, `preview.pdf` | compile check (`tectonic -Z search-path=. numerics/preview.tex` in `papers/weil-edge/`) |
| `consolidate_kink.py`, `kink_errors.out`, `kink_errors.json` | error bands (venv with mpmath: `python consolidate_kink.py <[NUM] dir>`) |
| `make_tables.py` | generated tables (`python3 make_tables.py <[NUM] dir>`) |
| `fig_kink_split.py`, `fig_kink_split.pdf` | the figure (`python3 fig_kink_split.py <[NUM] dir>`) |
| `k5_L1/` | the rerun: `PREREG_K5_L1.md`, `PREREG_K5_L1.md5`, solver copies, `k5_run.py`, `k5_summary.py`, `k5_batch.sh`, `k5_batch.log`, `out/*.json`, `out/k5_summary_*.out` |
