# Responses: rStation priority sweep and final referee report (final pass 1)

Date: 31 October 2026. Inputs: `scratch_archive/rstation/OVERLAP_MAP.md` §3(d), `deep_C3/C4/C5/C6/C8/C9.md`, the cached rh_67 v1 manuscript (§§2–3.3, 6, 7, 9, 10 re-read), rh_66 v2 Prop 6.1, the post-21 comment metadata (authors and timestamps re-verified from the cache), the mathia clone (PL-329, PL-336, PL-337, PL-338 statements re-read), `papers/purelog/review_ext1/` (comparison, check_novelty, responses) and `work/review_final1.md`.

Backups: `work/main_before_rstation.tex`, `work/refs_before_rstation.bib`.
Build: tectonic, 50 pages (was 47). No errors, no overfull boxes, no undefined references or citations, clean BibTeX log. Underfull vboxes remain (a short page 6 and some bibliography pages), as before the revision.
Nothing was pushed, published or sent. No local paths, host names, IPs or the accounts@ address are in `main.tex` or `refs.bib`. The author block is unchanged: Johann Alexander Botha, GenusCore, info@genuscore.com.

Numbering in the new PDF: Thm E = 4.1, Lemma field = 5.2, Lemma layer = 5.3, Thm transl = 5.4, Thm H = 5.6, Cor edgefree = 5.7, Prop nonvan = 5.8, Prop R = 6.2, Thm K1 = 7.1, Thm kink = 7.3, Cor K4 = 7.4, Thm K5 = 7.5, Cor K6 = 7.6, Thm T0 = 8.3, Thm T1 = 8.5, Lemma Z = 8.6, Prop T4 = 8.7, Thm T2 = 8.8, Thm contact = 9.1, Thm T3 = 9.2, Thm T5 = 9.3, Prop T6 = 9.4.

---

## Part A. Priority and novelty (task 1; OVERLAP_MAP §3(d))

**A1. Abstract (map (d)1).** Rewritten.
- It now says that trace existence, |A+| = |A−| and the Hadamard formula on simple branches, including activations, with a limit formula for A±, were proved first in an unrefereed rStation manuscript by the AI agent bramble_trace (riemann_hypothesis paper 67, 27 Oct 2026).
- It says that the mathia notes had derived the trace with a remainder of order 1/log(1/r) in substance.
- Our contribution is stated as: proofs with quantitative remainders, uniform on compact ranges; a different route for (H); the second-order edge law; the translation (mixed) identity for λe ≠ λo; the kink law; the tail law.
- The pointwise-in-L caveat is added (see B2).

**A2. False statement at old line ~135 (map (d)2).** "New here are a complete proof for every pole weight s and every eigenfunction, the integral formula of Theorem E(iii), and …" is deleted. The edge-law paragraph of §1.4 now credits the following.
- rh_67 [BT26] (2.2), (3.8), §3.3, (3.19): existence for every eigenfunction and every real pole weight (class (2.8)), the L∞ bound and a limit formula of the same kind.
- The first public appearance, comment XNTCbIH-RNPZ9afU of 2026-10-18 23:44:00 UTC [BT26a].
- [BT26] (7.3) and §7: the uniform trace bound and continuity in a. Its only remainder is a relative o(1) (§4). Its route to existence is described as essentially ours.
- **mathia, each note described exactly:**
  - PL-319–323: the limit with a qualitative remainder o(ℓ⁻¹) per eigenstate. A pointwise realisation of a singular integral is assumed (PL323-3, PL323-4).
  - PL-329 (new bib entry, commit ac5835e, 16 Sep): for profiles obeying the PL-319 endpoint identity, with envelope A Q^{-1/2} and a source bounded by S, |g − C Q^{-1/2}| ≤ K(1+S)/Q + K e^{−c(Q−Q₁)}, with K, c, Q₁ independent of the family parameter and Q = ℓ + log 2. The quantitative maximum-principle step is asserted, not written out (PL329-4, PL329-20). Their η and R are renamed c and Q₁ to avoid clashes.
  - PL-336: applies PL-329 to the odd branch at the first activation, conditional on uniform L∞, and gives u₀(1−2e^{−Q}) = C₀Q^{−1/2} + O(Q^{−1}) (PL336-6).
  - PL-337: the uniform L∞ bound on compact window ranges with bounded eigenvalue (PL337-3).
  - PL-338: the expansion with an L² remainder on the new layer, for odd states near every activation (PL338-2, -3).
  - Conclusion stated in the paper: a uniform O(ℓ⁻¹) remainder is stated there for s = 1, with a sketched step.
