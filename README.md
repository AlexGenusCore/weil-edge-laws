# Edge law, Hadamard formula, and echo and tail laws for the localized Weil form

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23832559.svg)](https://doi.org/10.5281/zenodo.23832559)

Paper and research notes by Johann Alexander Botha (GenusCore, info@genuscore.com), version 0.2.0, 2026-10-31.

## Progress

Public releases across the author's three related repositories, as of 1 November 2026. All are **unrefereed** and
**AI-assisted** (Anthropic's Claude, used through Claude Code, directed by the author). Every review so far was run by AI
systems: internal Claude-based referees, and for the later items a second AI system, OpenAI's Codex. **No human expert has
checked any of them.** Independent review is welcome: info@genuscore.com.

| Date | Release | Result | Review status |
|---|---|---|---|
| 2026-10-25 | [weil-ground-state-simple-even](https://github.com/AlexGenusCore/weil-ground-state-simple-even), first release (commit `26fd9e6`; no tag, no DOI) | Certified simple, even ground state of the localized Weil form for `L` in `(0, 1.09]` | Internal AI review rounds only |
| 2026-10-26 | weil-ground-state-simple-even, version of 2026-10-26 (commit `8adfbe5`; no tag, no DOI) | Range extended to `(0, 1.19]` | Internal AI review only; the new windows 1.03–1.19 had no review round at release |
| 2026-10-31 | weil-ground-state-simple-even v1.1.0, archived as v1.1.1 (credits corrected): [10.5281/zenodo.23832221](https://doi.org/10.5281/zenodo.23832221) | Range extended to `(0, 1.4035]` (Piece III, with Elston's certifier) | Internal AI review only; Piece III not audited beyond `L = 1.19` |
| 2026-10-31 | [weil-edge-laws](https://github.com/AlexGenusCore/weil-edge-laws) v0.1.2, research notes: [10.5281/zenodo.23832560](https://doi.org/10.5281/zenodo.23832560) | Edge law, Hadamard formula, kink (echo) and tail laws | Internal AI referee rounds only |
| 2026-10-31 | [log-laplacian-interval-trace](https://github.com/AlexGenusCore/log-laplacian-interval-trace) v1.0.0, paper: [10.5281/zenodo.23832744](https://doi.org/10.5281/zenodo.23832744) | Boundary trace identity and simple Dirichlet spectrum for the logarithmic Laplacian on an interval | Internal AI referees; two reviews by GPT-6.1 Sol (the second through Codex): release as a preprint after minor corrections, which were made |
| 2026-10-31 | weil-edge-laws v0.2.0, paper: [10.5281/zenodo.23834265](https://doi.org/10.5281/zenodo.23834265) | The notes consolidated into a paper with complete proofs | Internal AI referees; Codex (GPT-6.1 Sol): release as a preprint after minor fixes, which were made; the changes were not reviewed again |
| 2026-11-01 | weil-ground-state-simple-even v2.0.0: [10.5281/zenodo.23852617](https://doi.org/10.5281/zenodo.23852617) | Range extended to `(0, 2]` (Piece IV) | Fresh-agent AI audits of Piece IV; two Codex (GPT-6.1 Sol) rounds, the first "not yet" (three major points), the second "release as a preprint after minor corrections"; all points addressed. Neither round re-ran the large certificates |

Several of these results, or parts of them, were obtained earlier by others; each repository's README and paper give
the credits (among them Zhu, Kramarenko-Byrd, Elston, the rStation authors bramble_trace and lihongmin, and the mathia
notes). None of the results is a result about the Riemann hypothesis. Work on extending the range and on computer-light
proofs continues; nothing beyond the releases above is claimed.

## Paper (v0.2.0)

**Edge laws, a Hadamard formula and kink singularities for eigenfunctions of the localized Weil quadratic form**, J. A. Botha, 31 October 2026.

- PDF: [`paper/main.pdf`](paper/main.pdf) (52 pages; source [`paper/main.tex`](paper/main.tex), [`paper/refs.bib`](paper/refs.bib), tables and figure in [`paper/numerics/`](paper/numerics/)).
- Numerical supplement: [`paper/supplement/README.md`](paper/supplement/README.md) (every script, registration and raw output behind Section 10; `sha256sum -c SHA256SUMS`).
- Reviews and responses: [`reviews/`](reviews/).

The paper is the consolidated version of the research notes below, with complete proofs. In plain terms, for the localized Weil form $Q_L$ (pole terms with any real weight) it proves:
- **Edge law.** Every eigenfunction $\psi$ vanishes at the window edges like $A_\pm(\log\frac1r)^{-1/2}$, with a remainder $O(\ell^{-1})$ that is uniform on compact ranges of $L$, the pole weight and $\lambda$ (sharpened to $O(\ell^{-3/2})$), and with a **second-order term**: $\psi(\pm(L-r))=A_\pm(\log\frac1r-D)^{-1/2}+O(\log^{-5/2}\frac1r)$, $D=\lambda+\log2\pi+\gamma$.
- **Hadamard formula.** $d\lambda/dL=-(A_+^2+A_-^2)$ with an explicit remainder, for eigenvalues that are simple only within their parity sector (even or odd), also where a new prime power enters; the proof uses an exact two-window cross identity. The formula itself was posted first, with its own proof, by the AI agent bramble_trace on rStation (riemann_hypothesis paper 67, 27 October 2026); the paper credits it and claims no priority for it.
- **Kink law.** The prime terms copy the edge singularity into the interior: at $L-\log n$, and at every point reached from an edge by a chain of such shifts, $\psi$ has a logarithmic singularity with an explicit two-sided profile. For $L>\frac12\log6$ these points are dense, and $\psi$ is Hölder of no positive order on any interval when $A_\pm\ne0$.
- **Tail laws over the zeta zeros.** First order: $\sum_{|t_\rho|>T}\hat\psi(\gamma_\rho)\hat\psi(-\gamma_\rho)=(A_+^2+A_-^2)/(\pi T)+O(1/(T\log T))$. Second order: the per-parity-sector term, proved in smoothed form (the sharp-cutoff form is open). Both are **unconditional**: no hypothesis on the location of the zeros is made.

None of this proves or disproves the Riemann hypothesis. The laws are asymptotic and say nothing where $A_\pm=0$; for the true even ground state they say nothing quantitative at accessible scales.

**Credited to others** (details in §1.2 of the paper): bramble_trace, rStation riemann_hypothesis paper 67 v1 (existence of the edge traces with an $L^\infty$ bound and a limit formula, the Hadamard formula, and the pure-log simplicity theorem; see the priority note below); the mathia research notes (the traces in substance, the question of a Hadamard law in edge stresses with conditional reductions, and a remainder of order $\ell^{-1}$ with a sketched step); Kwaśnicki (the $\ell^{-1/2}$ boundary law on a half-line); Eberwein (numerical observation of the kinks); Mori and Connes–Consani (cut points at $L-\log n$ in trial vectors); Mori, Groskin and Joubert (zero-side and frequency-tail bounds of order $\log T/T$, and a numerical precursor of the link between edge values and the zero-side tail). The statements for the true ground state on $(0,1.19]$ use the author's unrefereed computer-assisted simple-even theorem (see Related repositories).

**Status.** Unrefereed preprint, AI-assisted (Anthropic's Claude, via Claude Code, directed by the author). Each proof went through repeated Claude-based referee passes, and the assembled text through further passes on proofs, novelty and citations, and exposition. On 31 October 2026 it was reviewed by a separate AI system, OpenAI's Codex (model GPT-6.1 Sol, high reasoning effort), whose verdict was release as a preprint after minor fixes, with no fatal or major mathematical error found in the principal results; its findings were addressed in this version (see [`reviews/`](reviews/)), and those changes have not been reviewed again. **No human expert has checked the proofs or the code.** Two pre-registered numerical tests failed in part as registered; all failures are reported.

To rebuild the PDF: `cd paper && tectonic --keep-intermediates main.tex`, run twice (a single clean run can leave page references one pass short).

## Research notes (v0.1.x)

The localized Weil quadratic form restricts Weil's explicit-formula quadratic form for the Riemann zeta function to functions supported in a window $[-L,L]$. Its eigenfunctions vanish at the window edges like $A\,(\log\frac1{\text{distance}})^{-1/2}$. These notes study the edge trace $A$ and what it controls:
- **(E) edge law** and **(H) Hadamard formula** $d\lambda/dL=-2A^2$, with a translation identity, a pure-log theorem and nonvanishing results;
- the **kink (echo) law**: the prime terms copy the edge germ into the interior at $L-\log n$ and along chains of prime shifts, one logarithm weaker at each step;
- the **tail law**: the weight that the zeta zeros above height $T$ carry in Weil's explicit formula for an eigenfunction is about $|\lambda'(L)|/(\pi T)$.

> **Status.** Research note, dated 2026-10-31, posted to make the work public and citable. **It is not peer-reviewed.** It was produced largely with an AI assistant (Anthropic's Claude, via Claude Code), directed by the author, Johann Alexander Botha (GenusCore, info@genuscore.com). The only checking so far is by AI referees, in internal review rounds:
> - edge law and Hadamard formula: four internally refereed write-ups (each with a referee, a repair and a second referee), then a final referee who re-checked the chain line by line and recomputed the decisive constant with independent code;
> - kink and tail laws: two independent write-ups per law, each internally refereed, a pre-registered independent numerical test, then a final referee (verdict table in [`referee_summary.md`](notes/referee_summary.md)).
>
> No human expert has checked any of it. Nothing here proves or disproves the Riemann hypothesis.
>
> **Priority: earlier work on rStation.** Several results in these notes were obtained earlier by the AI-agent author `bramble_trace` on rStation, a research platform for AI agents: bramble_trace, "Boundary traces and support variation for localized Weil operators", rStation riemann_hypothesis paper 67, v1, published 2026-10-27 19:07:56 UTC, https://rstation.ai/problems/riemann_hypothesis/papers/67/v1 (below: rh_67). Its trace-existence lemma first appeared in rStation comment XNTCbIH-RNPZ9afU (bramble_trace, 2026-10-18 23:44:00 UTC), and the manuscript was first attached to comment hDqAfsXyecUVBoz0 (bramble_trace, 2026-10-27 17:43:11 UTC). That paper proves: (i) existence of the endpoint traces for every eigenfunction of the localized Weil operator, primes and pole included (its §3.3, without a rate), with an $L^\infty$ bound (3.8), a limit formula for the trace of the same kind as our Theorem 1(3) (its (3.19)), a uniform trace bound (7.3) and continuity in $a$ (§7); (ii) the support-variation (Hadamard) law for isolated clusters, $\lambda_k'(a)=-|\tau_-|^2-|\tau_+|^2$ on simple branches including prime activations, with remainder $o(\delta)$, and $B_-=B_+$, rank $\le1$ on eigenspaces (Theorems 2.1–2.2); (iii) an activation formula at prime powers (Theorem 2.4); (iv) for the pure $\log|D|$: every interval eigenvalue is simple and $|\tau_\pm|^2=1/(2a)$ (Corollary 2.3). Its (6.3) also gives the equal-eigenvalue case of our mixed identity: $A_eA_o=0$ at even/odd crossings. We learned of it from an external reviewer after writing these notes; our proofs are independent and in part different (for the trace value we use a dilation/cross identity). We claim **no priority** for (i)–(iv) or for (6.3). Not found there: the rate $\psi=A\ell^{-1/2}+O(\ell^{-1})$ of Theorem 1, the explicit remainder in (H), the second-order edge law, the mixed identity for eigenfunctions with different eigenvalues, the edge-free identity, and the kink and tail laws. For the Weil form and for $\log|D|$ the mixed identity reads $(\lambda_e-\lambda_o)\Phi'(0)=2A_eA_o$; for the logarithmic Laplacian $L_\Delta=2\log|D|$, whose eigenvalues are $\mu=2\lambda$, it reads $(\mu_e-\mu_o)\Phi'(0)=4A_eA_o$.
>
> **Other rStation items.** All comments below are on rStation riemann_hypothesis forum post 21 (https://rstation.ai/r/riemann_hypothesis/posts/21).
> - $A_eA_o=0$ for opposite parities at a meeting: comment nWrDJmydgFHjXF0u (span_of_dilates, 2026-10-27 18:55:11 UTC), confirmed by bramble_trace in comment ARELX3rLocSdLMoL.
> - Parity alternation for $\log|D|$ (the $k$-th interval eigenfunction has parity $(-1)^{k-1}$): bramble_trace, comment ARELX3rLocSdLMoL (2026-10-27 19:28:58 UTC).
> - The dilation commutator $[x\frac d{dx}+\frac12,\log|D|]=-I$, applied to functions with zero traces, so with no boundary term: comments Oh96OclK_-s0vtY8 (span_of_dilates, 2026-10-27 21:55:20 UTC) and S1mqO-tsM-U45_Ng (bramble_trace, 2026-10-27 22:21:51 UTC); also span_of_dilates, "The near radical of a finite-window Weil form carries planted-zero visibility above the Nyquist height", rStation riemann_hypothesis paper 68, v1, published 2026-10-28 01:51:06 UTC, https://rstation.ai/problems/riemann_hypothesis/papers/68/v1, §3. Our one-endpoint dilation identity, whose boundary term is the trace, was not found there.
> - A heuristic fit whose denominator contains $D=\lambda+\log2\pi+\gamma$: span_of_dilates, comment EAw5pFmSdKxMBRHA (2026-10-28 03:55:32 UTC; labelled heuristic, "I have no proof"). We claim only the proof of $D$ at fixed $L$.
> - A second-order expansion of the Wiener–Hopf factor $\kappa(s)$: halasz_resonator, comment 3-jlbw7xu_tS6Rou (2026-10-19 00:10:21 UTC). It expands the factor, not $V$ or $\psi$.
>
> We screened all 81 rStation riemann_hypothesis papers and forum post 21 on 2026-10-31. None of them states the kink or tail laws. Related, for different quantities: span_of_dilates, "Finite-window Weil forms on Davenport-Heilbronn functions: a certified onset bound, an exact joint detection identity, and finite-space measurements", rStation riemann_hypothesis paper 66, v2, published 2026-10-27 21:16:47 UTC, https://rstation.ai/problems/riemann_hypothesis/papers/66/v2, Proposition 6.1 (a far-field $1/\log$ law for a planted-quartet detection quantity; part (b) assumes GRH); and span_of_dilates, "An equilibrium conjecture for how far the ground state of a truncated Weil form tracks the zeros, with measurements for Dirichlet L-functions", rStation riemann_hypothesis paper 80, v1, published 2026-10-30 17:09:59 UTC, https://rstation.ai/problems/riemann_hypothesis/papers/80/v1, (3.2′) (a per-zero displacement formula). rStation papers are accepted by AI reviewer agents; they are not refereed. Throughout these notes "new" means only "not found in our search".
>
> **Related recent work.** Veltri, a preprint on log|D| on an interval, Zenodo record 23769666 (2026-10-29). We list it as recent related work and do not characterise its content further.
>
> **What is claimed, and what is not.**
> - Our independent proofs of (E) with rate $O(\ell^{-1})$ and of (H) with explicit remainder are complete, pending external review. Existence of the traces and (H) itself were proved first in rStation rh_67 v1 (§3.3, Thms 2.1–2.2).
> - The kink-law items K1–K6 and the tail-law items T0–T6 were accepted by the internal final referee (an AI referee).
> - Open: Conjecture K7 (second-order even part of the kink), Conjectures L and R, and Prediction F (sharp second-order tail law).
> - Open: $A_e\neq0$ for the true even ground state. This is equivalent to the simple-even problem.
> - The laws are asymptotic, and they are vacuous wherever $A=0$. For the true form at $L\ge1.2$, $A_e\sim10^{-24}$, so they say nothing at accessible scales.

## Contents

| Path | What it is |
|---|---|
| [`paper/`](paper/) | The paper (v0.2.0): `main.pdf`, `main.tex`, `refs.bib`, the tables and figure it includes (`numerics/`), and the numerical supplement (`supplement/`, see its [`README.md`](paper/supplement/README.md)). |
| [`reviews/`](reviews/) | The second review of the paper by OpenAI's Codex (`codex_review_2026-10-31.md`), the responses to it (`responses_codex1.md`), and the responses to the rStation priority sweep and final internal referee pass (`responses_rstation.md`). |
| [`notes/edge_hadamard_note_v2.md`](notes/edge_hadamard_note_v2.md) | Edge law (E), Hadamard formula (H), translation identity, pure log symbol (simplicity, $A^2=1/(2L)$), nonvanishing. Full proofs, numerical checks, prior art. |
| [`notes/tail_kink_laws_note.md`](notes/tail_kink_laws_note.md) | Kink law K1–K6 (Conjecture K7), tail law T0–T6, Conjectures L and R, numerical confirmation, prior art and credits, next steps. |
| [`notes/referee_summary.md`](notes/referee_summary.md) | The internal (AI) final referee's verdict table and what still needs a specialist read. |
| [`notes/checks/`](notes/checks/) | Small check scripts and outputs: the final referee's P0 Galerkin code for the Hadamard constant (`p0/`), the evidence table of the edge-law note (`evidence.py`), the final referee's recomputed constants (`fr_constants.py`), the moment and chain checks of the laws note. |
| [`numerics/`](numerics/) | The pre-registered P1 Galerkin test of the kink and tail constants, with its registration, scripts, small outputs and 10 500 zeta zeros. See [`numerics/README.md`](numerics/README.md). |

A companion paper on the pure-log case is in preparation; it is not part of this repository.

## How to cite

Archived on Zenodo. DOI for all versions (resolves to the newest): [10.5281/zenodo.23832559](https://doi.org/10.5281/zenodo.23832559); the paper, v0.2.0: [10.5281/zenodo.23834265](https://doi.org/10.5281/zenodo.23834265); the research notes, v0.1.2: [10.5281/zenodo.23832560](https://doi.org/10.5281/zenodo.23832560).

The paper:

> J. A. Botha, *Edge laws, a Hadamard formula and kink singularities for eigenfunctions of the localized Weil quadratic form*, version 0.2.0, 2026-10-31, Zenodo, doi:10.5281/zenodo.23834265. Not peer-reviewed; AI-assisted.

The research notes:

> J. A. Botha, *Edge law, Hadamard formula, and echo and tail laws for eigenfunctions of the localized Weil quadratic form: research notes*, version 0.1.2, 2026-10-31, Zenodo, doi:10.5281/zenodo.23832560. Not peer-reviewed; AI-assisted.

Machine-readable metadata are in [`CITATION.cff`](CITATION.cff). Please cite the credited prior work as well (bramble_trace's rStation paper 67, Eberwein, mathia, Kwaśnicki and others; see §1.2 of the paper, §14 of the edge-law note and §7 of the laws note).

## Related repositories

- [github.com/AlexGenusCore/weil-ground-state-simple-even](https://github.com/AlexGenusCore/weil-ground-state-simple-even): the author's computer-assisted proof that the ground state of the localized Weil form is simple and even on a range of windows. Theorem 5(d) of the edge-law note uses its range $(0,1.19]$ as an input.

## Running the checks

Python 3.10+ with numpy, scipy and mpmath. For example:

```
(cd notes/checks && python3 -I evidence.py)     # about 15 s
(cd notes/checks && python3 -I chain_enum.py)
(cd numerics && python3 p1weil.py zeros.txt)    # solver gates
```

## License

Code (`*.py`, `*.sh`) is under the MIT License. Text (`*.md`) is under CC BY 4.0. See [`LICENSE`](LICENSE).
