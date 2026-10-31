I recommend **public release as a preprint after minor fixes and completion of the promised numerical supplement**. I read `main.tex` in full, including all three appendices, and checked the numbered arguments sequentially. I found no fatal or major mathematical error in the principal results. The Wiener–Hopf construction, Hadamard argument, kink induction and unconditional zero-side argument appear coherent; the qualifications concerning vanishing traces, parameter uniformity and RH are appropriate. The priority discussion fairly credits the substantial overlap with earlier work. The issues below concern a normalization error in the heuristic explanation, a repairable proof passage, numerical documentation and exposition. This assessment does not certify every external reference or computation.

**Issues**

1. **Minor — §1.3, mechanism 4, and Remark 8.4; `main.tex:130,1006`: the heuristic conflates three differently normalized quantities.**  
   Writing \(f_z=\psi-\tau_z\psi\), the exact relations are
   \[
   Q^{(s)}(f_z)-\lambda\|f_z\|^2=2\mathcal L(z),
   \]
   and
   \[
   Z_{\cos}(z)=\lambda(1-\langle\psi,\tau_z\psi\rangle)
   +\mathcal L(z)-4(1-s)\sinh^2(z/4)P_\psi.
   \]
   Thus \(Z_{\cos}(z)\sim A^2z\), whereas \(Q^{(s)}(f_z)\sim2A^2z\) when \(A\ne0\). The introductory description assigns the latter leading coefficient to the former. Remark 8.4 also calls \(2\mathcal L(z)\) the energy cost without subtracting the eigenvalue term.  
   **Fix:** distinguish the quadratic-form energy, the reduced energy \(Q^{(s)}-\lambda\|\cdot\|^2\), and the zero sum. Theorem 8.3 itself has the correct normalization.