- **What we claim instead:**
  - A complete proof of that remainder for the whole family H_L^(s) and every eigenfunction, with constants explicit in terms of C∞ (eq. (3.3), Lemma 3.5).
  - The O(ℓ^{−3/2}) sharpening at fixed L (Thm 7.1(a)).
  - The second-order law with offset D (Thm 7.1(c), Prop 6.2).
- **Credits for D.** The heuristic fit with D in its denominator is credited to span_of_dilates, comment EAw5pFmSdKxMBRHA, 2026-10-28 03:55:32 UTC [SoDb]. halasz_resonator's κ(s) expansion is cited as related (comment 3-jlbw7xu_tS6Rou, 2026-10-19 00:10:21 UTC [HR26]).
- **Remark 4.2(4).** Added at Theorem 4.1, repeating the credit locally.

**A3. False statements at old line ~137 (map (d)3).** "No unconditional derivative formula was proved there, and we found none elsewhere" and "To our knowledge Theorems H and transl are new as theorems for the Weil form" are both deleted. The Hadamard paragraph now states the following.
- rh_67 Thms 2.1–2.2 are summarised: the cluster law λ − δ eig(H) + o(δ), (2.3)–(2.4); B− = B+, H = 2B+, rank ≤ 1, (2.5); λ′ = −|τ−|² − |τ+|² for simple branches including activations, (2.6); local Lipschitz, (7.5).
- The first public statement, comment hDqAfsXyecUVBoz0 of 2026-10-27 17:43:11 UTC [BT26b], is cited.
- Their method is described: collar decomposition, strong resolvent limit, Feshbach–Schur elimination.
- The activation formula is described: Thm 2.4, −2wp|τ+|²δ/log(1/δ).
- Explicitly not new: Thm 5.6 for simple eigenvalues and Thm 5.4(a),(b), which are [BT26, (2.5), (2.6)]; and Thm 5.4(d), which is [BT26, (6.3)], with the even–odd case spelled out in comment nWrDJmydgFHjXF0u (2026-10-27 18:55:11 UTC) [SoDa].
- **Ours:**
  - a different route (cross identity plus layer integral; the shared ingredient, the exterior response ≈ Aℓ^{1/2}, is noted against [BT26, (4.7)]);
  - the remainder Cδℓ(δ)^{−1/2}, uniform on compact L-ranges (theirs is o(δ));
  - C¹ for sector-simple branches, labelled a minor extension.
  - It is also stated that [BT26] is stronger on clusters, one-sided extensions and the Lipschitz bound.
- New, to our knowledge: the translation identity with a rate, part (c) for λe ≠ λo (the mixed identity), and Cor 5.7.
- The pure-log sentence now cites [BT26, Cor 2.3] first.
- Credit sentences are also placed at the statements: after Thm 5.4, at the end of Thm 5.6, and in Remark 5.10(3) and (4).
- The "A>0, λ′<0, (c) new" remark after Prop 5.8 now notes that [BT26] proves monotonicity but no nonzero trace (§6 after (6.3)).

**A4. Kink paragraph (map (d)4).**
- Added: [BT26, Thm 2.4] concerns the regime that the kink law excludes, so neither result implies the other.
- Added: the existence of the traces, the input to the kink law, is credited to [BT26].
- "We found no statement …" is extended with "(our searches included the rStation manuscripts on the Riemann hypothesis and the forum thread on [BT26], screened on 31 October 2026)".

**A5. Tail paragraph (map (d)5).**
- "Structure found in [PL338]" now reads "… and proved for eigenvalues in [BT26, Thm 2.4]", both in §1.4 and after Thm 9.1.
- Added: [SoD66, Prop 6.1], under GRH, a far-field 1/log limit for a different, Christoffel-type quantity (rh_66 v2, 2026-10-27 21:16:47 UTC); no tail law over zeros was found on rStation.

**A6. Pure-log paragraph (map (d)6).** Now reads: simplicity and A±² = ‖u‖²/|I| were proved first in [BT26, Cor 2.3], and [BPL] gives another proof plus the edge law with a rate.

**A7. Literature-search sentence (map (d)7).** Now reads: "(arXiv, Zenodo, GitHub, rStation and the web, to 31 October 2026; the web search engines we used do not index rStation)".

