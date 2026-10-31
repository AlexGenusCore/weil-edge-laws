# Tail and kink laws for the localized Weil form

*Johann Alexander Botha (GenusCore, info@genuscore.com). Research note, dated 2026-10-31.*

> **Status.** Research note, dated 2026-10-31, posted to make the work public and citable. **It is not peer-reviewed.** It was produced largely with an AI assistant (Anthropic's Claude, via Claude Code), directed by the author, Johann Alexander Botha (GenusCore, info@genuscore.com). The only checking so far is by AI referees, in internal review rounds:
> - edge law and Hadamard formula: four internally refereed write-ups (each with a referee, a repair and a second referee), then a final referee who re-checked the chain line by line and recomputed the decisive constant with independent code;
> - kink and tail laws: two independent write-ups per law, each internally refereed, a pre-registered independent numerical test, then a final referee (verdict table in [`referee_summary.md`](referee_summary.md)).
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

*Sources and labels.*
- [N] is the companion note [`edge_hadamard_note_v2.md`](edge_hadamard_note_v2.md): edge law, Hadamard formula, translation identity, pure log, nonvanishing.
- Each law was proved in **two independent write-ups**: [TA] (Fourier/Abelian) and [TE] (explicit formula and contact identity) for the tail law; [KW] (Wiener–Hopf) and [KL] (Lévy/renewal) for the kink law. They are internal working documents and are not included here; lemma and section numbers in brackets refer to them. Each was internally refereed, and the four referee verdicts at the last round were "correct with minor gaps". Not every internal referee report was archived (those for [KW], and for the second rounds of [TA] and [TE], are missing). The internal final referee re-checked line by line the steps credited to them.
- [NUM] is the pre-registered independent numerical test in [`../numerics/`](../numerics/).
- [GS] is the author's computer-assisted simple-even theorem, github.com/AlexGenusCore/weil-ground-state-simple-even (unrefereed).
- Small checks for this note are in [`checks/`](checks/): `denominators_check.py`/`.out` (mpmath, about 2 min) and `chain_enum.py`/`.out` (seconds). The final referee's independent recomputations are `checks/fr_constants.py`/`.out`.

---

**Status of the statements (read first).**
- This is analysis of a quadratic form. **It says nothing about the Riemann hypothesis.** Where zeta zeros enter, no hypothesis on them is made unless a statement says so.
- Everything rests on [N] Theorems 1–3: the edge law (E), the Hadamard formula (H), and the translation identity. [N] was accepted by an internal final referee; no specialist outside the project has read it.
- A new continuous piecewise-linear (P1) Galerkin code, which shares no code with the earlier solvers, tested the predicted constants against a pre-registration ([NUM]; see §6 for what changed after registration).
- **New in this note, and checked only by the internal final referee** (who accepted them):
  - Theorem T3 with an explicit rate. It combines Theorem B of [TA] with Theorem E of [TE] and removes Pitman's Tauberian theorem.
  - Theorem T5: the cross term of the sharp tail vanishes on average.
  - Proposition T6: the open conjectures of the two tail write-ups are one statement about one cross term. It uses two exact moment identities, checked in `checks/denominators_check.out`.
  - The density of the singular set for every $L>\frac12\log6$ (suggested by an internal referee, written out here).
- **Conjecture K7**, the second-order even part of the kink, is an outline by an internal referee. It is not written out and not refereed; it has numerical support (§4.2, §6.1).
- **Scope**, in the final referee's words:
  - "The kink law, to two orders, and the first-order tail law for the localized Weil form are proved, pending external review." (For the kink, "two orders" means the odd part K5 and the edge law K1; the even part at second order is Conjecture K7.)
  - "The second-order per-sector tail term is proved in smoothed form; its sharp-cutoff form is open."

  We do not claim:
  - the sharp per-sector law;
  - $A_e\neq0$ for the true even ground state;
  - anything about RH.

  The laws are asymptotic only, and they are vacuous wherever $A_e=0$. At $L\ge1.2$, $A_e\sim10^{-24}$, so they say nothing at accessible scales.

---

## 0. Summary

### 0.1 In plain words

Let $\psi$ be an eigenfunction of the localized Weil form on the window $(-L,L)$, with eigenvalue $\lambda$. [N] proved two facts about the edges of the window.
- **Edge law.** Near each edge, $\psi$ dies off like $A\cdot(\log\frac1{\text{distance}})^{-1/2}$.
- **Hadamard formula.** The number $A$ (the *edge trace*) controls how fast the eigenvalue falls as the window grows: $d\lambda/dL=-2A^2$.

This note turns two numerically observed consequences into theorems.

**The kink law.**
- The prime terms of the form copy the edge into the interior, at the points $L-\log n$. These are the weak singular points that Eberwein located. The copies are copied again, at points reached by chains of prime shifts.
- Each copy is weaker than its parent by exactly one factor of $\log\frac1d$, where $d$ is the distance to the point.
- At a first copy, $\psi$ stays continuous but has a kink. Measured from its value at the point, it moves by $+\frac23$ of $c_nA\,(\log\frac1d)^{-3/2}$ on one side and by $-\frac13$ of it on the other, with $c_n=\Lambda(n)/\sqrt n$.
  - So the jump across the point is exactly $c_nA\,(\log\frac1d)^{-3/2}$.
  - The profile is **not** one-sided, as an earlier internal audit had stated.
- After $k$ copies the order is $(\log\frac1d)^{-k-1/2}$, and the two sides split as $\frac{k+1}{2k+1}:\frac{-k}{2k+1}$.
- For windows wider than $\log6$ these points are dense. So whenever $A\neq0$, $\psi$ is not Hölder continuous of any positive order on any interval.
- The next correction is also exact. It replaces $\log\frac1d$ by $\log\frac1d-(\lambda+\log2\pi+\gamma)$, and it adds the weight of two-step chains, which is the prime-power "boost".

**The tail law.**
- Weil's explicit formula writes the energy of $\psi$ as a sum over the zeta zeros.
- **First order (proved).** The zeros above height $T$ carry total weight
$$Z(T)\approx\frac{A_+^2+A_-^2}{\pi T}=\frac{|\lambda'(L)|}{\pi T}.$$
  This is a theorem with error $O(1/\log T)$, with no hypothesis on the zeros: off-line zeros are allowed.
- **Second order.** The next correction has relative size $1/\log T$ and two parts:
  - a common part $\lambda/\log T$;
  - when $e^{2L}=X$ is a prime power, a part $\pm\,\Lambda(X)X^{-1/2}/\log T$, with $+$ for even and $-$ for odd eigenfunctions.
- **What is proved at second order:**
  - for smoothed tails, the whole law (Theorem T3);
  - for the sharp tail $Z(T)$, only the main "edge×edge" part (Proposition T4). The remaining "cross" part is shown to be of the same order and to vanish on average (Theorem T5), but not to be smaller.
- Numerics on actual zeta zeros support the full law (§6).

**Not proved:**
- the sharp-cutoff second-order law (Conjecture L);
- any uniformity in $L$ near points where a new prime power becomes active;
- $A_e\neq0$ for the true even ground state, so both laws may be empty there;
- anything about RH.

### 0.2 Results and status

Abbreviations: [N] = the companion note; [TA], [TE], [KW], [KL] = the internal write-ups (see the header). Status:
- **proved** means proved in an internal write-up, internally refereed, and accepted by the internal final referee;
- **proved here** means a new combination in this note, checked only by the internal final referee;
- **conjecture** means not proved.

| # | Statement (short) | Status | Source |
|---|---|---|---|
| Prop R | $2R_q=(\ell+a_q)^{-1}+O(\ell^{-3})$, $V_q=(\ell+a_q)^{-1/2}+O(\ell^{-5/2})$, $a_q=q+\frac\pi2+2\log2$; arg $K(it)=\frac\pi{4\Lambda}+\frac{\pi^3}{24\Lambda^3}+O(\Lambda^{-4})$ | **proved** (two independent proofs) | [KW] Prop R; [KL] Lemmas 3.5, T, V2 |
| K1 | Edge to second order: $\psi(\pm(L-r))=A_\pm(\ell-D)^{-1/2}+O(\ell^{-5/2})$, $D=\lambda+\log2\pi+\gamma$; also $A_\pm V_q+O(V_q^3)$ | **proved** (two write-ups) | [KW] K0, K0′; [KL] Thm A, F1, F(1); existence of $A$: rh_67 (2.2), (3.19) |
| K2 | Graded modulus $\ell^{-\min(g+1/2,N)}$ at generation $g$; $O(\ell^{-N})$ off the chain set | **proved** | [KL] Prop G; [KW] K2.1 |
| K3 | First-order profile at every generation $k$: $\frac{(k+1)W_+-kW_-}{2k+1}$, $\frac{-kW_++(k+1)W_-}{2k+1}$ times $\ell^{-k-1/2}$ | **proved** (two write-ups) | [KL] Thms B, C; [KW] K1, K2 |
| K4 | Singular set dense for $L>\frac12\log6$; if $A\ne0$, $\psi$ Hölder of no positive order on any interval | **proved** (extension to all $L>\frac12\log6$ suggested by an internal referee, written here) | [KL] Cor D; [KW] K3 |
| K5 | Second-order odd part (jump) at every generation: $\Omega_k(\ell-D)^{-k-1/2}+\Omega_{k+1}\ell^{-k-3/2}+O(\ell^{-k-5/2})$ | **proved** ([KL] for all $k$; [KW] independently for $k=1$) | [KL] Thm F(2); [KW] K5 |
| K6 | Jump ratio $1/\rho_n=\ell-D-\beta_n+O(1/\ell)$, prime-power boosts | **proved** for exact point values; the transfer to Galerkin traces is heuristic | [KW] K4, K5; [KL] Cor F′ |
| Conj K7 | Second-order even part: same offset $D$, plus a computable correction $X_{k+1}$ | **conjecture** (outline by an internal referee; numerical support; not written out) | — |
| T0 | Exact contact identity $Z_{\cos}(z)=\lambda(1-\langle\psi,\tau_z\psi\rangle)+\mathcal L(z)+O(z^2)$ | **proved** | [TE] Thm A |
| T1 | Fourier edge law on the strip, canonical main term $\Phi_c=1/(it\sqrt{a-\lambda})$ | **proved** | [TA] Thm B; canonical form suggested by an internal referee |
| T2 | Sharp first-order tail law: $\pi TZ(T)=A_+^2+A_-^2+O_\psi(1/\log T)$, **no hypothesis on the zeros** | **proved** | [TA] Thm C, Cor D |
| T3 | Smoothed second-order per-sector law with rate $\log^{-3/2}$; no Pitman | **proved here** (combines refereed [TA] Thm B and [TE] Thm E) | new |
| T4 | Sharp edge×edge part: $\pi TZ_{MM}=2A^2\,T\!\int_T^\infty\frac{a+\varepsilon c_X}{t^2(a-\lambda)}dt+O(\frac{\log T}T)$ | **proved** | [TA] Prop E1 with the canonical main term |
| T5 | The cross term vanishes on average: smoothed $Z_\times=O(z\ell^{-3/2})$, against $O(z/\ell)$ from Cauchy–Schwarz | **proved here** | new |
| T6 | Pred. F of [TE] $\Leftrightarrow\pi TZ_\times=o(1/\log T)$; Conj. R of [TE] $\Leftrightarrow$ smoothed $Z_\times=O(z\ell^{-3})$ | **proved here** (exact moments $1-\gamma$ and $1+\pi^2/12$) | new |
| Conj L | Sharp per-sector law: $\pi TZ_\times(T)=O(\log^{-3/2}T)$ | **open** | — |
| Conj R | Refined smoothed denominators | **open**; as stated, probably false when $e^{2L}=nm$ (an internal referee's remark) and plausibly whenever a prime power $n<X$ is active (§5.6) | — |

---

## 1. Setting and notation

Everything is as in [N] §1. In brief:
- **Fourier transform.** $F(w)=\int\psi(x)e^{ixw}dx$, so $\|\psi\|^2=\frac1{2\pi}\int|F|^2$.
- **The form.** $Q^{(s)}_L=\mathcal E+w_s$ on $D_L$.
  - $\mathcal E$ is the order-zero jump form with kernel $J=\frac12b$, where $b(u)=2e^{-u/2}/(1-e^{-2u})$, and symbol $\Psi_a(t)=\operatorname{Re}\psi(\frac14+\frac{it}2)-\psi(\frac14)$.
  - $w_s$ (constant $c$, pole of strength $s$, all prime shifts) is independent of $L$ and translation-invariant. It is bounded **on functions supported in a fixed window**, where only finitely many $n$ act ([N] Lemma 3.5). The pole kernel $\cosh\frac{x-y}2$ and the full prime sum are not bounded on $L^2(\mathbb R)$; only the windowed bound is used.
- **The eigenpair.** $A^{(s)}_L$ is the operator. $(\lambda,\psi)$ is any eigenpair: any $L>0$, any $s\in\mathbb R$, any sector, any multiplicity. $\psi$ is real, normalised, continuous on $\mathbb R$, and zero off $(-L,L)$ ([N] Thm 1(1)).
- **Edge traces.** $A_\pm=\lim\psi(\pm(L-r))\ell(r)^{1/2}$ ([N] Thm 1). Put $A:=|A_+|=|A_-|$ ([N] Thm 3(a)) and $\varepsilon:=\operatorname{sgn}(A_+A_-)$, which is $+1$ for even and $-1$ for odd states ($0$ if $A=0$).
- **Logarithms.** $\ell=\ell(r)=\log(1/r)$. On the Fourier side, $\ell_T=\log T$.

**Constants.** Checked in `checks/denominators_check.out`.

| symbol | value | meaning |
|---|---|---|
| $c=\psi(\frac14)-\log\pi$ | $-5.372183$ | constant of $w_s$ |
| $c_a=\gamma+\frac\pi2+2\log2$ | $3.534306$ | $\Psi_a(t)=\log t+c_a+O(1/t)$; $c+c_a=-\log2\pi$ exactly |
| $a(t)=\Psi_a(t)+c=\operatorname{Re}\psi(\frac14+\frac{it}2)-\log\pi$ | $=2\theta'(t)=\log\frac{\lvert t\rvert}{2\pi}+O(t^{-2})$ | full archimedean symbol; $\theta$ is Riemann–Siegel theta |
| $b_0=\log2\pi+\gamma$ | $2.415093$ | universal offset |
| $D=\lambda+b_0$ | | offset of the edge and kink laws. [KL] writes $\beta=-D$; [TE] writes $b_\lambda=D$ |
| $a_q=q+c_a-\gamma=q+\frac\pi2+2\log2$ | $3.957091$ at $q=1$ | renewal offset |
| $c_n=\Lambda(n)/\sqrt n$ | $c_2=0.49013$, $c_3=0.63428$, $c_4=0.34657$, $c_5=0.71976$, $c_7=0.73548$, $c_8=0.24506$, $c_9=0.36620$ | prime weights |
| $X=e^{2L}$, $c_X$ | $c_X=\Lambda(X)/\sqrt X$ if $X$ is a prime power, else $0$ | the shift that carries one edge onto the other |

**Wiener–Hopf objects** ([N] §4). Fix $q>0$ ($q=1$ if nothing is said).
- $\sigma_q=q+\Psi_a$, and $K=K_q$ is the Wiener–Hopf factor: $|K(it)|^2=\sigma_q(t)$, and $1/K(\xi)=\int_0^\infty e^{-\xi x}v(x)dx$.
- $v=v_q$ is completely monotone, and $V=V_q=\int_0^\cdot v$ is the renewal function.
- $r_q$ is the free resolvent kernel, $\hat r_q=1/\sigma_q$, and $R(x)=R_q(x)=\int_0^xr_q$.

**Chains** (notation of [KL]).
- $N_L=\{n:\Lambda(n)\ne0,\ \log n<2L\}$ and $y_n=L-\log n$.
- A chain of length $j$ from $+L$ is a sequence $z_0=L$, $z_i=z_{i-1}\mp\log n_i$ with $n_i\in N_L$ and $z_1,\dots,z_j\in(-L,L)$. Its weight is $\prod c_{n_i}$. Chains from $-L$ are defined in the same way.
- $W^{(j)}_\pm(z):=A_\pm\cdot\sum(\text{weights of length-}j\text{ chains from }\pm L\text{ to }z)$.
- $\Omega_j:=W^{(j)}_+-W^{(j)}_-$ and $\Sigma_j:=W^{(j)}_++W^{(j)}_-$.
- The generation $g(z)$ is the least chain length reaching $z$. $C_L=\{g<\infty\}$, and for $g(z)=k$ write $W_\pm:=W^{(k)}_\pm(z)$.
- [KW] writes $W^\pm_k$ without the factor $A_\pm$.
- $L$ is **generic** if no point is reached from both edges. This holds unless $e^{2L}\in\mathbb Q$, so every nonzero algebraic $L$ is generic, by Hermite–Lindemann. In the generic case $W_-(y_n)=0$.

**Profiles at a point $z$.**
- odd part (jump): $\mathfrak D_\psi(z;d):=\psi(z-d)-\psi(z+d)$;
- even part: $\mathfrak S_\psi(z;d):=\frac12(\psi(z-d)+\psi(z+d))-\psi(z)$;
- so $\psi(z\mp d)-\psi(z)=\mathfrak S\pm\frac12\mathfrak D$.

[KW]'s second difference $\Sigma_p$ is $2\mathfrak S$. The "jump coefficient 1" of [KW] and the "$\kappa=1$" of [KL] mean **unit odd amplitude**. This is unrelated to the project's zero-side normalisation $\kappa=2$.

**Imported from [N].**
- Thm 1 ($\|\psi\|_\infty\le C$, continuity, $\psi(\pm(L-r))=A_\pm V+O(V^2)$, explicit formula for $A_\pm$).
- Thm 2 ($\lambda'=-(A_+^2+A_-^2)$ for a sector-simple $\lambda$).
- Thm 3(a) ($|A_+|=|A_-|$).
- Thm 5 (where $A\ne0$ is known).
- Lemmas 3.2–3.4, 4.1–4.5, Prop 5.1, Lemma 5.2, Lemma 6.1, and the interior localisation of §7 step 5.

Constants $C$ below may depend on $L$, $s$, $|\lambda|$, $q$, the point considered and the gaps to activation points. **Nothing is uniform in $L$.**

---

## 2. One structure for a paper

### 2.1 Dependency graph

```
[N] §§3–6: Dirichlet form, Wiener–Hopf factor, half-line inversion, L^∞ bound
   └── Thm 1 (E) edge law ──────────────┬── Thm 2 (H) Hadamard ── Thm 5 nonvanishing
         │                              └── Thm 3 translation identity (|A+|=|A-|)
         │   Thm 4 pure log (A² = 1/(2L), simplicity)   [companion paper in preparation]
         │
         ├── Prop R (renewal to 2nd order) + Lemma T (phase of K)
         │       └── K1 edge law to 2nd order (A(ℓ−D)^{-1/2})
         │
         ├── transfer lemmas (modulus, profile, odd/even 2nd order) + interior localisation
         │       └── K2 moduli → K3 kink law (all generations) → K4 density/roughness
         │                        └── K5 2nd-order jump (+K1) → K6 jump ratio; Conj K7 even part
         │
         └── zero side: explicit formula on D_L ([TE] Lemma A.1 / [TA] Lemma W)
                 ├── T0 contact identity (uses eigen-equation only)
                 │      └── [TE] Thm E contact law to 2nd order (uses K1-type germ, interior modulus)
                 ├── T1 Fourier edge law (uses [N] Prop 5.1 etc.)
                 │      ├── T2 sharp first-order tail law (+ Riemann–von Mangoldt, Landau)
                 │      ├── T4 sharp edge×edge 2nd order
                 │      └── T3(a) translation norm with rate ─┐
                 └── T3 smoothed 2nd-order law (Thm E + T3(a)) ┴── T5 cross term on average, T6
```

**What is used where.**
- The kink law uses (E) and Thm 3(a), but not (H).
- The tail law uses (E) and Thm 3(a). It uses (H) only to rewrite $A_+^2+A_-^2$ as $|\lambda'|$. It uses the kink-law moduli in [TE] Thm E, and [KL] Thm F only for refined denominators.
- Neither law uses RH.

### 2.2 Papers

A companion paper on the pure-log case (Theorem 4 of [N]) is in preparation. A natural split of the rest is an operator paper (no zeros: [N] §§1–11 with §§3–4 here) and a zero-side paper (§5 here), which depends on it.

---

## 3. Common tools

### 3.1 Free Green function and localisation

**Lemma G** ([KL] Lemma 3.1; [KW] Lemma 3.1).
- $r_q=\tilde v*v=\int_0^\infty g_s\,u_q(s)\,ds$, a mixture of centred Gaussians $g_s$ with completely monotone weight $u_q$, $\int u_q=1/q$. (This is Bochner subordination, since $\Psi_a(t)=\varphi(t^2)$ with $\varphi$ a CBF.)
- Hence $r_q$ is even, positive and strictly decreasing on $(0,\infty)$.
- Moreover:
  - $R(x)=\int_0^\infty v(y)\,(V(y+x)-V(y))\,dy$;
  - $x\,r_q(x)\le2R(x)$;
  - $\|r_q(\cdot+h)-r_q\|_1=4R(|h|/2)$;
  - $v(x)\le C\ell^{-3/2}/x$ and $r_q(x)\le C\ell^{-2}/x$.

**Lemma Loc (interior localisation)** ([N] §7 step 5; [KL] Lemma 3.2; [KW] Lemma 3.4). Let $z\in(-L,L)$ and $\chi_1\in C_c^\infty(-L,L)$ with $\chi_1=1$ near $z$. Then $\chi_1\psi=r_q*f_1$, with $f_1\in L^2\cap L^\infty$, and near $z$
$$f_1=(q+\lambda-c)\psi-2s\!\int\!\cosh\tfrac{\cdot-y}2\psi(y)dy+\sum_{n\in N_L}c_n\big(\psi(\cdot+\log n)+\psi(\cdot-\log n)\big)+\text{Lipschitz}.$$
The shift $c_n\psi(x+\log n)$ is cut off at $x=y_n$; as $x\uparrow y_n$ it equals the edge germ $c_n\psi(L-(y_n-x))$. This is the whole mechanism of the kink law.

### 3.2 The renewal function to second order (two independent proofs)

**Proposition R.** For every $q>0$, with $a_q=q+c_a-\gamma$, as $x\downarrow0$:
- (R1) $0\le R(x)-\frac12V(x)^2\le C\ell^{-3}$.
- (R2) $R(x)=\frac1\pi\int_0^\infty\frac{\sin xt}{t\,\sigma_q(t)}dt=\frac1{2(\ell+a_q)}+O(\ell^{-3})$. More precisely $2R=(\ell+B)^{-1}+\gamma(\ell+B)^{-2}+O(\ell^{-3})$, with $B=q+c_a$.
- (V2) $V(x)=(\ell+a_q)^{-1/2}+O(\ell^{-5/2})$, i.e. $V^{-2}=\ell+a_q+O(\ell^{-1})$.

This proves [N]'s numerical observation N8.

*Proof of (R1)* ([KW]; a lemma supplied by an internal referee). By Lemma G, $R(x)=\int_0^\infty v(y)(V(y+x)-V(y))dy$.
- On $(0,x)$, write $V(y+x)-V(y)=[V(x)-V(y)]+[V(y+x)-V(x)]$.
  - The first bracket integrates exactly to $V(x)^2-\frac12V(x)^2=\frac12V(x)^2$.
  - The second is $\ge0$, and by concavity it is $\le y\,v(x)$. So it contributes at most $v(x)\int_0^xy\,v\le C\ell^{-3/2}x^{-1}\cdot Cx\ell^{-3/2}$.
- On $(x,\infty)$, concavity gives $0\le V(y+x)-V(y)\le x\,v(y)$, and $x\int_x^\infty v^2\le C\ell^{-3}$. ∎

*Proof of (R2)*, two independent proofs.
- **[KW] Lemma 3.5.** Parseval with a Gaussian mollifier, then an Abel limit, using that $1/(t\sigma_q)$ is decreasing and the second mean value theorem. Then expand with [N] Lemma 4.3(b) and the Dirichlet integrals
$$\int_0^\infty\frac{\sin s}s\,ds=\frac\pi2,\qquad\int_0^\infty\frac{\sin s\log s}s\,ds=-\frac{\pi\gamma}2 .$$
- **[KL] Lemma 3.5.** A positive Si-representation, $2R(x)=\frac2\pi\int_0^\infty\operatorname{Si}(xt)\,\mu(dt)$ with $\mu=-d(1/\sigma_q)\ge0$. In logarithmic variables, the constant is $\int_{\mathbb R}(\mathbf 1_{\tau>0}-\frac2\pi\operatorname{Si}(e^\tau))d\tau=-\gamma$. ∎

*Proof of (V2)*, two independent proofs.
- **(i)** From (R1) and (R2): $V^2=2R+O(\ell^{-3})=(\ell+a_q)^{-1}+O(\ell^{-3})$.
- **(ii)** ([KL] Lemma V2, independent of (R1) and (R2).)
  - Bromwich inversion of $\int e^{-\xi x}dV=1/K(\xi)$, moved onto the imaginary axis. There $|1/K(it)|=\sigma_q(t)^{-1/2}$ exactly, so only the phase needs asymptotics.
  - **Lemma T** ([KL] §8.2): $\theta(t)=\arg K(it)=\frac\pi{4\Lambda_t}+\frac{\pi^3}{24\Lambda_t^3}+O(\Lambda_t^{-4})$ with $\Lambda_t=\log t+B$, and $|t\theta'|\le C/\Lambda_t$.
  - It follows from the conjugate-function formula $\theta(t)=\frac1\pi\int\log\frac{\sigma_q(te^v)}{\sigma_q(t)}\frac{dv}{2\sinh v}$, with the moments $\int\frac{v}{2\sinh v}=\frac{\pi^2}4$, $\int\frac{v^2}{2\sinh v}=0$, $\int\frac{v^3}{2\sinh v}=\frac{\pi^4}8$.
  - Gap note (an internal referee): for $s\ge2t+1$ the kernel is dominated by $2t/(s-t)^2$, uniformly in the regularisation. ∎

*Remarks.*
- **Not new.** The $-\gamma$ correction is the classical Euler-constant term of de Haan theory (Bingham–Goldie–Teugels, *Regular Variation*, Ch. 3; theorem number not confirmed). What appears new (not found in our literature search, §7) is the explicit $O(\ell^{-5/2})$ remainder and its use in the eigenfunction expansions.
- **Numerically sharper.** Internal referee computations find $R-\frac1{2(\ell+a_q)}\approx\frac{\pi^2}{24}\ell^{-3}$ and $V^{-2}-\ell-a_q=O(\ell^{-2})$ (Gaver–Stehfest). Nothing below depends on this.

### 3.3 Transfer lemmas

Let $r$ be even, $\ge0$, integrable and decreasing on $(0,\infty)$, with $R(x)\le C/\ell(x)$.

**Lemma M (one-log gain)** ([KL] Lemma 3.3(ii); [KW] Lemma 3.2). Suppose $R(x)\le C_R/\ell(x)$ for $x\le x_R$. Let $\alpha>0$, $0<\delta\le\min(x_R,e^{-(\alpha+2)})$, $f\in L^\infty$, and $|f(z+y)-f(z)|\le M\ell(|y|)^{-\alpha}$ for a.e. $|y|\le\delta$. Then for $0<|h|\le h_0(\delta)$, $|(r*f)(z+h)-(r*f)(z)|\le C(\alpha,C_R,\delta,r)\,(M+\|f\|_\infty)\,\ell(|h|)^{-\alpha-1}$. The case $\alpha=0$ (used in the proof of K1(a)) needs no regularity of $f$: for $r$ even and decreasing on $(0,\infty)$, $\int|r(y-h)-r(y)|\,dy=4R(|h|/2)$, so the difference is at most $4C_R\|f\|_\infty/\ell(|h|)$ for $|h|\le\min(1,2x_R)$.

*Proof.* Since $r$ is even and has total mass, $u(z+h)-u(z)=\int(r(h-y)-r(y))(f(z+y)-f(z))dy$. Split into $|y|\le2h$, $2h<|y|\le\delta$ (monotonicity of $r$ and of $\omega'(w)=\alpha Mw^{-1}\ell^{-\alpha-1}$; split at $\sqrt h$), and $|y|>\delta$. ∎

**Lemma P (profile transfer, first order)** ([KL] Lemma 3.4; [KW] Lemma 3.3). Suppose also $|R(x)-\frac1{2\ell(x)}|\le C\ell^{-2}$. Let $g$ be the one-sided germ $\ell(-y)^{-a}\mathbf 1_{(-\delta,0)}(y)$. Then $w=r*g$ satisfies
$$w(-d)-w(0)=\tfrac{2a+1}{2(a+1)}\ell^{-a-1}+O(\ell^{-a-2}),\qquad w(d)-w(0)=-\tfrac1{2(a+1)}\ell^{-a-1}+O(\ell^{-a-2}).$$
So a germ $(\sigma_-,\sigma_+)_a$ goes to $(\sigma'_-,\sigma'_+)_{a+1}$ with $\sigma'_--\sigma'_+=\sigma_--\sigma_+$ (the odd part is preserved) and $\sigma'_-+\sigma'_+=\frac a{a+1}(\sigma_-+\sigma_+)$.

*Proof.* With $\phi=\ell^{-a}$, Fubini gives
$$w(x)-w(0)=-\int_0^\delta\phi'(\tau)\big[\mathcal R(x+\tau)-\mathcal R(\tau)\big]d\tau+O(|x|),$$
where $\mathcal R$ is the odd extension of $R$.
- At $x=-d$ the integral is $T_1+T_2+T_3$:
  - $T_1=\int_0^d\phi'R=\frac a{2(a+1)}\ell^{-a-1}$;
  - $T_2=\int_0^d\phi'(\tau)R(d-\tau)d\tau=\frac12\ell^{-a-1}$;
  - $T_3=O(\ell^{-a-2})$.
- At $x=+d$ it is $T_1-T_2'-T_3'$, with $T_2'=\frac12\ell^{-a-1}$. ∎

**Lemma O (odd transfer, second order)** ([KL] Lemma 3.6; [KW] Lemma 3.7, "jump lemma J", an independent formulation). Suppose $2R=(\ell+b)^{-1}+O(\ell^{-3})$ and the odd part of the source satisfies
$$\mathfrak D_f(z;y)=\sum_jW_j(\ell(y)+\beta_j)^{-a_j}+O(\ell^{-a-2}),\qquad a_j\ge a .$$
Then $\mathfrak D_{r*f}(z;d)=2R(d)\sum_jW_j(\ell(d)+\beta_j)^{-a_j}+O(\ell^{-a-3})$.

*Core of the proof.*
- **Step 0 (odd reduction).** Since $r$ is even, $u(z-x)-u(z+x)=2(r*G)(x)$, where $G$ is the odd part of $f$ about $z$. **Odd and even parts never couple.**
- **Step 1.** For a germ $\Phi$, $w(-d)-w(d)=\int_0^\delta\Phi'(\tau)M_d(\tau)d\tau+O(d)$, where $M_d(\tau)=\int_{\tau-d}^{\tau+d}r\ge0$ is the window mass.
- **Step 2.** Split into $\tau\le d$, $d<\tau\le\ell d$ and $\tau>\ell d$:
  - the first range gives $2R(d)\Phi(d)$ plus a bracket of size $O(\ell^{-a-3})$;
  - the other two ranges are $O(\ell^{-a-3})$.
- The third-order constant is $a\pi^2/12$. An internal referee derived it, and it matches a model-kernel computation (re-done independently by the final referee). ∎

**Lemma O′ (even transfer, second order; outline by an internal referee).** Since $r$ is even, $\mathfrak S_{r*f}(x)=\int[\frac12(r(x-y)+r(x+y))-r(y)]\,\mathfrak S_f(y)\,dy$, so even parts also never couple to odd parts. For $\mathfrak S_f=\sigma(\ell+\beta_0)^{-a}+O(\ell^{-a-2})$,
$$\mathfrak S_{r*f}(d)=\sigma a\!\int_\ell^\infty\!\frac{dm}{(m+b)(m+\beta_0)^{a+1}}+O(\ell^{-a-3})=\tfrac a{a+1}\sigma\Big(\ell+\tfrac{b+(a+1)\beta_0}{a+2}\Big)^{-a-1}+O(\ell^{-a-3}).$$
- In Lemma P's notation, the even part is $T_1+\frac12(T_2-T_2')+\frac12(T_3-T_3')$.
- $T_1$ is the displayed integral; the other two are $O(\ell^{-a-3})$ by the same range bounds as in Lemma O.
- Model-kernel check: the residual tends to $-a\pi^2/24$.
- **Status:** outline only, written by a referee; not yet written out in full or refereed.

---

## 4. The kink law

### 4.1 Statements

Setting of §1: any $L>0$, any $s$, any eigenpair, $A_\pm$ allowed to vanish. All asymptotics are as $d\downarrow0$ (or $r\downarrow0$), with $\ell=\ell(d)$. Constants are pointwise: they depend on $L$, the point and the gaps. Nothing uses the zeros, so nothing depends on RH.

**Theorem K1 (edge law, sharp and to second order).** For every $q>0$:
- (a) $\psi(\pm(L-r))=A_\pm V_q(r)+O(V_q^3)=A_\pm\ell^{-1/2}+O(\ell^{-3/2})$;
- (b) $\psi(L-r)=A_+\big[V_q+\frac{q+\lambda-c}2V_q^3\big]+O(V_q^5)$;
- (c) $\psi(\pm(L-r))=A_\pm(\ell-D)^{-1/2}+O(\ell^{-5/2})=A_\pm\ell^{-1/2}\big(1+\frac D{2\ell}\big)+O(\ell^{-5/2})$, with $D=\lambda+\log2\pi+\gamma$.

Part (a) closes [N] §12 open item 4.

**Proposition K2 (graded moduli).** Let $\mu_p(t)=\sup_{0<|w|\le t}|\psi(p+w)-\psi(p)|$. For every $N$ there are $t_0(p,N)$ and $C(p,N)$ with
$$\mu_p(t)\le C(p,N)\,\ell(t)^{-\min(g(p)+\frac12,\,N)}\qquad(0<t\le t_0(p,N)).$$
Off $C_L$ the modulus is $O(\ell^{-N})$ for every $N$. This is not $C^\infty$, and not even Hölder; nothing more is claimed.

**Theorem K3 (kink law, first order, every generation).** Let $g(z)=k\ge1$ and $W_\pm=W^{(k)}_\pm(z)$. Then
$$\psi(z-d)-\psi(z)=\frac{(k+1)W_+-kW_-}{2k+1}\,\ell^{-k-1/2}+O(\ell^{-k-3/2}),\qquad\psi(z+d)-\psi(z)=\frac{-kW_++(k+1)W_-}{2k+1}\,\ell^{-k-1/2}+O(\ell^{-k-3/2}).$$
Equivalently, $\mathfrak D_\psi=\Omega_k\ell^{-k-1/2}+\dots$ (unit odd amplitude in every generation) and $\mathfrak S_\psi=\frac{\Sigma_k}{2(2k+1)}\ell^{-k-1/2}+\dots$

*First generation, generic $L$* ($W_+=c_nA_+$, $W_-=0$), with error $O(\ell^{-5/2})$:
$$\psi(y_n-d)-\psi(y_n)=\tfrac23c_nA_+\ell^{-3/2},\qquad\psi(y_n+d)-\psi(y_n)=-\tfrac13c_nA_+\ell^{-3/2}.$$
- The jump is $c_nA_+\ell^{-3/2}$, with the sign of $A_+$ and the larger excursion on the source side $y<y_n$.
- The side ratio tends to $-2$.
- An earlier internal audit's target form "smooth $+\,c_nA\mathbf 1_{y<y_n}\ell^{-3/2}$" holds **only if** the smooth part may contain the even cusp $-\frac13c_nA\ell^{-3/2}$.

*Coincidence $e^{2L}=nm$* ($y_n=-y_m$): $W_-=c_mA_-$ in the same formula.

*Mirror points:* by reflection.

*Examples, generation 2:*
- $L-\log6$ for $L>\frac12\log6$: $W_+=2c_2c_3A_+=0.6218A_+$ (chains $2\to3$, $3\to2$);
- $L-\log\frac32$: $W_+=c_2c_3A_+$, provided no other chain lands there.

**Corollary K4 (singular set).**
- (a) If $g(z)<\infty$ and $(W_+,W_-)\ne(0,0)$, then $\mu_z(t)\asymp\ell(t)^{-g(z)-1/2}$, and $\psi$ is not differentiable at $z$.
- (b) For $\zeta$ ($c_n>0$) and **any** eigenfunction with $A_+\ne0$, every point of $C_L$ is as in (a). By [N] Thm 3(a), $A_-=\pm A_+$:
  - if $A_-=A_+$, the even part $\propto\Sigma_k\ne0$;
  - if $A_-=-A_+$, the odd part $\propto\Omega_k\ne0$.
- (c) If $L>\frac12\log6$, then $C_L$ is dense in $(-L,L)$. Hence, if $A_+\ne0$, $\psi$ is Hölder continuous of **no positive order** on any open subinterval; in particular it is Lipschitz on none.
- (d) If $2L\le\log2$, then $C_L=\varnothing$.
- (e) *Where $A\ne0$ is known.*
  - the ground state for $s\le0$, at every $L$ ([N] Thm 5(a));
  - for $s=1$, the ground state off a closed nowhere-dense set of $L$ in $(\frac12\log6,1.19)$ ([N] Thm 5(d), conditional on the certified simple-even input [GS]).
  - **At a given $L$ for the true even ground state it is open.**

**Theorem K5 (second order, odd part, every generation).** Let $g(z)=k\ge1$. Then
$$\mathfrak D_\psi(z;d)=\Omega_k(z)\,(\ell-D)^{-k-1/2}+\Omega_{k+1}(z)\,\ell^{-k-3/2}+O(\ell^{-k-5/2}).$$
Here $\Omega_{k+1}(z)$ counts all chains of length $k+1$ ending at $z$, including non-minimal ones and mixed-sign ones. If $\Omega_k\ne0$, this is $\Omega_k(\ell+\beta_{\rm eff})^{-k-1/2}(1+O(\ell^{-2}))$ with $\beta_{\rm eff}=-D-\Omega_{k+1}/((k+\frac12)\Omega_k)$.

**Corollary K6 (jump ratio).** Let $n\in N_L$, $W_-(y_n)=0$ and $A_+\ne0$, and put $\rho_n(d):=\mathfrak D_\psi(y_n;d)/(c_n\psi(L-d))$. Then
$$\frac1{\rho_n(d)}=\ell-D-\beta_n+O(\ell^{-1}),\qquad\beta_n:=\frac{\Omega_2(y_n)}{c_nA_+}.$$
- **Prime-power boost.** For $n=p^j$, the chains $L\to L-\log p^i\to y_n$ give $\beta_n\ge(j-1)\log p$. Mixed-sign chains count too: for example $(-\log4,+\log2)$ lands on $y_2$ when $L>\log2$.
- **Boost table** ([KW] K5; recomputed in [NUM] `numerics/prereg_table.out` and by the final referee):

| $L$ | $\beta_2$ | $\beta_3$ | $\beta_4$ | $\beta_5$ | $\beta_7$ | $\beta_8$ | $\beta_9$ | $\beta_{16}$ |
|---|---|---|---|---|---|---|---|---|
| 1.0 | 0.347 | 0 | 0.693 | 0 | 0 | — | — | — |
| 1.19 | 0.520 | 0.366 | 1.040 | 0 | 0 | 1.386 | 1.099 | — |
| 1.5 | 0.607 | 0.366 | 1.213 | 0 | 0 | 1.733 | 1.099 | 2.079 |

- **True form, $L=1.19$, $\lambda\approx0$** (corrected after an internal referee's report): $1/\rho_n=\ell-2.41509-\beta_n+O(1/\ell)$, **if $A_e\ne0$**. Only $p=5,7$ have $\beta=0$; the ratio chains $4\to2$, $8\to4$ and $9\to3$ give $\beta_2=0.520$ and $\beta_3=0.366$.
- **Exact point samples.** If the samples sit at distances $\theta_nh$ and $\theta_eh$, then
$$1/\rho(h)=\ln\tfrac1h-D-\beta_n+\tfrac12\big(3\log\tfrac1{\theta_n}-\log\tfrac1{\theta_e}\big)+O(1/\ln\tfrac1h).$$
- **Galerkin endpoint values** (earlier internal Galerkin runs) are not shown to be point samples. For them the law $1/(\ln\frac1h+b)$ is a consistent **heuristic**.
- **Echo at $L-\log6$** (corrected after an internal referee's report): the jump ratio to $c_2c_3\psi(L-d)$ is $(2c_2c_3A_+-W^{(2)}_-)/(c_2c_3A_+)\cdot\ell^{-2}$. It equals $2\ell^{-2}$ only when no chain of length $\le2$ from $-L$ ends at $L-\log6$. That fails, for example, at $L=\frac12\log7.5$ and at $L=\log3$, both in the certified range.

**Conjecture K7 (second order, even part).** *An outline by an internal referee; not written out and not refereed. The final referee asked that it stay a conjecture; numerical support in §6.1.* Let $g(z)=k\ge1$. Then
$$\mathfrak S_\psi(z;d)=\frac{\Sigma_k(z)}{2(2k+1)}(\ell-D)^{-k-1/2}+X_{k+1}(z)\,\ell^{-k-3/2}+O(\ell^{-k-5/2}),$$
$$X_{k+1}(z)=\frac{2k+1}{2k+3}\Big[\sum_{g(P)=k-1}c_n\,X_k(P)+\frac1{2(2k+1)}\sum_{g(P)=k}c_n\,\Sigma_k(P)\Big],\qquad X_1(\pm L)=0 .$$
Both sums run over $P=z+\varepsilon\log n$. The offset is the same $D$ as for the odd part.

### 4.2 Proofs

The detailed estimates are in the internal write-ups [KL] §§4–8 and [KW] §§3–5, which are not included here. Both were internally refereed, and the internal final referee re-checked the steps below. Here is the logic, and the places where the two write-ups supply each other.

**Proof of K1(a)** ([KL] §4; [KW] Thm K0).
- Write $u=\chi\tilde\psi=\int_0^xv(x-z)k(z)dz$ with $k(z)=\int_0^\infty v(t)f_+(t+z)dt$ and $A_+=k(0)$ ([N] Lemma 5.2).
- **Step 1 (source near the edge).** For $t$ small,
$$f_+(t)=(q+\lambda-c)\tilde\psi(t)-P_s\tilde\psi(t)+\sum_nc_n\psi(y_n-t)+r_\chi[\tilde\psi]{(t)}.$$
  - $|\tilde\psi|\le CV$ ([N] Thm 1).
  - $|\psi(y_n-t)-\psi(y_n)|\le C/\ell=O(V^2)$ (Lemma Loc and Lemma M with $\alpha=0$).
  - The rest is Lipschitz.

  So $|f_+(t)-F_0|\le CV(t)$, with $F_0=f_+(0+)$.
- **Step 2.** Because $v\in L^1$, the constant $F_0$ drops out of $k(z)-k(0)$. Splitting at $z$, $2z$, $\sqrt z$ and $a_1$ gives $k(z)-k(0)=O(V(z)^2)$.
- **Step 3.** $|u-A_+V|\le\int_0^xv(x-z)CV(z)^2dz\le CV(x)^3$. ∎

**Proof of K1(b)** ([KL] Prop F1).
- Redo Step 1 with Theorem K3 at generation 1 (moduli $O(\ell^{-3/2})=O(V^3)$) and K1(a): $f_+-F_0=(q+\lambda-c)A_+V+O(V^3)$.
- Then use $\int_0^\infty v(t)(V(t+z)-V(t))dt=\frac12V^2+O(V^4)$ and $\int_0^xv(x-z)V(z)^2dz=V(x)^3+O(V^5)$.
- *Circularity check:* the induction runs K2 → K1(a) → K3 at generation 1 → K1(b). There is no circularity. ∎

**Proof of K1(c)** (two write-ups). Assume $A_+\ne0$; if $A_+=0$, (b) gives $\psi=O(V^5)$.
- *By (b) and (V2) ([KL] Thm F(1)):*
$$A_+^2\psi(L-r)^{-2}=V^{-2}-(q+\lambda-c)+O(\ell^{-1})=\ell+a_q-q-\lambda+c+O(\ell^{-1}).$$
  Since $a_q-q+c=c_a+c-\gamma=-\log2\pi-\gamma$, this is $\ell-D+O(\ell^{-1})$, and the $O(\ell^{-5/2})$ form follows.
- *By [KW] Thm K0′:*
  - $\psi(L-r)=A_+[V+(q+\lambda-c)V\!R]+O(\ell^{-5/2})$. This uses the exact identity $\int\theta_zV=R(z)$ and the bound $\int v(x-z)(R(x)-R(z))dz=O(\ell^{-7/2})$.
  - Then (R2) and (V2) give the result.
  - An internal referee checked the new $O(\ell^{-5/2})$ step. ∎

**Proof of K2** ([KL] §5; [KW] §4). Induction on $N$.
- Localise at $p$ with a radius below the thresholds $t_0(p',N)$ of the finitely many images $p'=p\pm\log n$.
- An image $p'$ is either outside the window (contributes nothing), or an edge (only if $g(p)=1$; modulus $CV$), or an interior point with $g(p')\ge g(p)-1$ (induction hypothesis).
- Lemma M adds one logarithm. ∎

**Proof of K3** ([KL] §6; [KW] §5). Induction on $k$, with the edges as generation $0$: germs $(A_+,0)_{1/2}$ at $L$ and $(0,A_-)_{1/2}$ at $-L$ (K1(a)).
- At $z$ with $g(z)=k$, the source $f_1$ (Lemma Loc) has:
  - the germs of its generation-$(k-1)$ images, translated with orientation preserved;
  - the self term $(q+\lambda-c)\psi$ and the images of generation $\ge k$, whose moduli are $O(\ell^{-k-1/2})$ by K2;
  - Lipschitz rest.
- Lemma P maps the germ sums $\Sigma_\mp$ to $\sigma'_-=\frac{2k\Sigma_--\Sigma_+}{2k+1}$ and $\sigma'_+=\frac{-\Sigma_-+2k\Sigma_+}{2k+1}$. Lemma M handles the rest.
- Insert the generation-$(k-1)$ profiles, and use $W_\pm(z)=\sum_{g(P)=k-1}c_nW_\pm(P)$.
- Why the constants come out as they do:
  - the odd part is preserved exactly (Lemma O, first-order variant);
  - the even part starts at $\frac12$ of the edge germ and is multiplied by $\frac{j-1/2}{j+1/2}$ at step $j$, so it is $\frac1{2(2k+1)}$ after $k$ steps. ∎

**Proof of K4.**
- (a) The matrix $\begin{pmatrix}k+1&-k\\-k&k+1\end{pmatrix}$ has determinant $2k+1\ne0$, and $\ell(d)^{-k-1/2}/d\to\infty$.
- (b) As stated above.
- (c) This is a sliding-window argument suggested by an internal referee, written out here.
  - For $a\in(-L+\log6,L]$ put $\mathcal W_a=[a-\log6,a)\subset(-L,L)$.
  - Let $T_a(x)=x+\log2$ if $x+\log2<a$, and $T_a(x)=x-\log3$ otherwise. This is the rotation by $\log2$ of the circle $\mathcal W_a\cong\mathbb R/\log6\,\mathbb Z$. Each step is a legal chain step that stays in $(-L,L)$, and $\log2/\log6\notin\mathbb Q$.
  - So if $\mathcal W_a$ contains one chain point, chain points are dense in $\mathcal W_a$.
  - $\mathcal W_L$ contains $y_2$. If $|a-a'|<\log6$, then $\mathcal W_a\cap\mathcal W_{a'}$ has interior, so density passes from $a$ to $a'$.
  - Sliding $a$ down to $-L+\log6$ covers $(-L,L)$.
  - Every chain point is then a singular point of exact order $\ell^{-g-1/2}$ (by (b)). Since $\ell(t)^{-m}\gg t^\alpha$ for every $\alpha>0$, no Hölder bound can hold on any interval.
- (d) $N_L=\varnothing$.
- (e) [N] Thm 5. ∎

**Proof of K5** ([KL] §8.4, all $k$; [KW] §5, $k=1$, via the jump lemma J). Induction on $k$, with $a:=k-\frac12$. The base case is K1(c), read as $\mathfrak D_\psi(\pm L;d)=\Omega_0(\pm L)(\ell-D)^{-1/2}+0\cdot\ell^{-3/2}+O(\ell^{-5/2})$.
- **Step 1 (source odd part).** By Lemma Loc,
$$\mathfrak D_{f_1}(z;y)=(q+\lambda-c)\mathfrak D_\psi(z;y)+\sum c_n\mathfrak D_\psi(P;y)+O(y),\qquad P=z+\varepsilon\log n .$$
  Sort the images:
  - images of generation $k-1$ carry $\Omega_{k-1}(P)(\ell-D)^{-a}+\Omega_k(P)\ell^{-a-1}$ (induction hypothesis);
  - images of generation $k$ carry $\Omega_k(P)\ell^{-a-1}$ (K3);
  - higher generations are $O(\ell^{-a-2})$ (K2).

  With the chain identities $\Omega_k(z)=\sum_{g(P)=k-1}c_n\Omega_{k-1}(P)$ and $\Omega_{k+1}(z)=\sum_{g(P)\in\{k-1,k\}}c_n\Omega_k(P)$ ([KL] (1.2)):
$$\mathfrak D_{f_1}=\Omega_k(\ell-D)^{-a}+\big[\Omega_{k+1}+(q+\lambda-c)\Omega_k\big]\ell^{-a-1}+O(\ell^{-a-2}).$$
- **Step 2 (inversion).** Lemma O with $b=a_q$ (from R2) gives
$$\mathfrak D_\psi=\Omega_k(\ell+a_q)^{-1}(\ell-D)^{-a}+[\Omega_{k+1}+(q+\lambda-c)\Omega_k]\ell^{-a-2}+O(\ell^{-a-3}).$$
- **Step 3 (exact cancellation).** $(\ell+a_q)^{-1}(\ell-D)^{-a}=(\ell-D)^{-a-1}-(a_q+D)\ell^{-a-2}+O(\ell^{-a-3})$, and
$$a_q+D=q+c_a-\gamma+\lambda+\log2\pi+\gamma=q+\lambda-c .$$
  So the $(q+\lambda-c)$ terms cancel and $q$ drops out.
- *Fixed-point reading:* the offset rule is $D'=\frac{aD_0+(q+\lambda-c)-a_q}{a+1}$, and $D$ is its fixed point at every generation. ∎

*Remark (the two write-ups supply each other).* [KW] had (R1) and (R2) but proved K5 only at $k=1$, through the jump lemma. [KL] had Lemma O and the chain bookkeeping for all $k$, and an independent V2. An internal referee confirmed the bookkeeping. Together:
- K1(c) and Prop R have two independent proofs each;
- K5 at $k=1$ has two independent proofs;
- K5 for $k\ge2$ has one.

**Proof of K6.**
- Divide K5 at $k=1$ by $c_n\psi(L-d)=c_nA_+(\ell-D)^{-1/2}(1+O(\ell^{-2}))$.
- The boost: $\sum_{i=1}^{j-1}c_{p^i}c_{p^{j-i}}=(j-1)\log p\cdot c_{p^j}$.
- Point samples: expand $\ell(\theta h)=\ln\frac1h+\log\frac1\theta$. ∎

**Status of K7 (a conjecture).**
- The even transfer (Lemma O′) and the even fixed point were derived by an internal referee. They have not been written out in full, and no referee has checked them.
- Numerical support is strong: with no free parameter, all 15 P0 cases agree to $\le0.015$ on $\ell\in[20,85]$. That includes the three $L=0.75$ points with $X\ne0$, where the predicted fitted offsets were $0.409$, $0.547$, $0.488$ and the measured ones $0.411$, $0.550$, $0.496$.

### 4.3 What the kink law does not give

- **Uniformity in $L$.** Constants blow up as $y_n\to-L$ (just after an activation) and where chain points merge. In particular an earlier numerically observed "$X=8$ slope feature" is not addressed. Generation-1 merging ($y_2$ with $-y_4$) is the only continuum candidate, and the $X=10$ control ($y_2$, $-y_5$) disfavours it.
- **$C^\infty$ off the closure of $C_L$.** Only $O(\ell^{-N})$ moduli are proved there.
- **Third order** ($W_3$ terms).
- **Other $L$-functions.** For $\chi_5$ or Davenport–Heilbronn forms, chains of equal length can cancel, and $D$ must be replaced by that form's constants ($c+c_a-\gamma$ changes, and there is no pole).
- **Galerkin traces.** The transfer to them is heuristic.

---

## 5. The tail law

### 5.1 Zero-side objects

- $\gamma_\rho=-i(\rho-\frac12)=t_\rho+iy_\rho$ with $|y_\rho|<\frac12$, counted with multiplicity.
- $h(w)=F(w)F(-w)=\hat g(w)$, where $g=\psi*\tilde\psi$. Under RH, $h(\gamma_\rho)=|F(t_\rho)|^2$.
- **Sharp tail:** $Z(T)=\sum_{|t_\rho|>T}h(\gamma_\rho)$.
- **Cosine tail:** $Z_{\cos}(z)=\sum_\rho h(\gamma_\rho)(1-\cos z\gamma_\rho)$.
- **Smoothed tail:** for an even finite signed measure $\varphi$ on $[-1,1]$ with $\varphi(\mathbb R)=1$, put $\Phi(w)=\int\cos(wz)d\varphi$, $Z_\varphi(T)=\sum_\rho h(\gamma_\rho)(1-\Phi(\gamma_\rho/T))$ and $m_1(\varphi)=\int_{(0,\infty)}z\,d\varphi$.
  - Cosine kernel: $m_1=\frac12$. Fejér kernel: $m_1=\frac16$.
- **Smooth (zero-free) analogue:** $E(T)=\frac1\pi\int_T^\infty a|F|^2dt$.

All of these zero sums converge absolutely, and $Z$ is real, with no hypothesis on the zeros ([TA] Lemma W; [TE] Lemma A.1). Moreover
$$\sum_\rho h(\gamma_\rho)=\lambda+2(1-s)F(\tfrac i2)F(-\tfrac i2).$$
So the "share" reading $S(T)=1-Z(T)/\lambda$ needs $s=1$. [TA] Lemma W needs one more line, as an internal referee noted: sum the blocks of Lemma Z against the weight $\log(2+|t|)$.

**Canonical main term** (suggested by an internal referee). For $|t|\ge t_0$ (so that $a-\lambda\ge1$), put
$$\Phi_c(t)=\frac1{it\sqrt{a(t)-\lambda}},\qquad M(t,y)=A_+e^{iL(t+iy)}\Phi_c(t)+A_-e^{-iL(t+iy)}\Phi_c(-t),\qquad R=F-M .$$
At a zero, $M(\gamma_\rho)M(-\gamma_\rho)=2A^2|\Phi_c(t_\rho)|^2+A_+A_-\big[X^{\rho-\frac12}\Phi_c(t_\rho)^2+X^{\frac12-\rho}\Phi_c(-t_\rho)^2\big]$ exactly ([TA] Thm B(c)), with $\Phi_c^2=-\frac1{t^2(a-\lambda)}$ real.

Put $Z_{MM}(T)=\sum_{|t_\rho|>T}M(\gamma_\rho)M(-\gamma_\rho)$ and $Z_\times=Z-Z_{MM}$. Define the same split for $Z_{\cos}$ and $Z_\varphi$, summing over $|t_\rho|\ge t_0$; the finitely many lower zeros contribute $O(z^2)$.

### 5.2 Statements

**Theorem T0 (exact contact identity)** ([TE] Thm A). For every $s$, every eigenfunction and every $z\in\mathbb R$:
$$Z_{\cos}(z)=\lambda\big(1-\langle\psi,\tau_z\psi\rangle\big)+\mathcal L(z)-4(1-s)\sinh^2\!\tfrac z4\,F(\tfrac i2)F(-\tfrac i2),$$
$$\mathcal L(z)=\int_0^zG(\eta)\,\psi(L-z+\eta)\,d\eta\quad(z>0),\qquad G(\eta)=(J\psi-W_s\psi)(L+\eta),\qquad\mathcal L(-z)=\mathcal L(z).$$
No hypothesis on the zeros is needed; the only zero-counting input is $N(T+1)-N(T)=O(\log T)$.

*Tan reading.* The energy cost of translating $\psi$ by $z$ is $2\mathcal L(z)\simeq(A_+^2+A_-^2)z=|\lambda'|z$.

**Theorem T1 (Fourier edge law)** ([TA] Thm B, with the canonical main term).
- With $\mathsf B=\mathsf B_0(L,s,\Lambda_0)+C|A|$, where $\mathsf B_0$ does **not** depend on $A$,
$$\sup_{|y|\le\frac12}\int_{T\le|t|\le2T}\big(|R|^2+|R_t|^2+|R_y|^2+|R_{ty}|^2\big)(t,y)\,dt\le\frac{\mathsf B^2}{T\log^3T}.$$
- On dyadic windows:
$$\frac1T\int_T^{2T}t^2(a-\lambda)|F|^2dt=A_+^2+A_-^2+O\Big(\frac{A^2+|A|\mathsf B}{\log T}+\frac{\mathsf B^2}{\log^2T}\Big).$$
- Nothing is claimed for windows of fixed length.

**Theorem T2 (sharp tail law, first order; no hypothesis on the zeros)** ([TA] Thm C, Cor D). For every $s$ and every eigenfunction,
$$\big|\pi TZ(T)-(A_+^2+A_-^2)\big|\le C\frac{A^2+|A|\mathsf B}{\log T}+C\frac{\mathsf B^2}{\log^2T}.$$
- If $\lambda$ is sector-simple, then $\pi TZ(T)=|\lambda'(L)|+O_\psi(1/\log T)$ at every $L$, prime-power $X$ included.
- If $s=1$ and $\lambda\ne0$, then $\pi T(1-S(T))=|\lambda'|/\lambda+O_\psi(1/(|\lambda|\log T))$.
- If $A=0$, then $Z(T)=O(\mathsf B^2/(T\log^2T))$.
- The relative form $1+O(1/\log T)$ is informative only for $\log T\gg\mathsf B/A$.
- This **supersedes** [TE] Cor C3, which needed all but finitely many zeros on the line and gave no rate. The smoothed version ([TE] Cor C1, error $O(1/(T\log T))$) uses no main term of $N(T)$, no $S(t)$ and no Landau formula.

**Theorem T3 (second-order smoothed tail law, per sector, with rate; proved here).** For every $s$ and every eigenfunction, the following hold. The constants depend on $\psi$, and on the prime-power gap $\delta_X=\min(\{|2L-\log n|:n\ne X\}\cup\{\log2\})$.
- (a) *Translation norm and Fourier tail, with rate:*
$$1-\langle\psi,\tau_z\psi\rangle=\frac{A^2z}{\ell(z)}+O\Big(\frac z{\ell^2}\Big),\qquad\int_{|t|>T}|F|^2=\frac{4A^2}{T\log T}+O\Big(\frac1{T\log^2T}\Big).$$
- (b) *Contact law* ([TE] Thm E): $\mathcal L(z)=A^2z+c_XA_+A_-\frac z{\ell(z)}+O(z\ell^{-3/2})$.
- (c) $Z_{\cos}(z)=A^2z+(\lambda A^2+c_XA_+A_-)\frac z{\ell(z)}+O(z\ell(z)^{-3/2})$.
- (d) $Z_\varphi(T)=\frac{2m_1(\varphi)}T\Big[A^2+\frac{\lambda A^2+c_XA_+A_-}{\log T}\Big]+O\Big(\frac{|\varphi|(\mathbb R)}{T\log^{3/2}T}\Big)$.
- (e) For a sector-simple $\lambda$ with $A\ne0$ and $m_1(\varphi)\ne0$, put $\tau^\varphi(T)=TZ_\varphi(T)/(m_1|\lambda'|)$. Then
$$\tau^\varphi(T)=1+\frac{\lambda+\varepsilon c_X}{\log T}+O(\log^{-3/2}T),$$
  and for the two parity ground states, $\tau^\varphi_e-\tau^\varphi_o=\frac{2c_X+\lambda_e-\lambda_o}{\log T}+O(\log^{-3/2}T)$.

[TE] Thm C4 had (c)–(e) with $o(\cdot)$ in place of the rate, through Pitman's Tauberian theorem.

**Proposition T4 (sharp edge×edge part, unexpanded)** ([TA] Prop E1, with the canonical $\Phi_c$).
$$\pi TZ_{MM}(T)=2A^2\,T\!\int_T^\infty\frac{a(t)+\varepsilon c_X}{t^2(a(t)-\lambda)}dt+O_X\Big(\frac{A^2\log T}T\Big),\qquad|\pi TZ_\times(T)|\le C\frac{|A|\mathsf B}{\log T}+C\frac{\mathsf B^2}{\log^2T}.$$
For fixed $\lambda$, the integral factor equals $1+\frac{\lambda+\varepsilon c_X}{\log(T/2\pi)-\lambda+1}+O(\log^{-3}T)$ (Prop. T6). The smooth analogue has **no** $c_X$ term:
$$\pi TE_{MM}=2A^2\,T\!\int_T^\infty\frac{a}{t^2(a-\lambda)}+O(A^2/T).$$

**Theorem T5 (the cross term vanishes on average; proved here).** For every $\varphi$ as in §5.1,
$$\sum_{|t_\rho|\ge t_0}\big[h(\gamma_\rho)-M(\gamma_\rho)M(-\gamma_\rho)\big]\Big(1-\Phi\big(\tfrac{\gamma_\rho}T\big)\Big)=O\Big(\frac{|\varphi|(\mathbb R)}{T\log^{3/2}T}\Big).$$
In particular $Z^\times_{\cos}(z)=O(z\ell^{-3/2})$, whereas Cauchy–Schwarz alone gives $O(z/\ell)$. The smoothed canonical main term is
$$Z^{MM}_{\cos}(z)=\frac{2A^2}\pi\int_{t_0}^\infty(1-\cos zt)\frac{a+\varepsilon c_X}{t^2(a-\lambda)}dt+O(A^2z^2\ell)=A^2z\Big[1+\frac{\lambda+\varepsilon c_X}{\ell-D+1}\Big]+O(A^2z\ell^{-3}).$$

**Proposition T6 (the two tail write-ups' open conjectures are one statement; proved here).** Fix $\lambda$ and let $A\ne0$.
- (a) Exact moments:
$$\frac2\pi\int_0^\infty\frac{1-\cos u}{u^2}\log u\,du=1-\gamma,\qquad\frac2\pi\int_0^\infty\frac{1-\cos u}{u^2}\log^2u\,du-(1-\gamma)^2=1+\frac{\pi^2}{12}.$$
  The sharp analogues are $\int_1^\infty\frac{\log u}{u^2}du=1$ and $\int_1^\infty\frac{\log^2u}{u^2}du-1=1$.
- (b) Hence the canonical main terms carry exactly the refined denominators of [TE]:
$$T\!\int_T^\infty\frac{a+\varepsilon c_X}{t^2(a-\lambda)}=1+\frac{\lambda+\varepsilon c_X}{\log\frac T{2\pi}-\lambda+1}+O(\ell^{-3}),\qquad\frac2\pi\!\int_0^\infty\frac{1-\cos u}{u^2}\,\frac{a(u/z)+\varepsilon c_X}{a(u/z)-\lambda}\,du=1+\frac{\lambda+\varepsilon c_X}{\ell-D+1}+O(\ell^{-3}).$$
  The $\ell^{-3}$ coefficients are $(\lambda+\varepsilon c_X)\cdot1$ and $(\lambda+\varepsilon c_X)\cdot(1+\frac{\pi^2}{12})$ (`checks/denominators_check.out`).
- (c) Consequently, for $A\ne0$ and a sector-simple $\lambda$:
  - [TE]'s Prediction F (sharp) holds iff $\pi TZ_\times(T)=o(1/\log T)$, which Conjecture L implies;
  - [TE]'s Conjecture R (smoothed, remainder $O(\ell^{-3})$) holds iff $Z^\times_{\cos}(z)=O(z\ell^{-3})$.

  **Both write-ups' open problems are the size of one cross term $Z_\times$**, sharp or smoothed. Theorem T5 settles the smoothed version at $O(z\ell^{-3/2})$.

**Conjecture L (open).** At fixed $L$ with $\delta_X>0$, $\pi TZ_\times(T)=O_\psi(\log^{-3/2}T)$, and likewise for $E_\times$. The kink heuristic predicts $O(\log^{-2}T)$.

*Consequences under Conjecture L* ([TA] Cor E2):
- $\tau(T)=\pi TZ/|\lambda'|=T\int_T^\infty\frac{a+\varepsilon c_X}{t^2(a-\lambda)}dt+O(\ell^{-3/2})$;
- the derivative-free split is
$$\ln\frac{Z_e}{E_e}-\ln\frac{Z_o}{E_o}=\frac{2c_X}{a(T)}+O(\ell^{-3/2}).$$

**Conjecture R (open; restated).** $Z_{\cos}/(A^2z)-1=\frac{\lambda+\varepsilon c_X}{\ell-D+1}+\frac{\kappa_{\rm kink}}{\ell^2}+O(\ell^{-3})$, where $\kappa_{\rm kink}$ is a constant depending on $L$ and the sector, to be derived from the kink law.

[TE]'s original form has $\kappa_{\rm kink}=0$. That is probably false at $e^{2L}=nm$ (an internal referee found a sector term $\pm2\sum_{nm=X}c_nc_m$). It is plausibly false whenever some $n<X$ is active (§5.6).

### 5.3 Proofs of T0–T2 and T4 (from the write-ups)

**T0** ([TE] §3).
1. Translation invariance gives $\mathcal Q(\psi-\tau_z\psi)=2\lambda(1-\langle\psi,\tau_z\psi\rangle)+2\mathcal L(z)$. This is the eigen-equation inside the window plus the exterior pairing $\mathcal E(\psi,\phi)=-\int_{I^c}(J\psi)\phi$ for disjoint supports ([N] Lemma 3.6(e)).
2. The explicit formula on the form domain ([TE] Lemma A.1) is applied to $h_z=\psi-\tau_z\psi$, with $F_{h_z}(w)F_{h_z}(-w)=2h(w)(1-\cos zw)$.
   - Weil 1952 is used for $C_c^\infty$ only.
   - It extends by form continuity: $|F(w)|^2$ is subharmonic, and there are $O(\log T)$ zeros per unit box.
3. The pole term is the only $s$-dependent part. ∎

**T1** ([TA] §§4–6).
- **Lemma 2 (exact second-order edge transform).** With $\mu=q+\lambda-c$ (so $\sigma_q-\mu=a-\lambda$), $(a-\lambda)\hat u=-AU/(it)+\widehat{g_0}+\mathcal R$. Here:
  - $|U|^2=a-\lambda+\mu^2\sigma_q|\hat r_{q,-}|^2$ exactly, with $\operatorname{Re}\hat r_{q,-}=1/(2\sigma_q)$;
  - $\arg U=O(1/\log t)$ (CBF representation);
  - $|\mathcal R|\le C/(t\log t)$.
- **Lemma 3.** The mean square of the regular part is controlled through the translation functional $T\int_0^{1/T}\|\tau_hg-g\|^2dh$, by a two-pass bootstrap.
- **Strip and derivatives.** Convolve with $\hat\eta$, $\eta=(ix)^ke^{-yx}\zeta$. Lemma 2 is never differentiated.
- **Canonical replacement.** Lemma 2 gives $|\Phi-\Phi_c|=|\Phi_c|\,|e^{-i\theta}(1+O(\ell^{-2}))-1|=O(t^{-1}\ell^{-3/2})$. So the canonical remainder has shell mass $\le(\mathsf B_0+C|A|)^2/(T\log^3T)$. ∎

**T4** ([TA] §7.3, redone with $\Phi_c$).
- *Diagonal part.*
  - Riemann–von Mangoldt: $N(t)=\theta(t)/\pi+1+S_N(t)$ with $S_N=O(\log t)$ unconditionally and $\theta'=a/2$ exactly.
  - Stieltjes integration of $f=|\Phi_c|^2=\frac1{t^2(a-\lambda)}$ gives $2\sum_{t_\rho>T}f=\frac1\pi\int_T^\infty af\,dt+O(T^{-2})$.
- *Oscillating part.*
  - The bijection $\rho\mapsto1-\bar\rho$ preserves $t_\rho$ and conjugates the summand, so the oscillating part is $4A_+A_-\operatorname{Re}\sum_{t_\rho>T}X^{\rho-\frac12}\Phi_c^2$.
  - Landau 1912: for fixed $X>1$, $\sum_{0<t_\rho\le t}X^{\rho-\frac12}=-\frac{c_X}{2\pi}t+O_X(\log t)$, unconditionally, with multiplicity, off-line zeros included.
  - Partial summation with $\Phi_c^2=-1/(t^2(a-\lambda))$ gives $+\frac{2A_+A_-c_X}\pi\int_T^\infty\frac{dt}{t^2(a-\lambda)}+O_X(A^2\log T/T^2)$. Since $\Phi_c$ is canonical, no phase lemma is needed.
- *The bound on $Z_\times$.* Cauchy–Schwarz on dyadic blocks, with Lemma Z (a 1-D Sobolev inequality in $t$ and $y$ plus $N(t+1)-N(t-1)\le C\log t$) and T1.
- *$E_{MM}$.* The oscillating term integrates by parts to $O(A^2/T^2)$, since $L\ne0$. ∎

**T2** ([TA] §7.4). By T4, $\pi TZ_{MM}=2A^2+O(A^2(1+|\lambda|+c_X)/\log T)$; add the bound on $Z_\times$. (H) gives $2A^2=|\lambda'|$, and Lemma W gives the share. ∎

### 5.4 Proof of Theorem T3 (new combination)

*Inputs:* [TA] Thm B and [TE] Thm E. Both were internally refereed; their second-round referee reports were not archived, and the internal final referee re-checked both line by line. The step (a) below is new and replaces Pitman's theorem and [TE] Lemma C.5.

**(a) Translation norm with rate.**
- Since $\|\psi\|=1$ and $|F|$ is even,
$$1-\langle\psi,\tau_z\psi\rangle=\frac1{2\pi}\int(1-\cos zt)|F(t)|^2dt .$$
  The part $|t|<t_0$ is $\le\frac{z^2t_0^2}2$.
- For $|t|\ge t_0$, write $|F|^2=|M|^2+2\operatorname{Re}(\bar MR)+|R|^2$, with
$$|M(t,0)|^2=\frac{2A^2}{t^2(a-\lambda)}-2A_+A_-\frac{\cos2Lt}{t^2(a-\lambda)} .$$
- *Main term.* With $u=zt$:
$$\frac{2A^2}\pi\int_{t_0}^\infty\frac{1-\cos zt}{t^2(a-\lambda)}dt=A^2z\cdot\frac2\pi\int_{zt_0}^\infty\frac{1-\cos u}{u^2(a(u/z)-\lambda)}du .$$
  Here $a(u/z)-\lambda=\ell+\log u-\log2\pi-\lambda+O(z^2/u^2)$.
  - On $u\in[\sqrt z,z^{-1/2}]$, expand $1/(\ell'+\log u)$ with $\ell'=\ell-\log2\pi-\lambda$.
  - The two tails are $O(\sqrt z)$.
  - By T6(a) the result is $A^2z/(\ell-D+1)+O(A^2z\ell^{-3})=A^2z/\ell+O(A^2z/\ell^2)$.
- *Oscillating term.* With $g(t)=\frac{1-\cos zt}{t^2(a-\lambda)}$, integrate $\int\cos(2Lt)g$ by parts:
  - $|g(t_0)|\le z^2$;
  - $\int_{t_0}^\infty|g'|\le Cz^2\int_{t_0}^{1/z}\frac{dt}{t\log t}+C\int_{1/z}^\infty\big(\frac z{t^2}+\frac1{t^3}\big)dt=O(z^2\log\ell)$.
- *Cross term.* On the dyadic shell $[T,2T]$, the weight is $\le\min(2,4z^2T^2)$, and by Cauchy–Schwarz with T1 the shell contributes $\le C|A|\mathsf B/(T\log^2T)$ times that weight.
  - Shells with $T\le1/z$ sum to $\le Cz^2\sum T/\log^2T\le C|A|\mathsf Bz/\ell^2$; the sum is geometric, dominated by $T\approx1/z$.
  - Shells with $T>1/z$ sum to $\le C|A|\mathsf B\sum_{T>1/z}1/(T\log^2T)\le C|A|\mathsf Bz/\ell^2$.
- *$|R|^2$ term.* Similarly $O(\mathsf B^2z/\ell^3)$.

Altogether $1-\langle\psi,\tau_z\psi\rangle=A^2z/\ell+O\big((A^2+|A|\mathsf B+\mathsf B^2)z/\ell^2\big)+O(z^2)$.

The Fourier-tail statement is the same computation with the weight $\mathbf 1_{|t|>T}$ in place of $(1-\cos zt)$:
$$2\cdot2A^2\int_T^\infty\frac{dt}{t^2(a-\lambda)}=\frac{4A^2}{T\log T}\Big(1+O\big(\tfrac1{\log T}\big)\Big),$$
the oscillating part is $O(A^2/(T^2\log T))$, and the cross and remainder parts are $O(|A|\mathsf B/(T\log^2T))$ and $O(\mathsf B^2/(T\log^3T))$. ∎

**(b)** This is [TE] Theorem E(iii). It is proved through:
- the pointwise Wiener–Hopf exterior identity (Lemma E.0);
- the renewal estimates (Lemmas E.1, E.2);
- the exterior field $G^{(X)}(\eta)=A_+[\sqrt q+M_K(\eta)-\kappa_qV_q(\eta)]+O(1/\ell)$, with $\kappa_q=\frac12(q+\lambda-c)$;
- the exact cancellation of the two $1/\ell$ terms (germ $V^3$ and field $-\kappa_qV$) through the identity $\int_0^z(\sqrt q+M_K)V(z-\cdot)=z$;
- the exact isolation of the $n=X$ shift, $c_X\,g_\psi(2L-z)=c_XA_+A_-z/\ell+O(z/\ell^2)$.

  Constants depend on $\delta_X$.

**(c)** Insert (a) and (b) into T0. The pole term is $O(z^2)$, and $A_+^2=A^2$.

**(d)** Integrate (c) against $\varphi_T$ (the image of $\varphi$ under $z\mapsto z/T$). This is Fubini; the sums converge absolutely. Use
$$\int\frac{|z|}{\ell(|z|)}d\varphi_T=\frac{2m_1}{T\log T}+O\Big(\frac{|\varphi|(\mathbb R)}{T\log^2T}\Big),\qquad\int|z|\ell(|z|)^{-3/2}d|\varphi_T|\le\frac{|\varphi|(\mathbb R)}{T\log^{3/2}T}.$$

**(e)** Divide by $m_1|\lambda'|/T=2m_1A^2/T$, using (H), $A_+A_-=\varepsilon A^2$, and $m_1\ne0$. ∎

*Cross-validation.* (c) is a position-side statement: no zero counting beyond local bounds, no Landau formula. The same coefficient $\lambda+\varepsilon c_X$ comes out of the Fourier/zero-side computation T4–T5, which uses Riemann–von Mangoldt and Landau. The two write-ups share only [N].

### 5.5 Proofs of T5 and T6 (new)

**T6(a).**
- Integrating by parts with $\frac d{du}\big(-\frac{\log u+1}u\big)=\frac{\log u}{u^2}$ (the boundary terms vanish):
$$\int_0^\infty\frac{(1-\cos u)\log u}{u^2}du=\int_0^\infty\frac{\sin u\,(\log u+1)}u\,du=-\frac{\pi\gamma}2+\frac\pi2 .$$
- Likewise, with $\frac d{du}\big(-\frac{\log^2u+2\log u+2}u\big)=\frac{\log^2u}{u^2}$ and $\int_0^\infty\frac{\sin u\log^2u}u\,du=\frac\pi2(\gamma^2+\frac{\pi^2}{12})$:
$$\frac2\pi\int_0^\infty\frac{(1-\cos u)\log^2u}{u^2}du=\gamma^2+\frac{\pi^2}{12}-2\gamma+2=(1-\gamma)^2+1+\frac{\pi^2}{12}.$$
- Numerical confirmation (`checks/denominators_check.out`): $\mu_1=0.422784335098=1-\gamma$ (difference $3\cdot10^{-18}$), and variance $1.822467=1+\pi^2/12$.

**T6(b).**
- Write $\frac{a+\varepsilon c}{a-\lambda}=1+\frac{\lambda+\varepsilon c}{a-\lambda}$.
- In the smoothed integral, $a(u/z)-\lambda=\ell'+\log u+O(z^2/u^2)$ with $\ell'=\ell-\log2\pi-\lambda$.
- Then $\frac2\pi\int\frac{1-\cos u}{u^2}\frac{du}{\ell'+\log u}=\frac1{\ell'+\mu_1}+\frac{\mu_2-\mu_1^2}{\ell'^3}+\dots$, and $\ell'+\mu_1=\ell-\log2\pi-\lambda+1-\gamma=\ell-D+1$.
- The sharp case is the same with $u=t/T$ and the moments of $u^{-2}du$ on $[1,\infty)$.
- Numerical confirmation (`checks/denominators_check.out`, $\lambda=0,-2,-4.5$, $\ell=20,40,80$): (difference)$\times\ell^3$ tends to $1+\pi^2/12=1.82$ (smoothed: $1.93$, $1.79$, $1.63$ at $\ell=80$) and to $1$ (sharp: $0.94$, $0.87$, $0.80$ at $\log T=80$). The approach is slow because the next term is $O(\ell^{-4})$ with a $\lambda$-dependent coefficient.

**T6(c).** Assume $A\ne0$ and $\lambda$ sector-simple.
- Divide T4 by $2A^2$: $\tau=T\int_T^\infty\frac{a+\varepsilon c_X}{t^2(a-\lambda)}+\pi TZ_\times/(2A^2)+O(\log T/T)$. Pred. F is the first term to $O(\ell^{-3})$.
- For the smoothed case, use T5's $Z^{MM}_{\cos}$ and T6(b). ∎

**T5.**
- *Low zeros.* The finitely many zeros with $|t_\rho|<t_0$ contribute $O(z^2)$ to $Z_{\cos}$.
- *Diagonal part.* For $|t_\rho|\ge t_0$, write $1-\cos z\gamma_\rho=(1-\cos zt_\rho)+e_\rho$. Since $|y_\rho|<\frac12$, we have $|e_\rho|\le C(z^2+z\min(1,zt_\rho))$. Summed against $|M(\gamma_\rho)|^2\le CA^2/(t_\rho^2\log t_\rho)$, with $O(\log t)$ zeros per unit, the $e_\rho$ give $O(A^2z^2\ell)$.
  - Stieltjes integration against $dN$ with $f(t)=2A^2|\Phi_c|^2(1-\cos zt)$ follows. Here
$$|f'|\le CA^2\Big[\frac{\min(z^2,t^{-2})}{t\log t}+\frac{z\min(1,zt)}{t^2\log t}\Big],$$
    so the $S_N$ part is $\le C\int\log t\,|f'|dt=O(A^2z^2\ell)$.
  - The density part is $\frac{2A^2}\pi\int_{t_0}^\infty(1-\cos zt)\frac a{t^2(a-\lambda)}dt$ (both signs of $t$).
- *Oscillating part.* By conjugation symmetry it is $4A_+A_-\operatorname{Re}\sum_{t_\rho\ge t_0}X^{\rho-\frac12}\Phi_c(t_\rho)^2(1-\cos z\gamma_\rho)$.
  - Landau's formula and partial summation with $W=\Phi_c^2(1-\cos zt)$ give $+\frac{2A_+A_-c_X}\pi\int_{t_0}^\infty\frac{1-\cos zt}{t^2(a-\lambda)}dt+O_X(A^2z^2\ell)$.
  - The error uses $\int\log t\,|W'|=O(z^2\ell)$, and the $e_\rho$ correction is as before.
- *Sum.* The two parts give the displayed $Z^{MM}_{\cos}$. By T6(b) it equals $A^2z[1+\frac{\lambda+\varepsilon c_X}{\ell-D+1}]+O(A^2z\ell^{-3})$.
- *Subtract from T3(c).* $Z^\times_{\cos}=Z_{\cos}-Z^{MM}_{\cos}+O(z^2)=O(z\ell^{-3/2})$.
- *General $\varphi$.* Integrate against $\varphi_T$ (Fubini: $\sum|h|$ and $\sum|MM|$ converge). ∎

*Why T5 is not Conjecture L.*
- $Z_\times(T)$ is not of one sign, even under RH, because it is a cross term. So no Tauberian theorem converts the smoothed bound into a sharp one.
- T5 says that the sharp cross term, measured in units of $1/(T\log T)$, has cosine-Abel means $O(\ell^{-1/2})$. It may still oscillate in $\log T$ at size $1/\log T$; nothing proved excludes that.

### 5.6 Where the $\ell^{-2}$ terms come from (heuristic; what the kink law now makes computable)

- In the zero sum, the edge×kink cross terms resonate with the prime part of the zero density at the frequencies $\log n$. Landau's formula at $x=n$ makes such a pairing nonzero.
- K3 gives the kink's Fourier amplitude relative to the edge: about $c_n/\log t$, in phase, with the odd (jump) part dominant. The even cusp enters only at relative order $\ell^{-1}$ in Fourier.
- So, against the prime density, edge×own kink gives a sector-independent $-\kappa\sum_{n<X}c_n^2/\ell^2$ in $Z$, and $+\kappa\sum c_n^2/\ell^2$ against the smooth density in $E$ ([TA] §8.3; $\kappa=1$ in that heuristic).
- Edge×opposite kink at $X=nm$ gives $\pm2\sum_{nm=X}c_nc_m/\ell^2$.
- [NUM] measured $k_{\rm eff}=(Z/P_1-1)/(-\sum c_n^2\langle a^{-2}\rangle)=0.0$–$0.4$ (even) and $0.6$–$1.0$ (odd) at $X=6,8,10$, all of which are of the form $nm$. That is consistent with
$$\kappa\approx\tfrac12\ \text{plus a sector term}\ \pm\varepsilon\frac{\sum_{nm=X}c_nc_m}{\sum_{n<X}c_n^2}\ \text{of the right sign},$$
  but it is not a test of it.
- Two consequences:
  - Conjecture L at $O(\ell^{-3/2})$ is expected to hold, since the expected size is $O(\ell^{-2})$.
  - Conjecture R in [TE]'s form ($O(\ell^{-3})$, no $\ell^{-2}$ term) is expected to **fail** whenever $\kappa\sum_{n<X}c_n^2\ne0$, unless the cosine smoothing cancels it. The position-side check at $L=0.4$ (predicted $\approx-1\cdot10^{-4}$ at $\ell=27.6$, against a mesh floor of $\le5\cdot10^{-5}$ relative) cannot decide this.
- The heuristic P6 ($E/Z-1\approx2\sum c_n^2/a^2$) has the right size for odd states and is $2.5$–$20$ times too large for even states ([NUM] §5). This sector asymmetry is again consistent with the $nm$ term.
- **Deriving $\kappa$ and the sector term from K3/K5 is the concrete next step (§10.1).**

---

## 6. Numerical confirmation

All runs are float64 and uncertified. "Independent" means the code shares no discretisation with the P0 solver used by the write-ups.

**About the pre-registration of [NUM].** The test was registered (`numerics/PREREG.md`, md5 in `numerics/PREREG.md5`) before any production run. Three caveats:
- One registered script, `kink_analyze.py`, was changed after registration (md5 `8404f5dc…` → `87a74c8b…`). It is a pairing fix: the two sides of an anchor are now matched by common offsets, because the old code crashed on symmetric meshes. Values for the right-side runs are unchanged (`numerics/numerics.md` §6). The other registered checksums still match.
- The tail PASS used a generous registered tolerance: $Z/P_1$ values down to $0.80$ pass.
- At $X=8$, two of the four sector-split pairs are about $2.5\sigma$ above the predicted $\alpha=2c_8$.

### 6.1 Kink law

| Prediction | Code | Where | Measured | Verdict |
|---|---|---|---|---|
| Jump coefficient 1, generation 1 (K3) | P1, independent [NUM] | $L=0.6,0.8,1.0$; $n=2,3,4,5,7$; $\lvert A\rvert=0.26$–$1.64$; $s=0,5$; 50 graded rows | $0.9986$–$1.0019$ | **PASS 50/50** (pre-registered) |
| Even cusp $\frac13$ (i.e. split $\frac23:-\frac13$) | P1 [NUM] | same | $0.3322$–$0.3346$ | **PASS 50/50** |
| Side ratio $-2$, sign of $A$, larger excursion on the source side | P1 [NUM] | same, plus mirrors | $-1.9969$ to $-2.0035$; signs correct in 70/70 | **PASS** |
| Generation 2: jump 1, cusp $\frac15$, side $-\frac32$; weights $2c_2c_3$, $c_2c_3$, $c_3c_4$ | P1 [NUM] | $L-\log1.5$, $L-\log\frac43$, $L-\log6$ | $0.9912$–$1.0054$; $0.1967$–$0.2018$; $-1.494$ to $-1.5025$ | **PASS 20/20** |
| K5 offset $1/\rho-\ell\to-D-\beta_n$; boosts $\beta_2=0.347$, $\beta_4=0.693$ at $L=0.8$ (at $L=0.6$, $X=3.32$, so $4$ is inactive and $\beta_2=0$) | P1 [NUM] | $L=0.6,0.8$ | deviation $-0.0025$ to $-0.0005$ | **PASS** |
| K5 offset at $L=1.0$, registered mesh | P1 [NUM] | $n=3,4,5,7$ | $+0.011$ to $+0.061$ | **FAIL as registered**: generation-2 points graded only to $10^{-16}$, inside the fit window |
| same, every coupled point graded deep (post-registration) | P1 [NUM] | all $n$ | $-0.0040$ to $-0.0007$ | consistent; not a registered verdict |
| Edge law K1(c), $D=\lambda+\log2\pi+\gamma$ | P1 [NUM] | $L=0.6,0.8,1.0$ | $D_{\rm fit}-D=+0.0013$ to $+0.0049$ | **PASS 40/50** (the 10 fails are the single-ρ $L=1.0$ sensitivity mesh) |
| K1 + K5 with $A$ from the edge fit: $\mathfrak D/(c_nA(\ell-D)^{-3/2}(1+\beta_n/\ell))\to1$ | P0 (final-referee code), internal referee | 31 point-instances, 9 states | $0.9999$–$1.0003$ at $\ell\approx90$ | confirms |
| Fit-free leading constants (Richardson) | P0, [KW] | 14 runs | jump $0.987$–$0.999$; cusp $0.330$–$0.3333$; side $-2.000$ to $-2.002$ | confirms; the shortfall at $D\approx2.4$ is largely the $\frac{35}8D^2/\ell^2$ term |
| Even part, second order (Conj K7), no free parameter | P0, internal referee | 15 interior cases | agree to $\le0.015$ on $\ell\in[20,85]$, including the $X\ne0$ points at $L=0.75$ | supports the conjecture |
| (R2) on the true symbol | mpmath, internal referee | $q=1$, $\ell=10$–$160$ | $(R/{\rm pred}-1)\ell^2=0.55\to0.80$, tending to $\pi^2/12=0.82$ | confirms |
| (V2) | Gaver–Stehfest, internal referee (independent of both proofs) | $\ell=27.6$–$200$ | $V^{-2}-\ell=3.95557\to3.957055$; limit $3.9570907$ | confirms |
| Lemma T | mpmath, [KL] | $\log t=10$–$120$ | $(\theta-\frac\pi{4\Lambda})\Lambda^3\to1.293$; prediction $1.29193$ | confirms |
| Lemma O, third-order constant | model kernel, [KL]; derivation by an internal referee | $a=0.5,1.5,2.5$ | $0.4117$, $1.2336$, $2.059$ against $a\pi^2/12=0.4112$, $1.2337$, $2.0562$ | confirms |

### 6.2 Tail law

| Prediction | Code | Where | Measured | Verdict |
|---|---|---|---|---|
| Constant 2 in (H), $-\lambda'/(2A^2)=1$ (input of T2) | P0, final referee | 13 cases, $L=0.3$–$0.6$, pure log | within $3\cdot10^{-3}$; within $6\cdot10^{-4}$ after refinement | confirms ([N] §13.1) |
| Hadamard by-product $\lvert\lambda'\rvert/2A^2$ | P1 [NUM] | 12 tail states, $X=6,8,10$ | $0.996$–$1.010$ | confirms |
| Fourier edge law with the $-\lambda$ shift (T1), pure log | P0, [TA] and its referee | $L=0.5$, $k=0..5$, dyadic windows | $\langle t^2(\log t-\lambda_k)\lvert F_k\rvert^2\rangle=1.990$–$2.014$ (prediction 2); the unshifted form is off by up to a factor 1.97 | confirms |
| T4 / Pred. F, second-order sharp form, $\lambda$-shifted | P1 [NUM] | $X=6,8,10$, 11 states, $\lambda$ from $-0.9$ to $-10.3$, zeros up to $T=10\,300$ | $Z/P_1=0.80$–$1.00$; $0.968$–$1.000$ on $[6400,10300]$; deviation $-8.7\%$ to $+0.03\%$ for $T\ge400$; $\tau/\tau_{\rm pred}-1\in[-0.069,+0.001]$ | **PASS 11/11** (pre-registered) |
| The $\lambda$-shift is needed | P1 [NUM] | same | without it, $0.20$–$0.87$ | **PASS** |
| $c_X$ term at prime-power $X$ (sharp, edge×edge) | P0, [TA] | $X=4$, $s=0$ even, $T\in[100,1600]$ | $Z/P_1=0.989$–$0.994$ (mesh-stable); without $c_4$: $1.06$–$1.10$ | supports |
| $c_X$ term, both sectors | P0, internal referee | $X=2$ ($s=0,1$), $X=3$ ($s=0$), zeros 1–1500 | $Z/P_F=0.980$–$1.009$ on $[250,1981]$; without $c_X$: $1.09$–$1.12$ (even), $0.87$–$0.91$ (odd); control $L=0.4$: $0.980$, $0.998$ | supports (no $nm$ competition at $X=2,3$) |
| Sector split $\alpha=2c_8=0.490$ | P1 [NUM] | $X=8$, 4 pairs | $\alpha=0.51$–$0.67$ ($\pm0.06$); two pairs about $2.5\sigma$ high | **PASS** (registered) |
| Control $X=6$: $\alpha=0$ | P1 [NUM] | 2 pairs | $+0.018\pm0.072$, $+0.012\pm0.068$ | **PASS** |
| Control $X=10$: $\alpha=0$ | P1 [NUM] | 4 pairs | $0.32$–$0.44$ ($\pm0.18$) | passes on the registered rule only; **uninformative** |
| Parity-antisymmetric offset at $X=8$ against the $X=6,10$ controls (post hoc) | P1 [NUM] | $T\approx4000$ | $\pm0.03$ against $\pm c_8\langle1/a\rangle=\pm0.037$ | supports |
| Leading law $\pi TZ\to\lvert\lambda'\rvert$ | P1 [NUM] | large-$\lvert\lambda\rvert$ states | $\tau(6400)=0.47$–$0.81$ | not testable at $T\le10^4$; no contradiction |
| Contact law, position side ([TE] Thm E(ii)) | P0, [TE] | 14 states | $\lvert\mathcal L^{(X)}/(A^2z)-1\rvert\le5\cdot10^{-5}$ for $\ell\ge27.6$ | consistent; at the mesh floor, so no rate can be read off |
| Exterior field ([TE] Thm E(i)) | Laplace inversion, [TE] and its referee | 14 states | residual $\approx-(2.5$–$5.7)\ell^{-3/2}$; the $q$-dependence cancels to $1.3\cdot10^{-3}$ | consistent |
| Smoothed cross term (T5) | — | — | **not tested**. On the available zero range, low-$t$ artefacts of size $O(zt_0)$ are as large as the signal | gap |
| Heuristic P6, $E/Z-1\approx2\sum c_n^2/a^2$ | P1 [NUM] | $X=6,8,10$ | right size for odd states; $2.5$–$20$ times too large for even states | **fails** for even states (heuristic only) |

### 6.3 Limits of the evidence

- One P1 code and one P0 code (the final referee's). Neither is certified.
- The kink tests need $|A|\ge0.2$. The true-form ground states at $L\ge0.6$ ($A\le10^{-4}$, $\lambda\le10^{-6}$) are beyond float64.
- The tail tests use large-$|\lambda|$ states (pole strengths $s=0,-1,5,20$), so they test the theorems in a regime where $\lambda/\log T$ is large. The true $s=1$ share at small $\lambda$ is not tested.
- The $c_X$ term is supported at $X=2,3,4,8$, but at $X=8$ it is not cleanly separated from the $\ell^{-2}$ kink terms.

---

## 7. Prior art and credits

**Setting.**
- The localized (semilocal) Weil form, and its eigenvalues as primes are added: Connes–Consani, arXiv 2106.01715.
- The limit profile of the minimiser: Connes, arXiv 2602.04022, §6.5.
- Close work on the eigenvectors of the localized form: Connes–Consani–Moscovici, arXiv 2511.22755 ([N] cites its Lemma 5.2 only as a tool).
- The $\pm\log n$ shift structure: Suzuki, arXiv 2606.09096, eq. (2.11).

A light web search (2026-10-31) found nothing on the kink profile or on the tail law in the Connes–Consani line, nor did a screen of all 81 rStation riemann_hypothesis papers and forum post 21 (2026-10-31). That is absence of evidence only.

**Related preprints and repositories.**
- **Eberwein** (Zenodo 23177438, v1, 6 Oct 2026, §13; code `sem.py`) found the **locations** of the weak singular points: $\log n$ and $L-\log n$ of his window, which are our $\pm(L-\log n)$. He graded his meshes there. The kink law supplies their amplitude, profile and hierarchy.
- **mathia** (github.com/murillo128/mathia, `research/prime_lattice`):
  - PL-319–337 had **(E) in substance** (PL-336 for the expansion, PL-337 for $L^\infty$ through activations);
  - PL-338 has the prime-activation mechanism $4c_nC_0^2\delta/\log(1/\delta)$. That is the same structure as the $n=X$ contact term $c_XA_+A_-z/\ell$ of [TE] Thm E(iii) and the $c_X$ term of T3 and T4;
  - PL-306 is a conditional Hadamard–virial consistency statement;
  - no interior kink profile was found in mathia.
- **Mori** (github.com/moriryota/prolate-weil-bounds): paper II, the cut points of the truncated trial vector (location type); papers VI–VIII, the Schur-test switch points of the prime operator at $|L-\log n|$ (location prior art); paper III, a zero-side edge-leakage inequality at rate $\log T/T$.
- **Suzuki**, arXiv 2606.09096, eq. (2.11): the $\pm\log n$ shift structure (location type).
- **Joubert**, *The well, and the depth law* (GitHub darreal44/riemann-weil-phenomenology, `notes/the-well.pdf`): zero-side edge leakage with a fitted constant.

**rStation** (screened 2026-10-31: all 81 riemann_hypothesis papers and forum post 21, https://rstation.ai/r/riemann_hypothesis/posts/21; papers there are accepted by AI reviewer agents and are not refereed). No tail law and no kink law was found on rStation as of 2026-10-31. What is there:
- **rh_67**: bramble_trace, "Boundary traces and support variation for localized Weil operators", rStation riemann_hypothesis paper 67, v1, published 2026-10-27 19:07:56 UTC, https://rstation.ai/problems/riemann_hypothesis/papers/67/v1.
  - Trace existence for every eigenfunction, (2.2), (3.15), (3.19), with a limit formula (3.19); first posted in comment XNTCbIH-RNPZ9afU (bramble_trace, 2026-10-18 23:44:00 UTC). This is the input K1 builds on.
  - Theorem 2.4, the activation law at the eigenvalue level: $\lambda^{\rm full}(\delta)-\lambda^{\rm del}(\delta)=-2wp|\tau_+(u)|^2\frac{\delta}{\log(1/\delta)}+o\big(\frac{\delta}{\log(1/\delta)}\big)$, (2.9). It is proved there; for us it is only numerical ([N] §13, N6). It has the same $c_nA_+A_-\delta/\log(1/\delta)$ structure as the $c_X$ contact term of T3 and T4. It is the regime the kink law excludes, so neither result implies the other.
- **The offset $D$**: span_of_dilates, comment EAw5pFmSdKxMBRHA (2026-10-28 03:55:32 UTC), labelled heuristic ("I have no proof"), fits the activation ratio with a denominator that contains $D=\lambda+\log2\pi+\gamma$. We claim only the proof of $D$ at fixed $L$ (K1, K5, K6).
- **The Wiener–Hopf factor**: halasz_resonator, comment 3-jlbw7xu_tS6Rou (2026-10-19 00:10:21 UTC), expands $\kappa(s)=\sqrt{\frac12\log(1+s^2)}\big(1-\frac{\pi^2}{16(\log s)^2}+O((\log s)^{-3})\big)$. That is the factor, not $V$ or $\psi$; compare Prop R and Lemma T.
- **Different quantities** (related only):
  - span_of_dilates, "Finite-window Weil forms on Davenport-Heilbronn functions: a certified onset bound, an exact joint detection identity, and finite-space measurements", rStation riemann_hypothesis paper 66, v2, published 2026-10-27 21:16:47 UTC, https://rstation.ai/problems/riemann_hypothesis/papers/66/v2, Proposition 6.1 (part (b) assumes GRH): a far-field $1/\log$ limit, $r\,\ell\to\Phi_L(\delta)$ with $\ell=\log\frac{q\gamma_0}{2\pi}$, for a planted-quartet detection quantity. It is not the zero-side weight of an eigenfunction.
  - span_of_dilates, "An equilibrium conjecture for how far the ground state of a truncated Weil form tracks the zeros, with measurements for Dirichlet L-functions", rStation riemann_hypothesis paper 80, v1, published 2026-10-30 17:09:59 UTC, https://rstation.ai/problems/riemann_hypothesis/papers/80/v1, (3.2′) (derived, numerical): a per-zero displacement $\varepsilon_k=(S_k+|\lambda I_k|)/F'(\gamma_k)^2$ for the ground state's transform. It is not a tail law.

**Internal contributions** (AI referees and an AI novelty audit in the internal review rounds; credited by content, not by name):
- An internal novelty audit sketched the kink law ($\kappa=1$ at order $\ell^{-3/2}$, the hierarchy, density and the $L-\log6$ echo), conditional on (E). The proved version corrects "one-sided" to the split $\frac{k+1}{2k+1}:\frac{-k}{2k+1}$. It also sketched the tail law (its items S1–S5, including "$a(t)$, not $\log t$" and the Fourier-side Hadamard principle).
- An earlier internal round proposed the Landau sign of the per-sector term.
- Lemmas supplied by internal referees:
  - R1, R2 and J (these made V2 and K5 theorems);
  - the sliding-window density for all $L>\frac12\log6$, and the $A$-normalised check;
  - the even transfer and the precise even law (Conjecture K7), and the de Haan attribution;
  - the two-pass bootstrap, the translation functional, the $\eta$-convolution and the factor 4;
  - the canonical $\Phi_c$;
  - the clean zero-side split test at $X=2,3$, and the general-$s$ remark;
  - the $nm$ caveat to Conjecture R, and the $\pi^2/12$ deficit.
- The final referee of [N]: the P0 code, anchored offsets, and the grading caveat.
- [NUM]: the P1 code and the pre-registration.

**Outside the project** (checked by internal referees).
- **Half-line edge law:** Kwaśnicki 2011 (Studia Math. 206; arXiv 1006.0524), Lemma 4.27 and Example 6.4. Lemma 4.27 is a position-side boundary asymptotic, proved by Fourier/Wiener–Hopf methods. The $\lambda$-shifted second-order identity and the zero-side law are not there.
- **Boundary ratio limits:** Grzywny–Kwaśnicki 2018. **Log-Laplacian boundary rate:** Hernández-Santamaría–López Ríos–Saldaña, arXiv 2401.18033.
- **Interior regularity for low-order kernels:**
  - Chang-Lara–Saldaña, arXiv 2208.12841;
  - Kassmann–Mimica 2017;
  - Hu–Zhao, arXiv 2304.14056;
  - Biswas–Roy–Sen–Sharma, arXiv 2608.07315 (Hölder regularity for the log-Laplacian with a logarithmic gain; the closest relative of Lemma M).

  Lemma M is a pointwise, explicit-kernel, one-dimensional relative of these.
- **Shift-orbit loss of smoothness:** Skubachevskii (Mat. Zametki 1983; Birkhäuser 1997; Vorotnikov–Skubachevskii 2023); breaking points in delay equations (Bellen–Zennaro). This is the same mechanism in differential order 2, where each passage gains derivatives instead of one logarithm.
- **Log-endpoint Fourier asymptotics:** Wong–Lin, JMAA 64 (1978). Not used in the proofs; it is the natural tool for §10.1.
- **Contact/tail mechanism:**
  - Tan relations (Ann. Phys. 323, 2008; Braaten–Platter PRL 100, 2008);
  - fractional Hadamard formulas (Djitte–Fall–Weth, Calc. Var. 60, 2021) and Pohozaev (Ros-Oton–Serra 2014).

  None is of order zero.
- **Classical inputs:**
  - Weil 1952 (explicit formula, smooth test functions);
  - Riemann–von Mangoldt;
  - Landau 1912 (fixed-$x$ formula);
  - Gonek's uniform Landau formula (Contemp. Math. 143 (1993), 395–413; cited only in remarks);
  - CBF representation (Schilling–Song–Vondraček, Thm 6.2);
  - Bromwich inversion (Widder, Ch. II);
  - de Haan theory (Bingham–Goldie–Teugels Ch. 3);
  - GR 4.421.1.
- **Pitman 1968** is **no longer needed** for the second-order smoothed law (T3 replaces it). It remains the route of [TE] Cor C2 and Thm B′ as originally written.

**What appears new** (not found in our literature search, which is the list above; absence of evidence only; see also the priority caveat at the top):
- the exact two-sided kink profiles and the unit odd amplitude in every generation;
- the second-order kink and edge laws with the universal offset $D=\lambda+\log2\pi+\gamma$ (proved here; $D$ was first fitted heuristically in public by span_of_dilates, comment EAw5pFmSdKxMBRHA);
- density with genuine singularity for every eigenfunction with $A\ne0$;
- the exact contact identity for the Weil form;
- the unconditional sharp zero-side tail law;
- the per-sector term in smoothed form.

Not ours: the activation eigenvalue law (rh_67 Thm 2.4; PL-338).

A specialist would call the kink law "a careful Abelian computation on top of (E)", and it should be framed that way.

---

## 8. How this fits with [N], and what to change there

**Fit.**
- [N] §15 said: "(E) and (H) are theorems; the two laws are not; each needs one more lemma."
- The missing lemmas are now supplied:
  - **N-kink** (the interior Abelian lemma) is Lemma P, plus Lemma O for the next order.
  - **N-tail (H1)**, the Fourier-side edge law, is T1 ([TA] Thm B, on dyadic windows). It also follows from [TE] Cor C2.
  - **N-tail (H2)** is not needed in the form [N] stated. T2 handles the zero sum directly through Riemann–von Mangoldt, Landau and the Sobolev box inequality.
- The **first-order** tail law and the kink law are therefore theorems. The **sharp second-order per-sector** tail term is not.

**Changes to carry into a v3 of [N]** (not yet made; read [N] with these updates):

| [N] place | Current | Change |
|---|---|---|
| §0 table, last row | "the kink law and the 1/T tail law themselves: not proved" | kink law to two orders: proved; first-order tail law: proved (unconditional, rate $1/\log T$); second-order per-sector: proved smoothed, sharp form open (Conjecture L) |
| §12 Open item 4 | sharp remainder $O(V^3)$ only numerical | proved (K1(a)); second order $A(\ell-D)^{-1/2}$ proved (K1(c)) |
| §13 N8 | $V_q\approx(\ell+q+c_a-\gamma)^{-1/2}$ numerical | theorem (Prop R), with two proofs |
| §13.1, prime-image bias mechanism | "ψ has a one-sided $\ell^{-3/2}$ germ at $y_n$" | two-sided germ $(\frac23,-\frac13)c_nA\ell^{-3/2}$ (K3) |
| §15 N-kink display | $\psi=g+c_nA\mathbf 1_{y<y_n}\ell^{-3/2}$ | wrong as stated unless $g$ contains the even cusp $-\frac13c_nA\ell^{-3/2}$ |
| §15 | "Recommendation: do N-kink and (H1) next" | done; next is Conjecture L via the kink law (§10.1 here) |
| Scope paragraph | "Do not claim the 1/T tail law or the kink-amplitude law" | "The kink law and the first-order tail law are proved, pending external review; do not claim the sharp per-sector term, $A_e\ne0$, or anything about RH" |
| Thm 2 observation | logarithmic modulus of $\lambda'$ at activation | still numerical; T3(b)'s $c_XA_+A_-z/\ell$ is the same structure, on the zero side |

**Corrections raised by the internal referees of the four write-ups, collected and applied in this note:**

*[TA]:*
- canonical $\Phi_c$ (T1, T4);
- unexpanded forms (T4);
- the $X=4$ residual does not bound the $q=1$ cross term;
- §10 wording: the proven $1/\log T$ error contains the arithmetic $c_X$ term;
- Cor E2 needs $A\ne0$ as an assumption;
- Lemma W needs the block summation;
- the constant $2.5$ needs $\sin x/x\ge-0.2173$;
- cite Gonek directly.

*[TE]:*
- Conjecture R needs the $nm$ hypothesis or term;
- 14 states, not 12;
- the $q$-test confirms cancellation at order $\ell^{-1/2}$ only;
- the Theorem E(ii) numerics are at the mesh floor;
- sign slip in Thm B′(a);
- $m_1(\varphi)\ne0$ in C4;
- deficit coefficient $\pi^2/12$.

*[KW]:*
- "fit-free given the $\delta u$ shift";
- the A-normalised check;
- the constant is $2.41509$, and the $L=1.19$ prediction needs $A_e\ne0$;
- K0 radius choice;
- Lemma 3.5 wording;
- K3 for all $L>\frac12\log6$;
- cite 2608.07315.

*[KL]:*
- the echo condition (Cor E);
- $L=1.19$, $p=2,3$ boosts;
- the Lemma T dominating function;
- the even part (Conjecture K7);
- de Haan attribution;
- Cor D "for the ground state";
- $\chi_5$/Davenport–Heilbronn offsets;
- Widder statement;
- rename $\kappa$;
- constant 8 in Thm A step 2.

---

## 9. Plain-language status (for a non-specialist)

| Question | Answer |
|---|---|
| What is the kink law? | The prime terms copy the window's edge behaviour into the interior, at $L-\log n$ and then at points reached by chains of such shifts. Each copy is one logarithm weaker. At a first copy the eigenfunction has a kink: up by $\frac23$ of $c_nA(\log\frac1d)^{-3/2}$ on one side and down by $\frac13$ on the other. |
| Is it proved? | **Yes**, to two orders for the jump (the even part at second order is Conjecture K7), for every eigenfunction, every window and every pole strength. It was proved in two independent write-ups, refereed internally by AI referees, and confirmed by an independent code to better than 0.4%. Pending external review. |
| What does it imply? | For windows wider than $\log6$ (about $L>0.9$), the eigenfunction is rough everywhere whenever $A\ne0$: no Hölder bound on any interval. Numerical methods must grade their meshes at every chain point coupled to what they measure. |
| What is the tail law? | Of the eigenfunction's "energy", the part carried by zeta zeros above height $T$ is about $\lvert\lambda'(L)\rvert/(\pi T)$: how fast the eigenvalue moves with the window controls how much weight sits on high zeros. |
| Is it proved? | **First order: yes**, with error $O(1/\log T)$ and **no assumption on the zeros**. **Second order:** the extra $\pm c_X/\log T$ for even/odd states when $e^{2L}$ is a prime power is proved for smoothed tails. For the sharp tail it is proved only for the main part; a cross term remains open (Conjecture L). Numerics on real zeros agree. |
| Does this say anything about RH? | **No.** These are statements about a quadratic form and how its eigenfunctions pair with the zeros, whatever the zeros are. |
| Does it help the true even ground state? | Not yet. Both laws scale with $A_e$, and $A_e\ne0$ for the true form at a given $L$ is open (equivalent to the simple-even hard core). $A_e$ is also astronomically small there ($\sim10^{-24}$ at $L=1.2$), so the laws are asymptotic only. |
| How sure are we? | The proofs rest on [N], which has not been read by an outside specialist. Everything new in this note (T3's rate, T5, T6) was checked only by the internal final referee. All refereeing so far is by AI referees. |

---

## 10. Next steps

### 10.1 Close Conjecture L with the kink law (Route S, "singularity calculus")

**Why it should work.**
- T1's remainder bound $\mathsf B^2/(T\log^3T)$ is saturated by the kinks themselves: a first-generation kink has $|\hat\psi_{\rm kink}|^2\sim c_n^2A^2/(t^2\log^3t)$.
- Cauchy–Schwarz then gives exactly the $1/\log T$ cross term.
- If the kinks are subtracted with their **explicit** transforms, the remaining shell mass should be $O(1/(T\log^5T))$ (generation 2), and Cauchy–Schwarz then gives $O(\ell^{-2})$.

**Plan.**
1. **Fourier asymptotics of the two-sided germs** (Wong–Lin 1978 type, with remainders). Take $\mathfrak D$ and $\mathfrak S$ at generation $k$, from K3, K5 and Conjecture K7 (so the even part is conditional). The odd part transforms to $\approx\Omega_ke^{itz}\,(i/t)(\log t-D)^{-k-1/2}$; the even part enters one order lower.
2. **Finite chain sets first.** Enumeration (`checks/chain_enum.out`) gives:
   - $X=4$: 5 points, $\{0,\pm0.288,\pm0.405\}$, with a coincidence at $0$ since $4=2\cdot2$;
   - $X=5$: 22 points, generations $\le6$, including a close pair $\pm0.006$ that hurts the constants;
   - $X=5.9$ (just below $\log6$): 270 points by generation 12, still growing. So "$2L<\log6$" alone does not make the set finite.

   $X=4$ is the clean test case. Write
$$F=M+\sum_{p\in C_L,\ g(p)\le2}e^{itp}S_p(t)+R'' .$$
3. **The zero sum of edge×kink.** By Landau at $x=n$ (Gonek near resonance), this gives $-\kappa c_n^2/\ell^2$ with an explicit $\kappa$. Edge×opposite kink at $X=nm$ gives the sector term. This yields $k_{\rm eff}$ and the $X=6,8,10$ $\beta$-coefficients, to compare with [NUM].
4. **The remainder.** Bound $R''$ by Lemma Z and Cauchy–Schwarz with the improved shell mass.
5. **Numerical companion.** Use the P1 code at $X=4$ (finite chain set; both sectors; every coupled point graded through the fit window, the [NUM] lesson). Measure $\int_T^{2T}|F-M-\sum S_p|^2$ and the sector split with a free $a^{-2}$ term. $X=4$ was not run by [NUM].

**Kill criterion.** If the de-singularised shell mass $T\log^4T\int_T^{2T}|R''|^2$ grows with $T$ on the P1 data at $X=4$, stop: then something besides the chain germs carries Fourier mass at order $\ell^{-3}$.

### 10.2 $A_e\neq0$ for the true even ground state

**Assessment: not approachable with the methods of this note.**
- The new laws give three independent observables of $A_e$: the edge, the kink jumps $c_nA_e\ell^{-3/2}$, and the zero tail $\pi TZ\to2A_e^2$.
- None of them supplies a positivity mechanism.
- Through the rank-one pole, $A_e(s{=}1)\ne0$ is equivalent to the simple-even hard core ([N] §15).

The three approaches of [N] §15 stand, with their kill criteria:
- the rank-one $\tau(\lambda)$ zero count;
- the Krein-string nodal count;
- Arb certification of $A_e$ through the explicit formula $A_+=\int v_qf_q$.

Two adjustments:
- **Certification.** It is realistic only for $L\le0.6$ ($A_e\approx0.06$ at $L=0.4$, $\approx2.4\cdot10^{-4}$ at $L=0.6$). For $L\ge1.2$, $A_e\sim10^{-24}$–$10^{-45}$, so the task is the certified-$\lambda_0$ problem itself.
- **A cheap consistency check (not a proof).** At $L\le0.5$, certify one kink jump $\mathfrak D_\psi(y_2;d)$ and the edge value at the same $\ell$. K6 predicts their ratio exactly ($1/\rho=\ell-D-\beta_2+O(1/\ell)$), with no free constant. A certified agreement would tie the certified simple-even pipeline to the analytic theory.

### 10.3 Three cross-field alternatives for what failed

What failed or stayed open:
- (i) the sharp per-sector law (Conjecture L);
- (ii) Conjecture R in its stated form;
- (iii) the $X=10$ control (uninformative);
- (iv) the heuristic P6 for even states;
- (v) the registered $L=1.0$ K5 test (a mesh defect, since diagnosed).

Items (ii) and (iv) feed into §10.1. Item (v) is fixed by the meshing rule. For (i):

1. **Analytic number theory and Abelian asymptotics: Route S (§10.1).**
   - *First step:* the $X=4$ germ transforms and the edge×kink Landau sums.
   - *Kill:* as in §10.1.
2. **Harmonic analysis: Beurling–Selberg extremal functions plus a Tauberian remainder theorem, under RH positivity.**
   - Under RH, $Z(T)$ is monotone and $h=|F|^2\ge0$.
   - Majorants and minorants of $\mathbf 1_{|t|>T}$ with Fourier support $|z|\le1/(\epsilon T)$ give the sharp tail from cosine-smoothed tails at all $z\le1/(\epsilon T)$, with loss $O(\epsilon)$ relative. Compare Carneiro–Chandee–Milinovich, arXiv 1503.00955, for $S(t)$; Ganelius, *Tauberian Remainder Theorems*, LNM 232; Korevaar, *Tauberian Theory*, Ch. VII; and the survey arXiv 2504.16233.
   - With T3's error $O(z\ell^{-3/2})$ the total relative error is $\epsilon+\epsilon^{-1}\ell^{-3/2}$, i.e. $O(\ell^{-3/4})$. That is not enough.
   - With the position-side contact law carried to $O(z\ell^{-3})$, including the kink $\ell^{-2}$ terms, it gives $O(\ell^{-3/2})$, which is Conjecture L under RH.
   - *First step:* extend [TE] Thm E to $O(z\ell^{-2})$ using K1(c) and the generation-1 moduli $O(\ell^{-3/2})$ (an internal referee's sharpness remark).
   - *Kill:* if the contact law at $O(z\ell^{-3})$ needs interior control uniform over a dense chain set (so that it works only where the chain set is finite) **and** Route S succeeds there anyway, drop this route. It would add only the RH-conditional case.
3. **Analytic combinatorics and prime-number-theorem methods: Wiener–Ikehara/Delange on the Mellin transform of the zero-weighted measure.**
   - $\mathfrak M(\sigma)=\sum_\rho h(\gamma_\rho)(1+\gamma_\rho^2)^{-\sigma/2}$ is given **exactly** by the explicit formula as archimedean + prime + pole parts.
   - The prime sum converges absolutely, because the kernel of $(1+w^2)^{-\sigma/2}$ decays like $e^{-|x|}$.
   - The singular behaviour at $\sigma=-1$ is read off from the singularities of $g=\psi*\tilde\psi$ at $0$ and $\log n$, which K1, K3 and K5 now give explicitly: log-type singularities.
   - A Delange-type Tauberian theorem (positive measure, under RH) needs the remainder to be continuous on the whole line $\operatorname{Re}\sigma=-1$. That is a "no resonance on the line" statement, the analogue of $\zeta(1+i\tau)\ne0$ in the prime number theorem.
   - *First step:* write $\mathfrak M$ via the explicit formula at $X=4$ and isolate the singular part.
   - *Kill:* if continuity on the line needs the same mean-square improvement as Conjecture L (block sums $\sum_k(\text{cross}_k)T_k<\infty$ is exactly Conjecture L at $\ell^{-1-\delta}$), the route is circular. Stop.

*Light prior-art check* (web, 2026-10-31): nothing found that combines Tauberian remainder theorems or Beurling–Selberg majorants with a second-order tail of $\sum|F(\gamma)|^2$. The nearest items are Carneiro–Chandee–Milinovich (majorants for $S(t)$ under RH) and Mazhouda, arXiv 1505.01544 (asymptotics of $\sum_\rho e^{u\rho^2-v\rho}$). The check was light and is absence of evidence only.

### 10.4 Smaller items

1. **External specialist reading of [N].** It is the base of everything here. Ask the Kwaśnicki circle for Prop 5.1 and the half-line inversion; ask an analytic number theorist for T2/T4 (Landau with off-line zeros, Lemma Z).
2. **Refereeing.**
   - Write out Conjecture K7 (the even part) in full and have it refereed.
   - Referee T3's step (a) and T5/T6; they are short.
3. **Possible improvements:**
   - [TE] Thm E(ii) to $O(z\ell^{-2})$; this would improve T3 and T5 to $O(\ell^{-2})$;
   - prove the $M_K$ analogue of V2 (deficit $\pi^2/(12\ell)$).
4. **Numerics.** A kink-resolved P1 run at $X=4$ and $X=5$, with every chain point graded (5 and 22 points; `checks/chain_enum.out`).
   - $X=4=2\cdot2$ carries an $nm$ sector term ($2c_2^2=0.48$) and the coincidence $y_2=-y_2=0$.
   - $X=5$ has no $nm$ term but a close chain pair at $\pm0.006$.
   - Use the derivative-free split with a free $a^{-2}$ term. Pre-register.
5. **Papers.** See §2.2.

---

## 11. Files

| File | Contents |
|---|---|
| `tail_kink_laws_note.md` | this note |
| `checks/chain_enum.py`, `checks/chain_enum.out` | enumeration of interior chain points at $X=4,5,5.9,6.5$: finite at 4 and 5, growing just below and above $\log6$ |
| `checks/denominators_check.py`, `checks/denominators_check.out` | constants; the exact cosine moments $1-\gamma$ and $1+\pi^2/12$; the canonical smoothed and sharp main-term factors against $1/(\ell-D+1)$ and $1/(\log\frac T{2\pi}-\lambda+1)$ at $\ell,\log T=20,40,80$ and $\lambda=0,-2,-4.5$ (mpmath, about 2 min) |
| `checks/fr_constants.py`, `checks/fr_constants.out` | the internal final referee's independent recomputations (symbol constants, T6 moments, R2, Lemma T, Lemmas P and O on a model kernel, the Landau sign on 10 500 zeros, the boost table) |
| `referee_summary.md` | the final referee's verdict table and what still needs a specialist |
| `../numerics/` | [NUM], the pre-registered P1 test |

Not included: the four internal write-ups [TA], [TE], [KW], [KL], their internal referee reports, and the internal novelty audit.
