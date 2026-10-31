# Edge law, Hadamard formula, and echo and tail laws for the localized Weil form

Research notes by Johann Alexander Botha (GenusCore, info@genuscore.com), version 0.1.0, 2026-10-31.

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
> **Priority caveat.** An external reviewer told us of an earlier manuscript, *Boundary traces and support variation for localized Weil operators*, reportedly posted on 27 October 2026 under the handle bramble_trace. Its Corollary 2.3 reportedly states that all interval eigenvalues of the compressed log|D| are simple and that the endpoint trace squares are 1/(2a). We have not been able to locate it. Its title suggests that it may also contain a support-variation (Hadamard-type) formula. Until we can compare, we make **no priority claim** for the translation (trace) identity, simplicity, the edge law, the Hadamard formula or the pure-log theorem. Wherever these notes call something "new" or say it "appears new", read: not found in our literature search (the search is listed in the note).
>
> **Related recent work.** Veltri, a preprint on log|D| on an interval, Zenodo record 23769666 (2026-10-29). We list it as recent related work and do not characterise its content further.
>
> **What is claimed, and what is not.**
> - The edge law (E) and the Hadamard formula (H) are proved, pending external review.
> - The kink-law items K1–K6 and the tail-law items T0–T6 were accepted by the internal final referee (an AI referee).
> - Open: Conjecture K7 (second-order even part of the kink), Conjectures L and R, and Prediction F (sharp second-order tail law).
> - Open: $A_e\neq0$ for the true even ground state. This is equivalent to the simple-even problem.
> - The laws are asymptotic, and they are vacuous wherever $A=0$. For the true form at $L\ge1.2$, $A_e\sim10^{-24}$, so they say nothing at accessible scales.

## Contents

| Path | What it is |
|---|---|
| [`notes/edge_hadamard_note_v2.md`](notes/edge_hadamard_note_v2.md) | Edge law (E), Hadamard formula (H), translation identity, pure log symbol (simplicity, $A^2=1/(2L)$), nonvanishing. Full proofs, numerical checks, prior art. |
| [`notes/tail_kink_laws_note.md`](notes/tail_kink_laws_note.md) | Kink law K1–K6 (Conjecture K7), tail law T0–T6, Conjectures L and R, numerical confirmation, prior art and credits, next steps. |
| [`notes/referee_summary.md`](notes/referee_summary.md) | The internal (AI) final referee's verdict table and what still needs a specialist read. |
| [`notes/checks/`](notes/checks/) | Small check scripts and outputs: the final referee's P0 Galerkin code for the Hadamard constant (`p0/`), the evidence table of the edge-law note (`evidence.py`), the final referee's recomputed constants (`fr_constants.py`), the moment and chain checks of the laws note. |
| [`numerics/`](numerics/) | The pre-registered P1 Galerkin test of the kink and tail constants, with its registration, scripts, small outputs and 10 500 zeta zeros. See [`numerics/README.md`](numerics/README.md). |

A companion paper on the pure-log case is in preparation; it is not part of this repository.

## How to cite

> J. A. Botha, *Edge law, Hadamard formula, and echo and tail laws for eigenfunctions of the localized Weil quadratic form: research notes*, version 0.1.0, 2026-10-31. Not peer-reviewed; AI-assisted.

Machine-readable metadata are in [`CITATION.cff`](CITATION.cff). Please cite the credited prior work as well (Eberwein, mathia, Kwaśnicki and others; see §14 of the edge-law note and §7 of the laws note).

## Related repositories

- [github.com/GenusCore/weil-ground-state-simple-even](https://github.com/GenusCore/weil-ground-state-simple-even): the author's computer-assisted proof that the ground state of the localized Weil form is simple and even on a range of windows. Theorem 5(d) of the edge-law note uses its range $(0,1.19]$ as an input.

## Running the checks

Python 3.10+ with numpy, scipy and mpmath. For example:

```
(cd notes/checks && python3 -I evidence.py)     # about 15 s
(cd notes/checks && python3 -I chain_enum.py)
(cd numerics && python3 p1weil.py zeros.txt)    # solver gates
```

## License

Code (`*.py`, `*.sh`) is under the MIT License. Text (`*.md`) is under CC BY 4.0. See [`LICENSE`](LICENSE).