**A8. Status list (map (d)8).** The first bullet uses the credited wording: our proofs are complete, pending review, and existence and (H) were proved first in [BT26, §3.3, Thms 2.1–2.2], which is unrefereed.

**A9. "What is new" paragraph (task 1, new).** Added at the end of §1.4. It lists:
1. the O(ℓ⁻¹) remainder for the full family with uniform constants, compared with mathia, plus O(ℓ^{−3/2}) at fixed L;
2. the second-order edge law with D;
3. the translation identity for distinct eigenvalues, the mixed identity and the edge-free identity;
4. the kink law (Thms 7.3, 7.5, Cors 7.4, 7.6);
5. the zero-side results (Thms 8.3, 8.5, 8.8, 9.1, 9.2, 9.3, Prop 9.4);
6. Prop 5.8.

It also lists, as second proofs, (E) by essentially the route of [BT26] and (H) by a different route. In the task text these results are numbered "Thms 8, 10, Cor 9, 11, Thms 13–19, Prop 20"; in this paper's section-based numbering they are the items above.

**A10. 4πe^{2L} law and "converged" λ0 at 2.25 or 2.5 (map C8).** Not present in this paper (checked by grep). Nothing to drop, and no rh_80, rh_81 or Mori-V citation is needed.

**A11. How rStation items are presented and cited.**
- §1.4 opens with a paragraph that:
  - describes rStation as a platform where AI agents post manuscripts that automated reviewer agents review and accept;
  - verifies that the normalisation is identical (a = L, τ± = A±, (2.1) = Q_L^(1), class (2.8) contains every s);
  - says that the items are cited for priority of public statements, are unrefereed public claims written by AI agents, have not had their proofs fully checked by us, and are not used in any proof.
- **Bib entries.** All use handle, title, "rStation, riemann_hypothesis paper N, vV, published <UTC>", and the URL https://rstation.ai/problems/riemann_hypothesis/papers/N/vV. Comments use the comment id plus the UTC timestamp, with the post-21 URL. The entries are:
  - BT26 (rh_67 v1, 2026-10-27 19:07:56 UTC);
  - BT26a (XNTCbIH-RNPZ9afU);
  - BT26b (hDqAfsXyecUVBoz0);
  - SoDa (nWrDJmydgFHjXF0u);
  - SoDb (EAw5pFmSdKxMBRHA);
  - HR26 (3-jlbw7xu_tS6Rou);
  - SoD66 (rh_66 v2);
  - Li45 (rh_45 v1, lihongmin, 2026-10-23 09:48:37 UTC);
  - BT60 (rh_60 v1, 2026-10-26 19:12:17 UTC).
- **Li45 and BT60.** These were added in §1.1 as posted positivity certificates for both sectors, on (0, ½ log 11] and (0, 2]. They concern the spectrum and complete the list of certified computations; they are not required by the map.
- **Kernel representation.** §1.2 now also credits the Lévy-kernel representation of the archimedean term to [BT26, (3.1)–(3.3)], which uses the same J.

**A12. Not done (needs the author).** No independence sentence was added ("found independently of [BT26]"). Map (d)10 makes it conditional on the author's confirmation, as in the purelog paper. The text says only that our proofs are a second route and do not depend logically on [BT26].

---

## Part B. Final referee report (work/review_final1.md)

**B1 (issue 1, [BPL] dependence).**
- The bib entry is now exactly: J. A. Botha, *Boundary trace and simplicity of the Dirichlet spectrum of the logarithmic Laplacian on an interval*, preprint, 2026; to be posted at https://github.com/AlexGenusCore. "In preparation; not yet public" is removed.
- §1.4 (pure-log paragraph) states that [BPL] is cited only for comparison (after Thm 5.4, Remarks 5.10 and 7.2, Table 2) and as the template for §3 and App. A, whose arguments are given in full, and that no proof depends on it.
- The search and reliance sentence repeats this.
- The cross-references to [BPL, Rem 1.3, Cor 1.5, Conj 9.2] follow the current draft of the companion paper. Re-check them once it is posted.

**B2 (issue 2, pointwise constants).**
- The abstract says: "The second-order and kink laws hold at fixed L, with constants that are not uniform near the windows 2L = log n."
- §1.2 adds the same caveat after the second-order edge display and in the kink paragraph.
- §1.2 also states that the first-order remainder O(ℓ⁻¹) is uniform.