2. **Minor — Proposition 9.4(b), proof; `main.tex:1143`: the general reciprocal-moment expansion needs a qualification.**  
   The assertion
   \[
   \int\frac{dP(u)}{\ell'+\log u}
   =\frac1{\ell'+\mu_1}
   +\frac{\mu_2-\mu_1^2}{\ell'^3}+O(\ell'^{-4})
   \]
   does not hold for an arbitrary probability measure merely because all logarithmic moments exist: the denominator can have a nonintegrable pole at \(u=e^{-\ell'}\). In this application the original denominator is \(a(u/z)-\lambda\), and the smoothed integral is truncated at \(u=zt_0\); these facts provide the needed protection.  
   **Fix:** retain that denominator and truncation explicitly, expand on the central range, and bound the two tails for the particular densities used here. Choose \(t_0\) sufficiently large before replacing the exact denominator by its logarithmic approximation. I do not see a resulting change to the proposition.

3. **Minor, but necessary for the numerical release — Data availability; `main.tex:1272–1275`, and numerical producer scripts.**  
   The supplied directory does not yet reproduce the entire numerical section. For example, `fig_kink_split.py:14` requires `out/k06_r1.15.json`, and `make_tables.py` requires the original `out/tail_summary.out`; neither is supplied here. The original registration, tail-analysis pipeline and P0/hp evidence are also absent. Consolidated tables and descriptions cannot replace their inputs.  
   **Fix:** include the complete promised archive, dependencies and commands, with relative paths that work from a fresh extraction. This does not undermine the analytic theorems, whose proofs do not use the computations.

4. **Minor — numerical Methods, `main.tex:1153`; `numerics/k5_L1/p1weil.py:389–390`: disclose the geometry-snapping rule.**  
   The description calls prime-shift overlaps “exact”, but the implementation sets anchor residuals below \(10^{-9}\) to zero. This matters when profiles use offsets as small as \(10^{-30}\): ordinary coordinate roundoff and an intentional identification of chain points must be distinguished. The rule may be entirely appropriate for those identities, but it is part of the numerical method.  
   **Fix:** describe it explicitly; preferably identify equivalent anchors through their chain/rational labels, and check that no unrelated anchors are merged. State that the overlap integration is exact conditional on the represented geometry.

5. **Minor — §1.4, `main.tex:160`: qualify the extremely small trace estimates.**  
   “Of order \(10^{-24}\) for \(L\ge1.2\)” gives neither a finite tested range nor evidence that these amplitudes are resolved. This is especially problematic alongside the disclosure that the computations are in double precision and these states are beyond the tests’ resolution.  
   **Fix:** identify the tested windows and supporting precision/convergence evidence, or replace the number by “below the resolved numerical scale”. The qualitative warning about inaccessible asymptotic regimes remains justified.

6. **Minor — abstract and §1.4: separate mathematical contribution from review history more economically.**  
   The manuscript is readable, but extensive priority and internal-review details precede a substantial amount of the mathematics and recur later. A specialist can follow the paper more easily if the abstract concentrates on the genuinely added results and their hypotheses.  
   **Fix:** retain a short, prominent attribution to the earlier trace/Hadamard work, and place the detailed chronology and comparison in the existing prior-work subsection. Preserve the present RH and numerical limitations.

**Claims independently checked, and how**

- **Form normalization and operator setup (§2).** I checked the Fourier factors, pole kernel, prime correlation coefficient, strict activation cutoff, form-domain approximation, compactness argument and bounded windowed perturbation. In particular,
  \[
  c_a=3.53430635281632,\quad c=-5.372183419225665,\quad
  c+c_a=-\log(2\pi).
  \]
  Numerical integration of \(2(1-\cos tu)J(u)\) reproduced the digamma difference at \(t=0.2,1,7\); the largest observed discrepancy was approximately \(4.2\times10^{-27}\).

- **Half-line inversion and first edge law (§§3–4; Appendix A).** I checked the Fourier signs in the factorization, the Hardy-space support argument, extension across the far endpoint, and the semigroup/Duhamel bootstrap. These arguments avoid assuming a pointwise singular-integral realization for the original eigenfunction.

- **Hadamard and translation results (§5).** I checked the signs in the cross identity, the exact renewal layer integral, treatment of bounded exterior terms, continuity of eigenvectors and traces, and passage to the derivative. The constant is **one squared trace per endpoint**. The mixed identity and its squared, edge-free consequence have consistent factors.

- **Second-order renewal and edge constants (§§6–7).** I checked the derivation
  \[
  a_q=q+\frac\pi2+2\log2,\qquad
  \mu_q-a_q=\lambda+\log(2\pi)+\gamma.
  \]
  An independent oscillatory quadrature of the free resolvent at \(q=1\) gave \(1/(2R(e^{-\ell}))-\ell\) approximately \(3.88165,3.91800,3.93710\) for \(\ell=10,20,40\), approaching the claimed \(3.9570906879\). These are numerical spot-checks, not error-certified evaluations.

- **Kink coefficients and propagation (§§6–7).** I checked the transfer matrix, generation induction, second-order odd-part bookkeeping and cancellation of \(q\). They produce the stated \(2/3:-1/3\) and \(3/5:-2/5\) splits. I independently recomputed every entry of the prime-power boost table. The irrational-rotation argument establishes the stated sufficient density threshold without requiring uniform estimates over the dense set.

- **Zero-side arguments (§§8–9; Appendices B–C).** I checked the form-domain extension of the explicit formula, absolute-convergence estimate, strip sampling inequality, two-pass Fourier bootstrap, off-line-zero pairing and Landau-term sign. I found no hidden use of RH. The distinction between the proved smoothed second-order law and the conjectural sharp version is maintained.

- **Mellin constants.** Independent differentiation of the Mellin transform gives
  \[
  \mu_1=0.422784335098467,\qquad
  \operatorname{Var}(\log u)=1.822467033424113,
  \]
  agreeing with Proposition 9.4.

- **Supplied numerical rerun.** All nine recorded checksums match. Reanalysis with the supplied scripts reproduces the reported verdicts. A separate NumPy refit of the raw profiles gives:

  | Grading set | Even edge-offset error | Odd edge-offset error |
  |---|---:|---:|
  | \(1.5,1.25\) | \(0.0038583\) | \(0.0051026\) |
  | \(1.5,1.25,1.15\) | \(0.0037281\) | \(0.00500448\) |

  The odd-state test therefore **still fails** the registered \(0.005\) threshold. The independently refitted jump offsets remain within approximately \(0.002\), consistent with the reported passes. The manuscript reports these outcomes honestly.

- **Closest public priority claims.** I independently inspected [rStation paper 67](https://rstation.ai/problems/riemann_hypothesis/papers/67) and [forum post 21](https://rstation.ai/r/riemann_hypothesis/posts/21). They substantiate the credited earlier trace existence, Hadamard formula, endpoint rigidity, pure-log result and activation comparison, including the cited statement numbers and posting dates. The forum also contains the acknowledged heuristic denominator involving \(D\). The paper appropriately treats the core trace/Hadamard results as prior work.

- **Selected external theorem numbers and hypotheses.** I checked Kwaśnicki’s cited CBF factorization and boundary results against [arXiv v4](https://arxiv.org/html/1006.0524v4); Suzuki’s Theorems 1.3–1.4 against [v2](https://arxiv.org/html/2606.09096v2); the meromorphic exception in [Kwaśnicki–Wszoła, Theorem 1.2](https://arxiv.org/html/2609.24892); [Denisov, Lemma 2.3](https://arxiv.org/html/0908.4049); and [Bonami–Karoui, equation (43)](https://arxiv.org/html/1012.3881v3). The cited descriptions are consistent with those sources. The fixed-\(X\), unconditional Landau formula used here is also stated as [Theorem 1 in Durkan–Hughes–Pearce-Crump](https://arxiv.org/html/2601.18025).

- **Novelty assessment.** Independent searches across arXiv, Zenodo, GitHub and accessible rStation material did not reveal an additional earlier statement of the explicit kink hierarchy or the eigenfunction zero-tail law. Inspection of cached, commit-specific mathia notes supports the manuscript’s attribution of the earlier \(O(\ell^{-1})\) trace work. The remaining novelty claims are reasonably hedged; search absence cannot establish priority conclusively.

**What I could not check**

- The rStation API endpoints failed through the available tools. Public paper/forum pages were accessible, but I could not complete an exhaustive platform-wide API audit.
- GitHub’s connected search required reauthentication; web access and the cached mathia repository provided only partial coverage. Several Zenodo records were inaccessible.
- I did not independently validate the computer-assisted simple-even certificate `[GS]`, its Arb implementation, or the other cited positivity certificates. Applications depending on `[GS]` remain dependent on that external input.
- I did not rerun the large Galerkin solves, regenerate the 10,500-zero dataset, or reproduce the missing original P0, hp and tail experiments.
- I did not verify every bibliography entry, every cited book theorem against its specified edition, or the full unavailable differential–difference papers. The cited numbers in SSV and Bertoin remain among these unchecked items.
- The numerical renewal checks have no rigorous quadrature error bounds. Neither they nor this review constitute formal verification of the analytic proofs.