# Responses to the Codex second review (review_codex_20261031_0954.md)

Reviewer: OpenAI Codex, GPT-6.1 Sol, high reasoning effort, 31 October 2026. Verdict: release as a preprint after minor fixes and completion of the numerical supplement.
Backups before this round: `work/main_before_codex1.tex`, `work/refs_before_codex1.bib` (refs.bib unchanged in this round).
Build: tectonic, 51 pages, no undefined references; the only warnings are the two underfull hboxes that were already there before this round.

## Point 1: heuristic normalisation (§1.3 mechanism 4, Remark 8.4). Accepted.

Checked against Theorem 8.3 and its proof before editing. With f_z = psi - tau_z psi and Q^(s)(f_z) = (E + w_s)(f_z):
- (i) gives Q^(s)(f_z) = 2 lambda (1 - <psi, tau_z psi>) + 2 L(z) = lambda ||f_z||^2 + 2 L(z), since ||f_z||^2 = 2(1 - <psi, tau_z psi>). So the reduced energy Q^(s)(f_z) - lambda ||f_z||^2 = 2 L(z). Confirmed.
- The proof of (ii) gives Q^(s)(f_z) = 2 Z_cos(z) + 8(1-s) sinh^2(z/4) P_psi, so Z_cos(z) = Q^(s)(f_z)/2 - 4(1-s) sinh^2(z/4) P_psi. This matches the reviewer's formula. Confirmed.
- Asymptotics: L(z) = A^2 z + ... (Thm 9.1/9.2(b)) and lambda ||f_z||^2 = O(z/ell) (Thm 9.2(a)). So 2L(z) ~ 2A^2 z, Q^(s)(f_z) ~ 2A^2 z, and Z_cos(z) ~ A^2 z (Thm 9.2(c)). The old §1.3 text gave Z_cos the coefficient (A_+^2 + A_-^2) = 2A^2, which is wrong. Theorem 8.3 and Theorem 9.2 themselves were already correct.

Edits:
- §1.3 item 4 now separates the three quantities: the form energy Q^(s)(f_z) := Q^(s)_{L+z}(f_z) ~ 2A^2 z; the reduced energy Q^(s)(f_z) - lambda ||f_z||^2 = 2L(z) ~ (A_+^2 + A_-^2) z, which is the contact integral; and the zero sum Z_cos = half the form energy, up to a pole term O(z^2) that vanishes for s = 1, so Z_cos ~ A^2 z.
- I added a Fourier-side consistency check to §1.3: the same density heuristic gives (2A^2/pi) ∫ (1 - cos zt)/t^2 dt = A^2 z.
- Remark 8.4(1) now states both exact relations. It calls 2L(z) the reduced energy, not "the energy cost", and gives the three leading coefficients with references to Thm 9.2(a), (c).

## Point 2: proof of Proposition 9.4(b). Accepted. The statement is unchanged.