**B3 (issue 6, unrefereed and AI-produced sources).**
- New sentence at the end of §1.4: no proof depends logically on any of the unrefereed sources (mathia, rStation, and the other deposits) or on [BPL]. The only exception is [GS] (which uses [Zhu]), on which the s = 1 statements on (0, 1.19] depend, as stated each time.
- The sentence also says which sources are AI-agent written: the rStation items and most of the mathia notes.

**B4 (issue 3, Thm H error term).** Done, because the change was short (App. C machinery).
- **Lemma 5.2 (exterior field)** now uses the Wiener–Hopf profile m(η) = 1 + M_K(η) of Lemma C.1. It has a bounded remainder R_f, uniform as in Thm 4.1. The proof uses Lemma C.2 (exterior identity) applied to u = χψ̃ = G₁f₊, together with:
  - |k(−η) − A+| ≤ ‖f₊‖∞ V(η);
  - mV ≤ 3, from Lemma C.1(c) and Lemma 3.3(a);
  - the R₄ bound (previously inside the proof of Thm 9.1, now proved in Lemma 5.2 and cited from there).
- **Lemma 5.3 (layer)**: the main term is exactly A⁽¹⁾A⁽²⁾δ, by ∫₀^δ m(η)V(δ−η)dη = δ (Lemma C.1(g)). The error is CδV(δ) ≤ Cδℓ(δ)^{−1/2}, uniform. The old proof (about 25 lines) is replaced by a short one.
- **Consequences:**
  - Thm 5.4 now has error O(hℓ(h)^{−1/2});
  - Thm 5.6 now has error Cδℓ(δ)^{−1/2} (was Cδ(1+log ℓ)ℓ^{−1/2}).
- **Why not O(δ/ℓ).** The referee's suggested O(δ/ℓ) would need the second-order germ (Thm 7.1(b)) and Lemma C.4, whose constants are pointwise in L, while Thm 5.6 needs uniformity through activations. A remark after Lemma 5.3 says so and does not claim it.
- **Circularity check.** Lemmas C.1 and C.2 use only §§2–3 and Lemma B.1, so there is no circularity. This is stated in the text.
- The numbering of the novelty claim and of the verification list is updated. These proofs are new since the last referee pass, and the verification section says they have not been re-refereed.

**B5 (issue 4, notation overloads).** Renamed:

| Old | New | Where |
|---|---|---|
| h_f | k_f | §3; now the same function as k_f in the edge lemma and k in Thm 4.1(iv), so "k_f = h_f on (0,∞)" is dropped |
| local h = ṽ*f | k | Apps B, C |
| h in Lemma 3.2 | b_q | Lemma 3.2 |
| h, H(y) | \hat r_q, 𝓗(y) | Prop 6.2 |
| G(u), G₀(s) | 𝔤(u), 𝓜(s) | Prop 6.2, Prop 9.4 |
| G(η) | 𝓖(η) | Thm 8.3 |
| G^(X), R_G | 𝓖^(X), R_𝓖 | App. C |
| G(t,y) | Y(t,y) | Lemma 8.6 |
| R(η) | R_f | Lemma 5.2 |
| support radius R | L′ | Lemma 8.1 |
| β_ρ | Re ρ, Im ρ (written directly) | — |
| Kim et al.'s β | "an exponent" | — |
| germ coefficients σ± | 𝗌± | — |
| germ sums Σ∓ | 𝖲∓ | kink proof |
| chain signs ε_i | ς_i | the old "not to be confused" note is dropped; App. A's integration variable ς becomes t′ |
| τ(T), τ^ν, τ_σ | Υ(T), Υ^ν, Υ_σ | — |
| Aronszajn–Krein τ(λ) | α_res(λ) | — |
| κ(r) | κ_ext(r) | Prop 5.8 |

- The notation table gains rows for 𝓖, m and R_f, and Υ.
- A sentence says that β, κ and M keep local meanings, always subscripted or in another font.
- Left as they were: translation steps h, κ_q, κ_kink, M_K, 𝖬, the fit coefficients σ₀ in §10 (they are column headers of the generated tables), and the App. A resolvents.

**B6 (issue 5, length and structure).**
- **Data availability "Registration record"** is condensed. The md5 sums, SAST times, file names and the empty-summary anecdote are gone. The facts are kept:
  - registered before any run, with checksums;
  - the L = 1.0 rerun registered separately;
  - three deviations (the side-matching fix in the analysis script, the summary step rerun with unchanged code, the bands computed afterwards);
  - the route labels;
  - the files to be supplied with the code.
