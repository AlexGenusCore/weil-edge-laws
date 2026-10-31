# Internal referee summary

*Johann Alexander Botha (GenusCore, info@genuscore.com). 2026-10-31.*

All refereeing so far is by **AI referees** (Anthropic's Claude, in separate review rounds directed by the author). No human expert has checked this work. Nothing here says anything about the Riemann hypothesis. This page is a summary of the internal final referee's report on the kink and tail laws; the full report and the transcripts are not published.

Abbreviations: [N] = [`edge_hadamard_note_v2.md`](edge_hadamard_note_v2.md); [S] = [`tail_kink_laws_note.md`](tail_kink_laws_note.md); [TA], [TE], [KW], [KL] = the internal write-ups (two per law; not included); [NUM] = [`../numerics/`](../numerics/); [GS] = the author's computer-assisted simple-even theorem, github.com/AlexGenusCore/weil-ground-state-simple-even (unrefereed).

## Scope of the verdicts

Everything rests on [N] Theorems 1–3. An earlier internal final referee accepted [N] (v1) "as proved"; no outside specialist has read it. "Accept as proved" below means: proved modulo [N] and the cited classical theorems, **pending external review**.

The referee recomputed the decisive constants with its own code, which shares no code with the write-ups: [`checks/fr_constants.py`](checks/fr_constants.py), output [`checks/fr_constants.out`](checks/fr_constants.out).

## Verdict per statement

| # | Statement ([S] numbering) | Verdict |
|---|---|---|
| Prop R | $2R_q=(\ell+a_q)^{-1}+O(\ell^{-3})$, $V_q^{-2}=\ell+a_q+O(\ell^{-1})$, Lemma T | accept as proved |
| K1 | edge law, sharp ($O(V^3)$), $V^3$ coefficient $\frac{q+\lambda-c}2$, and $A(\ell-D)^{-1/2}+O(\ell^{-5/2})$ | accept as proved |
| K2 | graded moduli | accept as proved |
| K3 | first-order kink law, all generations | accept as proved |
| K4 | singular set; density for $L>\frac12\log6$; no Hölder order | accept as proved for (a)–(d); (e) restates [N] Thm 5, and for $s=1$ it is conditional on [GS] |
| K5 | second-order odd part, every generation | accept as proved ($k=1$: two write-ups; $k\ge2$: [KL] only) |
| K6 | jump ratio $1/\rho_n=\ell-D-\beta_n+O(1/\ell)$ | accept as proved for exact point values; the Galerkin-trace reading is heuristic |
| K7 | second-order even part | **not proved** (an outline by a referee); keep as a conjecture with numerical support |
| T0 | exact contact identity | accept as proved |
| T1 | Fourier edge law on the strip, canonical $\Phi_c$ | accept as proved |
| T2 | sharp first-order tail law, no hypothesis on the zeros | accept as proved |
| T3 | smoothed second-order per-sector law, rate $\log^{-3/2}$ | accept as proved (first refereeing of the combination) |
| T4 | sharp edge×edge part | accept as proved |
| T5 | cross term vanishes on (cosine) average | accept as proved |
| T6 | exact moments; the open conjectures are one statement | accept as proved; (c) needs $A\ne0$ and a sector-simple $\lambda$ |
| Conj L, Conj R | sharp per-sector law; refined smoothed denominators | open, correctly labelled |

**Overall: accept.** The referee found no mathematical error in any statement marked "proved". Its issues concerned provenance, wording and citations; one item (K7) had to leave the theorem list.

## What the referee re-derived or recomputed (selection)

- The $q$-cancellation $a_q-q+c=-\log2\pi-\gamma$ (K1) and $a_q+D=q+\lambda-c$ (K5).
- The Lemma P side constants $\frac23,-\frac13$ ($a=\frac12$) and $\frac45,-\frac15$ ($a=\frac32$), and the Lemma O third-order constant $a\pi^2/12$, on an exact model kernel.
- The T6 moments $1-\gamma$ and $1+\frac{\pi^2}{12}$ from a closed form.
- The Landau sign of the per-sector term on 10 500 actual zeros: $\sum_{0<\gamma\le T}\cos(\gamma\log X)$ against $-\frac T{2\pi}c_X$ gives $-804.6$ vs $-803.7$ ($X=2$), $-1039.4$ vs $-1040.1$ ($X=3$), $-565.6$ vs $-568.3$ ($X=4$), $-400.8$ vs $-401.9$ ($X=8$); controls $X=6,10$ give $+3.3$ and $+0.9$ against $0$.
- The boost table $\beta_n$ at $L=1.0,1.19,1.5$ by direct chain enumeration.
- Where RH would enter: only in readings that need $h=|F|^2\ge0$ (positivity or monotonicity of $Z$, a Tauberian route to Conjecture L). No proof assumes RH; off-line zeros are allowed throughout.

## Issues raised, and how they were handled in [S]

| Issue | Severity | Handling |
|---|---|---|
| Four internal referee reports not archived | major (provenance) | [S] now says so; the referee re-checked the credited steps itself |
| External review of [N] still required | major | "proved, pending external review" everywhere |
| K7 listed as a theorem | medium | now Conjecture K7 |
| "$w_s$ is bounded" | medium | now "bounded on functions supported in a fixed window" ([S] §1) |
| Missing setting citations | medium | added in [S] §7: Connes–Consani 2106.01715; Connes 2602.04022 §6.5; Connes–Consani–Moscovici 2511.22755; Mori (prolate-weil-bounds, paper II); Suzuki 2606.09096 eq. (2.11) |
| K5 boost row: $L=0.6$ vs $0.8$ | minor | boosts stated at $L=0.8$; at $L=0.6$, $\beta_2=0$ |
| "Pre-registered" numerics | minor | [S] §6 discloses the post-registration change of `kink_analyze.py`, the generous tail tolerance, and the two $X=8$ split pairs at $2.5\sigma$ |
| T6(c) hypotheses | minor | stated in the bullet |
| Kwaśnicki 2011 wording | minor | "a position-side boundary asymptotic, proved by Fourier/Wiener–Hopf methods" |
| Gonek citation | minor | Contemp. Math. 143 (1993), 395–413 |
| Lemma M hypotheses | minor | $0<\lvert h\rvert\le h_0(\delta)$ and the $\lVert f\rVert_\infty$ dependence added |

## What still needs a specialist read

1. **[N], the base of everything.** A reader from the Kwaśnicki circle (complete Bernstein functions, Wiener–Hopf): Proposition 5.1 (especially Step 4), Lemma 6.1 (Steps 2–4), and Lemmas 8.3–8.4 (uniformity in $L$). A reader from the Weth/Saldaña log-Laplacian circle for Theorem 4.
2. **The zero side.** An analytic number theorist for [TA] §7: Lemma Z, Landau's formula with off-line zeros, and the conjugation bijection $\rho\mapsto1-\bar\rho$ (T2, T4).
3. **Two Wiener–Hopf steps to check first:** [TE] Theorem E (the exterior field, on which T3 and T5 rest) and [TA] Lemma 2 (the exact second-order edge transform).
4. **Conjecture K7:** write it out and referee it, or leave it as a conjecture.
5. **A cheap sanity anchor (optional):** at $L\le0.5$, certify one kink-to-edge ratio against $1/\rho=\ell-D-\beta_2$ ([S] §10.2).