I replaced the general reciprocal-moment assertion with a stated and proved Claim. Let p be a probability density with p <= C_0 min(1, u^{-2}), and let d >= 1 be the exact denominator, kept everywhere. Suppose |d - ell' - log u| <= eta on the central range U = [e^{-ell'/2}, e^{ell'/2}], with ell' >= 4 + 4C_0. Then ∫ p/d = 1/(ell' + mu_1) + (mu_2 - mu_1^2)/ell'^3 + O(ell'^{-4} + eta ell'^{-2}).
- The tails off U are bounded with d >= 1 only, by 2 C_0 e^{-ell'/2}.
- On U the expansion runs to fourth order with an explicit remainder, and the moment tails are O(ell'^k e^{-ell'/2}).
- A parenthetical notes why the claim fails without d >= 1: there is a nonintegrable pole at u = e^{-ell'}.

The Claim is applied to the two densities:
- Smoothed case: p = (2/pi)(1 - cos u)/u^2, C_0 = 4/pi, d = a(u/z) - lambda for u >= z t_0, and d = 1 below z t_0, where the truncation is explicit. The truncation costs O(z t_0). t_0 = t_0(lambda) is fixed before z -> 0. For small z, every u in U has u >= z t_0 and t = u/z >= (2 pi e^lambda / z)^{1/2} >= max(1, t_0). So the logarithmic approximation is used only where t is large, with eta = O(z) by Lemma 2.1(c). The pole t = 2 pi e^lambda lies below U, where the exact denominator is kept.
- Sharp case: p = u^{-2} on [1, inf), C_0 = 1, mu_1 = 1, mu_2 = 2, d = a(Tu) - lambda >= 1 since T >= t_0, eta = C/T^2.

Both formulas of (b) follow with O(ell^{-3}), so nothing in the statement changes. I also changed the proof of Theorem 9.2(a), which used the same expansion with tails O(sqrt z), to cite the Claim. There the exact denominator is kept off the central range. No circularity: the Claim uses only Lemma 2.1(c) and the moments of 9.4(a).

## Point 3: numerical supplement. Accepted and done.

Backup before this point: `work/main_before_codex1_pt3.tex` (the round's `work/main_before_codex1.tex` was kept, not overwritten; refs.bib unchanged).

- Built `supplement/` (31 MB, 157 files + SHA256SUMS) and `supplement.zip` (16.6 MB; all raw data included, so no sha-only list was needed). Layout: `registered/` (the first registration: PREREG.md + md5, all scripts, zeros.txt, every out/ file incl. `k06_r1.15.json` and `tail_summary.out`), `numerics/` (table/figure producers, generated tables, and `k5_L1/`, the registered rerun), `snap_check/` (point 4), `unregistered/{p0,hp,zero_side}` (P0 code and outputs behind Table 2, hp-FEM Hadamard runs and the Section 10.1 explicit-formula check, zero-side checks at X=2,3,4, fr_constants with the Landau check), `check_paper_numbers.py` (recomputes every Section 10 number from the files), `README.md`.
- Added the originally registered `kink_analyze.py` (md5 8404f5dc..., fetched read-only from the run VM) as `registered/kink_analyze_as_registered.py`. The VM's raw out/ files are md5-identical to the local archive.
- Scrubbed: VM name and home paths in PREREG_K5_L1.md and k5_batch.sh (registered; their md5 now fail, disclosed with every replaced string), batch scripts, notes, one usage line, and absolute import paths (now relative). No computational line changed.
- Fresh-extraction check: all summaries, kink_errors, all tab_*.tex and the figure regenerate identically; all 13 registered/diagnostic kink runs re-run on the VM (2 cores, <= 1.84 GB) give identical tables; cheap P0, hp-FEM, zero-side and one tail run reproduce the stored output. Not re-run: registered tail runs, rerun rho=1.25/1.15, the slower P0 runs, mesh_x4_check, zeros_make (reasons in README).
- Paper corrections found by the check: Upsilon(6400) 0.47-0.81 -> 0.42-0.88 (old value was the X=8 range only); explicit-formula agreement (1-3)e-5 -> 1e-5 to 2.3e-4 depending on the fit basis, for the torsion function of the archimedean part; Landau check "within 0.5%" now says "at T=10303"; the registration record now says the registered kink_analyze.py also stopped on two of the three L=0.8 runs (not only on mirror runs) and is otherwise output-identical.
- Data availability rewritten: contents, README, the reproduction check and its limits, the redactions, and what is not reproducible (the internal review's fit-model comparison and flatness diagnostic; code not kept).

## Point 4: anchor-snapping rule (Methods; p1weil.py l.389-390). Accepted, disclosed and checked.

- Methods now says that P1 stores each node as anchor + offset. Shift overlaps are integrated exactly (Simpson on the common refinement, which is exact for products of linear functions) in the frame of the first anchor. An anchor difference below 1e-9 is set to 0, that is, treated as an exact chain identity y' - log n = y. The overlaps are therefore exact, up to rounding, only for the represented geometry and conditional on this identification. The word "exact" was removed from the P0/P1 overlap sentence. The text says the rule and the check concern P1, and that P0 was not audited in this respect.
- Check (`work/snap_check.py`, output `work/snap_check.out`): a light, local check with no solves. It rebuilt every registered P1 mesh with the original scripts and arguments:
  - kink L = 0.6 (right side, rho = 1.5, 1.25, 1.15; mirror side, rho = 1.5, 1.25), L = 0.8 (3 gradings), L = 1.0 (registered rho = 1.5, 1.25 and the sensitivity mesh);
  - the K5 rerun at L = 1.0 (3 gradings);
  - the tail runs X = 6, 8, 10, base and fine, at L_0 = log(X)/2 and the finite-difference windows L_0 - d, L_0 - 2d, L_0 - 4d. That is 38 meshes.
- For every shift log n used in assembly, the check took all anchor pairs with |A_i - log n - A_j| < 1e-9 and compared them with exact rational labels.
  - For L with transcendental e^{2L}, the label is (sigma, q), with anchor = sigma L - log q.
  - At L_0 = log(X)/2 the label is exp(2 * anchor), a rational. There, cross-edge identities are genuine.
- Result: 0 unrelated merges. Every snapped pair is an exact identity, with rounding residual at most 4.5e-14 (stated in the paper as "below 1e-13"). The smallest anchor difference that is not snapped is 2.0e-3, which is 2d in the finite-difference windows. The check also confirms that the 1e-12 anchor merge in make_mesh joins only identical points.
- I did not implement the reviewer's preferred option, identification by chain/rational labels inside the solver. The registered results were produced with the 1e-9 rule. The check shows that on those meshes the rule coincides with label identification, so a re-run would change nothing.

## Point 5: "of order 1e-24 for L >= 1.2" (§1.5 Status and scope; the reviewer's §1.4). Accepted.

There is no resolved computation behind that number: our codes are double precision, and its only source is an internal note. It is replaced by evidence the paper already contains:
- A_e ~ 0.062 at L = 0.4 and 2.4e-4 at L = 0.6;
- at L = 0.7 the hp-FEM derivative lambda' ~ -3.5e-11 is already at the double-precision floor (caption of Table 2, `tab:H`);
- for larger L the trace is below the resolved numerical scale, and no value is given.

The qualitative warning (the laws say nothing quantitative at accessible scales) and the Limits paragraph (L >= 0.6 not resolved) are unchanged and consistent with this.

## Point 6: priority material in the abstract and introduction. Accepted.

- Abstract: the attribution is now one short, prominent sentence: the facts "are not new". They were first proved, unrefereed, by bramble_trace on rStation (paper 67), and the traces had been derived in substance earlier in the mathia notes, with details in §1.4. The dates, the forum comment and the remainder detail moved out of the abstract; all of them are already in §1.4. The RH and numerical-limitation sentences of the abstract are unchanged.
- §1.1: I removed the forum-comment chronology from the "closest work" paragraph and replaced it with a pointer to §1.4 for chronology and comparison.
- §1.4 (prior work) keeps the detailed chronology and comparison. It also keeps the revision-after-learning-of-BT26 disclosure, which bears on the independence claim. §1.5 keeps its short attribution, the RH statement and the numerical limitations.

## Verification section

- Added a "Second review" paragraph. It gives the system (OpenAI's Codex, model GPT-6.1 Sol, high reasoning effort), the date (31 October 2026) and the verdict (release as a preprint after minor fixes; no fatal or major mathematical error in the principal results).
- The paragraph lists what the review checked:
  - §2 normalisations, with a numerical check of the Lévy representation;
  - §§3-4 and Appendix A;
  - §5 cross identity, layer integral and factors;
  - §§6-7 renewal constants (quadrature at q = 1, not error-certified), kink coefficients, transfer matrix, induction and every boost-table entry;
  - §§8-9 and Appendices B-C (no hidden use of RH);
  - the Mellin constants of Proposition 9.4;
  - a rerun of the supplied numerical analysis (checksums, verdicts, and an independent refit that reproduced the odd-state failure);
  - the rStation statements and dates of BT26, BT26a and BT26b;
  - the theorem numbers in Kw11, Suz26, KW26, Den06 and BK17;
  - novelty searches.
- The paragraph also lists what the review did not check: GS, the large solves, the unsupplied original P0/hp/tail runs, and every bibliography entry.
- It lists the findings and how this version addresses them, and says that these changes have not been reviewed again.
- The earlier sentence "revisions after the last pass ... have not been re-refereed" now reads "were checked only by the second review described next".
- Durkan-Hughes-Pearce-Crump (the reviewer's alternative source for Landau's formula) was not added to the bibliography, so it is not named.

## Other

- `\enlargethispage{3pt}` after `\maketitle` removes a 2 pt overfull vbox on page 1. The shorter abstract had moved the page break.
- I checked main.tex and refs.bib for e-mail addresses other than info@, host names, user names, IPs and local paths: none found.