- **"Verification status"** is condensed to one paragraph. It keeps: AI assistance; the AI-only checking (including that Thms 9.2, 9.3 and Prop 9.4 were refereed only once before assembly); the result of the last proof pass; the referee-contributed ingredients; the revisions not re-refereed (including this round's); "no human expert"; the full list of steps that most need an expert reading (now including Lemmas 5.2, 5.3, C.1 and C.2); the citation-numbering caveats; [GS]; and responsibility. The workflow-log anecdote is dropped.
- **"Credits"** is condensed. It now refers to §1.4 for details, so the mathia attributions are no longer repeated almost verbatim. It adds the rStation credits.
- **§10 itself.** The facts remain: the registered PASS and FAIL rows, the registered FAIL at L = 1.0 with its cause, the post-hoc diagnostic marked "no verdict", and the separately registered rerun.
- **Net length.** 47 → 50 pages, because of the added priority text. Without the condensation it would be longer.

**B7 (issue 7, Prop T4 range mismatch).**
- Lemma 8.6 now takes T ≥ 2 and integrates over [T/2, 4T], which contains [T−1, 2T+1]. The proof notes the inclusion and log(2+|t|) ≤ C log T.
- In Prop 8.7 the cross terms use Thm 8.5(a) on the shells [T/2,T], [T,2T] and [2T,4T]. Prop 8.7 and Thm 8.8 now assume T ≥ 2T₀.

**B8 (issue 8, D_fit sensitivity).** Reported in §10. The referee's independent P0 computation gave:
- a fit of A and D alone: D_fit − D = +0.008 to +0.011;
- with an added c/ℓ term: −0.03 to −0.06.

The claim is widened: "supporting D to within a few hundredths, not to the registered ±0.005; the registered verdicts refer to the registered fit model". The fit-free flatness diagnostic is reported: ψ(L−r)(ℓ−D)^{1/2} is constant to about 1e-4 relative on ℓ ∈ [20, 60]. These are not registered numbers, and the text says so.

**B9 (issue 9, smoothed per-sector wording in §1.2).** Now reads: "the error is O(log^{−3/2}T), so this term is resolved only by a factor (log T)^{1/2} (Theorem 9.2(d),(e))".

---

## Part C. GitHub owner (task 3)
- refs.bib [GS]: github.com/GenusCore/weil-ground-state-simple-even → github.com/AlexGenusCore/weil-ground-state-simple-even.
- [BPL] points to github.com/AlexGenusCore.
- main.tex contains no other GitHub-owner reference.

## Part D. Items for the author
1. Confirm (or not) the independence of discovery before any "found independently" sentence is added (map (d)10).
2. Check the [BPL] theorem numbers once the companion paper is posted.
3. Before release, re-check the rStation versions list for rh_67 (v1 only on 2026-10-31).
4. Optional cosmetic fix: page 6 is short, because a long paragraph forces the break. Adding `\raggedbottom` would remove the underfull-vbox warnings; it was not added.

---

# Minor pass 2 (31 October 2026): check_rstation_novelty.md and check_rstation_math.md

Backups: `work/main_before_minor2.tex`, `work/refs_before_minor2.bib` (refs.bib unchanged).
Build: tectonic, 50 pages. No errors, no undefined references or citations, no overfull boxes, no underfull vboxes (after `\raggedbottom`), clean BibTeX log, no `??` in the PDF. Two pre-existing underfull hboxes remain (l. 243, 686). Forbidden strings: none in main.tex or refs.bib. Theorem numbering unchanged. Nothing pushed, published or sent.

**N1 (PL-335).** Checked against the note at commit 6f267e0 (PL335-1, -8, -9, -10, -11): at a = ½log2 (2L = log 2), s = 1, lowest odd eigenfunction ≥ 0 on (0,1), an antisymmetric Hopf lemma (Pollastro–Soave) gives liminf √Q u₀(1−2e^{−Q}) > 0, so C₀ > 0 whenever the trace exists. Remark after Prop 5.8 now credits A_o > 0 at s = 1, 2L = log 2 to [PL335] and restricts "new" to the other cases of A > 0 in (a), (b), to λ′ < 0 and to (c). "What is new" (vi) and the Credits section say the same.

**W1 (BT26 "proved").** Abstract: "first posted, with proofs (unrefereed), on rStation by bramble_trace, in paper 67 (27 Oct); the existence of the traces had been posted there as a working lemma in a forum comment of 18 October 2026" (the cached comment XNTCbIH-RNPZ9afU calls it a "working lemma" with a sketched argument). §1.1: "gives proofs (unrefereed; Section 1.4) of … first posted as a lemma in a forum comment of 18 October 2026 [BT26a]".

**W2 (route).** §1.4: "Its route to existence (a variance-gamma splitting, the half-line renewal function of [GR12] and a bounded perturbation) is close to ours, which factorises the archimedean symbol directly (Section 3)". "What is new": "by a route close to that of [BT26]".

**W3 / math issue 1 (K1(a) uniformity).** Decided from the proofs: uniform. The proof of Thm 7.1(a) uses only Thm 4.1 (‖f₊‖∞ ≤ C_q, |ψ̃| ≤ CV), Lemma modulus(a) (uniform, and it bounds every |ψ(y_n−t)−ψ(y_n)| by CV(t), including n near activation) and Lemma theta (threshold depends only on j and the interval). The source display holds on (0, min(ρ₀/2, log 2)) with a uniform O(t) (the δ⁻_X restriction is not needed there; pole term analytic, commutator term Lipschitz since χ = 1 on [−ρ₀, ρ₀]). Changes: Thm 7.1 sentence now says "uniform as in Theorem 4.1, for fixed q (its proof uses only …)"; the proof of (a) and the source display state the uniform range; the §§6–7 header names Lemma modulus(a) and Thm 7.1(a) as the exceptions to "pointwise"; §1.2 edge paragraph, §1.4 and "What is new" (i) say O(ℓ^{−3/2}) uniform on compact ranges (no "at fixed L"). Verification-status list adds this as not re-refereed.

**Math issue 2 (remark after Lemma layer).** Reworded: the loss ℓ(δ)^{−1/2} does not come from e₂ (O(V³) uniformly by Thm 7.1(a), contributing O(δ/ℓ)) but from the constant part of R_f (m(η)(k₊(−η)−A₊) → −f₊(0+), Lemma pot) together with the w_s-terms, also of order δV(δ); an O(δ/ℓ) bound would need that constant to cancel against the w_s-term as in step (4) of the proof of Thm 9.1, which uses Lemma pot with pointwise constants.

**W4–W6 (local credits).** After Thm 7.1: "The offset D appeared earlier, without proof, in a heuristic fit [SoDb]." Conj 11.5 "What is proved" (i): "(\cite[(6.3)]{BT26}, \cite{SoDa})". Kink paragraph: "forum post 21, where [BT26] was discussed". W7, W8 (optional) not applied.

**Math issues 3–6, 8 (notation, citations, layout).**
- Notation note: local β, κ, M "are defined where they occur".
- k = ṽ*f₊ renamed k₊ (Thm 4.1(iv), proofs of Thm 4.1, Lemma field, Lemma modulus, Thm 7.1, App. B, Lemma pot, proof of Thm 9.1); the general-f function in Lemma extid is now k_f (= k_f of §3). Table row "G_q, k_f, k₊" added. Eigenvalue index k and generation k unchanged.
- Odd-reduction proof (Lemma oddtransfer): G, G₁–G₃ renamed f^o, f^o₁–f^o₃ (odd part of f about z); O was not used, to avoid a clash with O(d).
- Lemma field proof: now cites Lemma Klevy(f) (K(2/η) ≤ Cℓ^{1/2}) and Lemma V(a) (VK ≤ 3), plus Kasym(b).
- Thm 8.5 (T1): "T₀ ≥ 2", so Lemma Z (T ≥ 2) applies wherever Prop 8.7 and Thm 8.8 use T ≥ 2T₀.
- `\raggedbottom` added; the page-6 gap and the underfull vboxes are gone.

**Math issue 7 (optional).** Abstract now adds that our proof of the Hadamard formula covers eigenvalues "only simple in their parity sector".

**Independence (author confirmed 2026-10-31).** §1.4, end of the rStation paragraph: results obtained without knowledge of rStation; [BT26] learned of from an external review on 31 October 2026, after the proofs were written, and the rStation comparisons added then; a later revision shortened the proofs of Lemmas field and layer using only Appendix C; parts of the mathia notes were known while working.

**Internal.** `scratch_archive/rstation/OVERLAP_MAP.md` §2 C5: comment nWrDJmydgFHjXF0u now attributed to span_of_dilates (2026-10-27T18:55:11Z), with a correction note.
