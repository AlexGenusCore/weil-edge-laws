# Edge law and Hadamard formula for the localized Weil form (v2)

*Johann Alexander Botha (GenusCore, info@genuscore.com). Research note, version 2, dated 2026-10-31.*

> **Status.** Research note, dated 2026-10-31, posted to make the work public and citable. **It is not peer-reviewed.** It was produced largely with an AI assistant (Anthropic's Claude, via Claude Code), directed by the author, Johann Alexander Botha (GenusCore, info@genuscore.com). The only checking so far is by AI referees, in internal review rounds:
> - edge law and Hadamard formula: four internally refereed write-ups (each with a referee, a repair and a second referee), then a final referee who re-checked the chain line by line and recomputed the decisive constant with independent code;
> - kink and tail laws: two independent write-ups per law, each internally refereed, a pre-registered independent numerical test, then a final referee (verdict table in [`referee_summary.md`](referee_summary.md)).
>
> No human expert has checked any of it. Nothing here proves or disproves the Riemann hypothesis.
>
> **Priority: earlier work on rStation.** Several results in these notes were obtained earlier by the AI-agent author `bramble_trace` on rStation, a research platform for AI agents: *Boundary traces and support variation for localized Weil operators*, riemann_hypothesis paper 67, v1 published 2026-10-27 19:07 UTC (https://rstation.ai/problems/riemann_hypothesis/papers/67/v1); its trace-existence lemma first appeared in a forum comment on 2026-10-18. That paper proves: (i) existence of the endpoint traces for every eigenfunction of the localized Weil operator, primes and pole included (its §3.3, without a rate); (ii) the support-variation (Hadamard) law for isolated clusters, $\lambda_k'(a)=-|\tau_-|^2-|\tau_+|^2$ on simple branches including prime activations, and $B_-=B_+$, rank $\le1$ on eigenspaces (Theorems 2.1–2.2); (iii) an activation formula at prime powers (Theorem 2.4); (iv) for the pure $\log|D|$: every interval eigenvalue is simple and $|\tau_\pm|^2=1/(2a)$ (Corollary 2.3). We learned of it from an external reviewer after writing these notes; our proofs are independent and in part different (for the trace value we use a dilation/cross identity). We claim **no priority** for (i)–(iv). Not found there: the $O(\ell^{-1})$ rate and the explicit formula for $A$ (Theorem 1), the second-order edge law, the mixed and edge-free identities, and the kink and tail laws. rStation hosts many other AI-agent papers on this problem; our comparison with them is still in progress, so throughout these notes "new" means only "not found in our search".
>
> **Related recent work.** Veltri, a preprint on log|D| on an interval, Zenodo record 23769666 (2026-10-29). We list it as recent related work and do not characterise its content further.
>
> **What is claimed, and what is not.**
> - The edge law (E) and the Hadamard formula (H) are proved, pending external review.
> - The kink-law items K1–K6 and the tail-law items T0–T6 were accepted by the internal final referee (an AI referee).
> - Open: Conjecture K7 (second-order even part of the kink), Conjectures L and R, and Prediction F (sharp second-order tail law).
> - Open: $A_e\neq0$ for the true even ground state. This is equivalent to the simple-even problem.
> - The laws are asymptotic, and they are vacuous wherever $A=0$. For the true form at $L\ge1.2$, $A_e\sim10^{-24}$, so they say nothing at accessible scales.

*Status of this note in detail.*
- Proved, modulo the standard theorems listed in §12. Theorem 5(d) on $(0,1.19)$ also uses the author's computer-assisted simple-even theorem [GS] as an input.
- Refereeing, described honestly: four internally refereed write-ups of closely related arguments (attempt, referee, repair, second referee each; all "correct with minor gaps"; they share one mechanism and one numerical solver, §12), then one final internal referee who checked v1 line by line, recomputed the decisive constant with independent code (§13.1) and returned "accept as proved". All referees were AI referees.
- No specialist outside this project has read it. Use "proved, pending external review" in any external text.
- This is analysis of a quadratic form, not a statement about RH.

*Note added (2026-10-31).* The last rows of the §0 table, §12 open items 4–5, §13 N8, the "one-sided germ" in §13.1 and all of §15 predate the companion note [`tail_kink_laws_note.md`](tail_kink_laws_note.md). That note proves the kink law to two orders and the first-order tail law, and it corrects the one-sided germ to a two-sided one. Its §8 lists the updates to carry into this note.

**Changes from v1.** v1 was an internal draft (not public). Items M1–M6 are the issue labels of the internal final referee's report on v1.
1. **§14 rewritten** (M1, M5). Prior art now includes Kwaśnicki 2011 (Lemma 4.27, Example 6.4: the exact half-line edge law), Grzywny–Kwaśnicki 2018 (Thm 1.11: boundary limits of ratios), FJW22 Remark 1.2(iii), the withdrawn arXiv 2411.15985, mathia PL-306 and PL-319–338 (credit for (E) in substance and for the activation mechanism PL-338), and Eberwein §13 (credit for the locations of the weak singular points). The novelty claim is narrowed to (E) on intervals with primes and pole, (H), Theorems 3 and 4, and means only "not found in our literature search" (§14.3; subject to the priority caveat at the top). Every citation in §14 was re-checked (table in §14.4).
2. **Correction found in the citation check** (not raised by the referee): v1 said FJW22 Remark 1.2(iii) lists the optimal boundary rate of the log-Laplacian as open. That remark is about the uniform-in-$s$ boundary decay of fractional eigenfunctions as $s\to0^+$. Corrected in §14.1.
3. **§13 evidence fixed** (M2). The fit-free checks confirm the identities, not the constant; Theorem 4 is not an independent check of the constant; the independent confirmation is the final referee's P0 code, tabulated in §13.1 with the derived ratios recomputed and two runs reproduced.
4. **"Four independent routes" replaced** by an honest description (M3; status above, §12, Appendix).
5. **Theorem 5(d)** is now stated on an open interval, with [GS] named as an input, giving $(0,1.19)$ (M4; §2, §11).
6. **Wording** (M5, M6): $\langle\psi_o,\psi_e'\rangle$ means $\Phi'(0)$ wherever it occurs; $w_{\log}$ is bounded only on functions supported in a bounded window; §0 now says "(E) and (H) are theorems; the two laws are not"; mathia PL-338 and PL-306 are credited. Also new: the "logarithmic modulus of $\lambda'$ at activation points" (v1, after Theorem 2) is marked as a numerical observation, since it is not proved.
7. **Prop 5.1 (Wiener–Hopf/Silverstein inversion) and Lemma 6.1 ($L^\infty$ bound) written out in full**, with every hypothesis stated where it is used (referee item 4). The Dirichlet-form facts they use are now a separate Lemma 3.6. Lemma 3.2(b) (density), which Prop 5.1 needs, has a fuller proof. Lemma 6.1 no longer cites Pazy: the exponential formula and Duhamel's formula are derived from the spectral theorem.

**Errors found in this revision: none in any theorem or proof.** No theorem was changed. The corrections are to statements *about* the work (items 2, 3, 4, 6).

---

## 0. Summary

**In plain words.** The localized Weil form $Q_L$ has a lowest eigenfunction $\psi$ in each parity sector. Near the window edge $x\to L$ it decays like a constant times $\log(1/(L-x))^{-1/2}$. The constant, the **edge trace** $A$, controls how fast the eigenvalue falls as the window grows: $d\lambda/dL=-2A^2$.

Both facts were numerical observations, and they were the two unproven inputs behind the 1/T tail law and the kink-amplitude law. **(E) and (H) are now theorems**, for the true form with all primes and the pole, at every window size. **The two laws themselves are not**: each still needs one more lemma (§15). The method is classical potential theory of an order-zero jump process; no fractional regularisation and no Pohozaev identity with $x\psi'$ are used.

| # | Statement | Status |
|---|---|---|
| Thm 1 (E) | For every $L>0$ and every eigenfunction (any sector, any multiplicity, any pole strength, $e^{2L}$ arbitrary), $A_\pm=\lim\psi(\pm(L-r))\,\ell(r)^{1/2}$ exists, with rate $\psi(\pm(L-r))=A_\pm\ell(r)^{-1/2}+O(\ell(r)^{-1})$ and an explicit formula for $A_\pm$. | **proved** |
| Thm 2 (H) | If $\lambda$ is simple in its parity sector, then $\lambda$ is $C^1$ in $L$ and $\lambda'=-(A_+^2+A_-^2)=-2A^2$. The constant 2 (one $A^2$ per endpoint) comes from Lemmas 8.2–8.3; absolute-amplitude numerics, including an independent code, agree (§13.1). No prime-power exclusion. | **proved** |
| Thm 3 | Translation identity. Consequences: $\lvert A_+\rvert=\lvert A_-\rvert$; the trace map has rank $\le1$ on every eigenspace; the mixed identity $(\lambda_e-\lambda_o)\langle\psi_o,\psi_e'\rangle=2A_eA_o$, where $\langle\psi_o,\psi_e'\rangle:=\Phi'(0)$ is a difference-quotient pairing, not an integral; $A_eA_o=0$ at even/odd crossings; the edge-free identity $[(\lambda_e-\lambda_o)\langle\psi_o,\psi_e'\rangle]^2=\lambda_e'\lambda_o'$. | **proved** |
| Thm 4 | Pure log symbol: every eigenfunction has $A_+^2=A_-^2=1/(2L)$, and every Dirichlet eigenvalue on an interval is simple. | **proved** |
| Thm 5 | Nonvanishing. (a) Pole strength $s\le0$: the ground state is simple, even and $\ge0$; $A>0$ and $\lambda_0'<0$ at every $L$. (b) $2L\le\log2$, any $s\ge0$ (true form included): the odd ground state is simple, $A_o>0$. (c) Hence hypothesis H6 of [BC] (§14.2) holds for $2L\le\log2$, and an even/odd crossing forces $A_e=0$ there. (d) True form ($s=1$): on any open $L$-interval where the overall ground state is simple and even, $A_e$ vanishes at most on a relatively closed nowhere-dense set. The certified simple-even theorem [GS] (an input; computer-assisted, unrefereed) supplies the interval $(0,1.19)$. | **proved** ((d) on $(0,1.19)$: conditional on [GS]) |
| — | $A_e\ne0$ at a given $L$ for the even ground state of the true form; $A_o\ne0$ once primes are active | **open** (§15) |
| — | asymptotics of $\psi'$ at the edge | **not proved, and not needed** |
| — | the kink law and the 1/T tail law themselves | **not proved**; one further lemma each (§15) |

**Scope for any external text** (final referee). Say: "The edge law and the Hadamard formula for the localized Weil form (an order-zero nonlocal operator) are proved, pending external review." Do not claim the 1/T tail law or the kink-amplitude law, $A_e\neq0$ for the true even ground state, or any implication for RH. Quote the mixed identity only with the $\Phi'(0)$ caveat.

---

## 1. Setting and normalisation

- **Fourier transform.** $F(t)=\int f(x)e^{ixt}dx$, so $\|f\|^2=\frac1{2\pi}\int|F|^2$. Write $\ell(r):=\log(1/r)$ for $0<r<1$.
- **The form.** The form of [GS, §2] with the pole multiplied by a strength $s\in\mathbb R$; $s=1$ is the true form:
$$Q^{(s)}_L(f)=\frac1\pi\int_0^\infty\Psi_L(t)|F(t)|^2dt+2s\,F(\tfrac i2)F(-\tfrac i2),\qquad f\in L^2,\ \operatorname{supp}f\subset[-L,L].$$
- **Kernels.** $b(u)=\dfrac{2e^{-u/2}}{1-e^{-2u}}=2\sum_{k\ge0}e^{-a_ku}$ with $a_k=2k+\tfrac12$, and $J(u):=\tfrac12 b(|u|)=\dfrac1{2|u|}+\dfrac14+O(|u|)$.
  - $J$ is completely monotone in $|u|$, hence positive and strictly decreasing.
  - $J(u)\le Ce^{-|u|/2}$ for $|u|\ge1$.
- **Archimedean symbol.** $\Psi_a(t):=\operatorname{Re}\psi(\frac14+\frac{it}2)-\psi(\frac14)$, where $\psi$ is digamma. The eigenfunction is also called $\psi$; context decides.
- **Jump form.**
$$\mathcal E(f,g)=\tfrac12\iint(f(x)-f(y))(g(x)-g(y))J(x-y)\,dx\,dy=\tfrac1{2\pi}\int\Psi_aF\bar G,$$
  with domain $D(\mathcal E)=\{f\in L^2:\int\log(2+|t|)|F|^2<\infty\}$. Equivalently, $D(\mathcal E)$ is the set of $f\in L^2$ for which the double integral is finite (Tonelli and Lemma 4.1).
- **Bounded part.** Put $c:=\psi(\tfrac14)-\log\pi$, $c_n:=\Lambda(n)/\sqrt n$, and
$$(W_sf)(x)=c\,f(x)+2s\!\int\!\cosh\tfrac{x-y}2\,f(y)\,dy-\sum_{n\ge2}c_n\big(f(x+\log n)+f(x-\log n)\big),\qquad w_s(f,g)=\int(W_sf)g .$$
- **Domains.** For a bounded open interval $I$, $D_I:=\{f\in D(\mathcal E):f=0\text{ a.e. off }\bar I\}$ and $D_L:=D_{(-L,L)}$. Also $D_+:=\{f\in D(\mathcal E):f=0\text{ a.e. on }(-\infty,0)\}$.
- **Operator.** $A^{(s)}_L$ is the self-adjoint operator of the closed form $(\mathcal E+w_s)|_{D_L}$ on $L^2(-L,L)$. It has compact resolvent and commutes with $x\mapsto-x$.
  - $\lambda^\sigma_k(L)$ is the $k$-th min-max value in sector $\sigma\in\{e,o\}$.
  - An eigenfunction is always real and $L^2$-normalised.
- **Pure log symbol.** $Q^{\log}_L(f)=\frac1{2\pi}\int\log|t|\,|F|^2$ on $D_L$, the half log-Laplacian of Chen–Weth.
  - Since $\log|t|=\frac12\log(1+t^2)-\frac12\log(1+t^{-2})$, we have $Q^{\log}=\mathcal E_{VG}+w_{\log}$.
  - $\mathcal E_{VG}$ is the jump form with $J_{VG}(u)=e^{-|u|}/(2|u|)$ and symbol $\frac12\log(1+t^2)$, by Frullani.
  - $w_{\log}(f)=-\langle k*f,f\rangle$ with $k(x)=(1-e^{-|x|})/(2|x|)\in(0,\frac12]$; it is translation-invariant and independent of $L$.
  - $w_{\log}$ is bounded **only on functions supported in a bounded window**: for $f$ supported in an interval $I''$ of length $\ell''$, $\|\mathbf 1_{I''}(k*f)\|_p\le\ell''\|f\|_p$. It is not bounded on $L^2(\mathbb R)$, because $k\sim1/(2|x|)$ is not in $L^1(\mathbb R)$. Only the windowed bound is used.
  - Every statement below for $Q^{(s)}$ holds verbatim for $Q^{\log}$, with $(J,\Psi_a,w_s)$ replaced by $(J_{VG},\frac12\log(1+t^2),w_{\log})$. Remarks in §§4–6 say where the replacement matters.

**Edge trace.** For an eigenfunction $\psi$ on $(-L,L)$, $A_\pm(\psi):=\lim_{r\downarrow0}\psi(\pm(L-r))\,\ell(r)^{1/2}$ whenever the limit exists. Theorem 1 shows it always exists. For parity states $A_-=\pm A_+$, and we write $A:=A_+$.

## 2. Main results

Fix $0<L_{\min}\le L_{\max}$, $\Lambda_0>0$ and $s$ in a compact set. "Constant" means a number depending only on these and on the fixed cutoff $\chi$ of §7. Put $\rho_0:=\min(L_{\min}/4,e^{-1})$.

**Theorem 1 (edge law).** Let $L\in[L_{\min},L_{\max}]$, let $\lambda$ be any eigenvalue of $A^{(s)}_L$ with $|\lambda|\le\Lambda_0$, and let $\psi$ be any eigenfunction. Simplicity, parity and the arithmetic of $e^{2L}$ play no role.
1. $\|\psi\|_\infty\le C$. Moreover $\psi$ has a representative that is continuous on $\mathbb R$ and vanishes off $(-L,L)$.
2. The limits $A_\pm$ exist, and for $0<r\le\rho_0$
$$\big|\psi(\pm(L-r))-A_\pm V(r)\big|\le C\,V(r)^2,\qquad \big|\psi(\pm(L-r))\,\ell(r)^{1/2}-A_\pm\big|\le C\,\ell(r)^{-1/2}.$$
   Here $V=V_1$ is the renewal function of §4, with $V(r)\ell(r)^{1/2}=1+O(\ell(r)^{-1})$.
3. *Explicit formula.* Let $\tilde\psi(r)=\psi(L-r)$ and $\mu(y)=\int_0^{2L}J(y-r)\tilde\psi(r)\,dr$ for $y>2L$. Then for every $q>0$,
$$A_+=\int_0^\infty v_q(r)\,f_q(r)\,dr,\qquad f_q:=\mathbf 1_{(0,2L)}\big[(q+\lambda)\tilde\psi-W_s\tilde\psi\big]-\mathbf 1_{(2L,\infty)}\,\mu ,$$
   where $v_q>0$ is the completely monotone density of §4. The same holds at $-L$ by reflection.

**Theorem 2 (Hadamard formula).** Suppose $\lambda^\sigma_k(L_0)$ is simple in its sector. Then on a neighbourhood $N$ of $L_0$:
- $\lambda:=\lambda^\sigma_k$ is $C^1$ and
$$\frac{d\lambda}{dL}=-\big(A_+(L)^2+A_-(L)^2\big)=-2A(L)^2 ;$$
- quantitatively, for $L_1<L_2$ in $N$ with $\delta=L_2-L_1\le\rho_0$,
$$\Big|(\lambda(L_2)-\lambda(L_1))\langle\psi_{L_1},\psi_{L_2}\rangle+\textstyle\sum_\pm A_\pm(L_1)A_\pm(L_2)\,\delta\Big|\le C\delta\,(1+\log\ell(\delta))\,\ell(\delta)^{-1/2}.$$

No condition on $e^{2L_0}$ is needed; in particular $\lambda$ is $C^1$ through every activation point $2L=\log n$.

*Observation, not proved.* Numerically (§13, N6), $\lambda'$ has only a logarithmic modulus of continuity at an activation point. The mechanism is the contribution of the newly active prime channel, analysed in mathia PL-338 (§14.2).

**Theorem 3 (translation identity).** Let $\psi_1,\psi_2$ be eigenfunctions of $A^{(s)}_L$ with eigenvalues $\mu_1,\mu_2$, and let $\tau_h\psi(x)=\psi(x-h)$. As $h\downarrow0$,
$$(\mu_1-\mu_2)\langle\psi_1,\tau_h\psi_2\rangle=\big(A_+^{(1)}A_+^{(2)}-A_-^{(1)}A_-^{(2)}\big)h+O\big(h(1+\log\ell(h))\ell(h)^{-1/2}\big).$$
Consequences:
- (a) $|A_+(\psi)|=|A_-(\psi)|$ for every eigenfunction.
- (b) On each eigenspace $E_\lambda$, the trace map $\psi\mapsto(A_+,A_-)$ has rank $\le1$. So if $\dim E_\lambda=m$, an $(m-1)$-dimensional subspace has $A_\pm=0$.
- (c) For an even $\psi_e$ and an odd $\psi_o$, put $\Phi(h)=\langle\psi_o,\psi_e(\cdot+h)\rangle$. Then $(\lambda_e-\lambda_o)\Phi(h)=2A_eA_o\,h+o(h)$. So if $\lambda_e\ne\lambda_o$, then $\langle\psi_o,\psi_e'\rangle:=\Phi'(0)$ exists and $(\lambda_e-\lambda_o)\langle\psi_o,\psi_e'\rangle=2A_eA_o$. This is the identity formulated in [BC].
- (d) If $\lambda_e=\lambda_o$, then $A_eA_o=0$.
- (e) If both are sector-simple, then $[(\lambda_e-\lambda_o)\langle\psi_o,\psi_e'\rangle]^2=\lambda_e'\lambda_o'$.

**Caveat on the pairing.** Here and everywhere in this note, $\langle\psi_o,\psi_e'\rangle$ *means* the derivative $\Phi'(0)$ of the translation pairing. It is not claimed to equal $\int\psi_o\psi_e'$, because $\psi_e\in W^{1,1}$ (or $BV$) is not proved. Any quotation of (c) or (e) must keep this caveat.

**Theorem 4 (pure log symbol).** For $Q^{\log}_L$, Theorems 1–3 hold. In addition:
- every eigenfunction, simple or not, has $A_+^2=A_-^2=\frac1{2L}$;
- every Dirichlet eigenvalue of $Q^{\log}_L$ is simple;
- $\lambda_k'(L)=-1/L$ for all $k$.

**Theorem 5 (nonvanishing).**
- (a) Let $s\le0$; this includes the pole-free form, archimedean part plus all primes. At every $L>0$:
  - the lowest eigenvalue $\lambda_0(L)$ of $A^{(s)}_L$ is simple;
  - its eigenfunction can be taken $\ge0$ and is even;
  - $A>0$;
  - $\lambda_0\in C^1(0,\infty)$ with $\lambda_0'=-2A^2<0$.
- (b) Let $2L\le\log2$ and $s\ge0$; this includes the true form for $L\le0.3466$.
  - The lowest odd eigenvalue is simple in the odd sector.
  - Its eigenfunction can be taken $\ge0$ on $(0,L)$.
  - $A_o>0$ and $\lambda_o'=-2A_o^2<0$.
- (c) In the setting of (b), suppose an even eigenvalue of $A^{(s)}_L$ equals the odd ground level. Then every even eigenfunction at that level has $A_e=0$. In particular, at the crossing strength $s_{\rm up}(L)$ of [BC], the even ground state has a vanishing edge trace whenever $2L\le\log2$. So H6 of [BC] holds there and the identification "$s_{\rm up}$ is a zero of $s\mapsto A_e(s)$" is unconditional.
- (d) Let $s=1$, and let $U$ be an open $L$-interval such that for every $L\in U$ the lowest eigenvalue of $A^{(1)}_L$ is simple with an even eigenfunction. Then $\{L\in U:A_e(L)=0\}$ is relatively closed in $U$ and has empty interior.
  - **Input.** The certified simple-even theorem [GS, §3] states exactly this hypothesis for every $L\in(0,1.19]$, for the form of [GS, §2], which is $Q^{(1)}_L$ (Lemma 3.1). So $U=(0,1.19)$ qualifies. [GS] is computer-assisted and unrefereed; the conclusion on $(0,1.19)$ is conditional on it.

---

## 3. The form, the domains, and the bounded part

**Lemma 3.1 (one $L$-independent form).** For $f\in D_L$, $Q^{(s)}_L(f)=\mathcal E(f)+w_s(f)$. Both $\mathcal E$ and $w_s$ are independent of $L$ and invariant under translations and under $x\mapsto-x$.

*Proof.*
- $\operatorname{Re}\psi(\frac14+\frac{it}2)-\log\pi=\Psi_a(t)+c$. Since $|F|^2$ is even, $\frac1\pi\int_0^\infty(\Psi_a+c)|F|^2=\mathcal E(f)+c\|f\|^2$.
- With $g(y)=\int f(x)f(x-y)\,dx$, we have $\frac1\pi\int_0^\infty\cos(t\log n)|F|^2=g(\log n)$. For $f\in D_L$, $g(\log n)=0$ when $\log n\ge2L$, so the cut $\log n<2L$ is automatic.
- The pole: $2F(\frac i2)F(-\frac i2)=2\iint f(u)f(v)\cosh\frac{u-v}2$.
- Invariance: $\mathcal E$ is a Fourier multiplier, the shifts commute with translations, and $F_{\tau_hf}(\pm\frac i2)=e^{\mp h/2}F_f(\pm\frac i2)$.
- The constant agrees with the paper's position side: on $D_L$, $-g(0)\log(1-e^{-4L})$ completes the truncated integral, and $\int_0^\infty\frac{2(e^{-x/2}-e^{-2x})}{1-e^{-2x}}dx=\psi(1)-\psi(\frac14)$. ∎

**Lemma 3.2 (domains).**
- (a) $D_L$ is the form-norm closure of $C_c^\infty(-L,L)$, so $A^{(s)}_L$ is the paper's operator.
- (b) $D_+$ is the closure of $C_c^\infty(0,\infty)$.
- (c) The dilations $f\mapsto f(\cdot/\theta)$, $\theta\in[\frac12,2]$, are uniformly bounded in form norm and strongly continuous in $\theta$.

*Proof.*
- (c) $\Psi_a(t)=\varphi(t^2)$ with $\varphi$ Bernstein (Lemma 4.1), and Bernstein functions satisfy $\varphi(\kappa x)\le\kappa\varphi(x)$ for $\kappa\ge1$. Together with $\hat f_\theta(t)=\theta\hat f(\theta t)$, this gives uniform boundedness. Strong continuity holds on $C_c^\infty$, hence everywhere by density.
- (a) Dilate into $(-\theta L,\theta L)$ with $\theta<1$, then mollify; the multiplier satisfies $|\hat\rho_\epsilon|\le1$.
- (b) Let $f\in D_+$ and write $\|\cdot\|_{\mathcal E_1}^2=\mathcal E(\cdot)+\|\cdot\|^2$.
  - *Translate.* $\tau_hf$ vanishes on $(-\infty,h)$, and $\|\tau_hf-f\|_{\mathcal E_1}^2=\frac1{2\pi}\int(1+\Psi_a)|e^{iht}-1|^2|F|^2\to0$ as $h\downarrow0$, by dominated convergence.
  - *Mollify.* For $\varepsilon<h$, $\rho_\varepsilon*\tau_hf$ is smooth, vanishes on $(-\infty,h-\varepsilon)$, and tends to $\tau_hf$ in $\|\cdot\|_{\mathcal E_1}$ as $\varepsilon\to0$, since $|\hat\rho_\varepsilon|\le1$ and $\hat\rho_\varepsilon\to1$.
  - *Cut off.* $g=\rho_\varepsilon*\tau_hf$ has all derivatives in $L^2$, so $g\chi(\cdot/R)\to g$ in $H^1$ as $R\to\infty$ (with $\chi\in C_c^\infty$, $\chi=1$ on $[-1,1]$). Since $1+\Psi_a(t)\le C(1+t^2)$, $H^1$-convergence implies $\|\cdot\|_{\mathcal E_1}$-convergence. The functions $g\chi(\cdot/R)$ lie in $C_c^\infty(0,\infty)$. ∎

**Lemma 3.3 (truncation).** Let $g\in D(\mathcal E)\cap L^\infty$ and let $I=(\alpha,\beta)$ be bounded. Then $\mathbf 1_Ig\in D(\mathcal E)$, and
$$\mathcal E(\mathbf 1_Ig)=\tfrac12\!\iint_{I^2}(g(x)-g(y))^2J+\int_Ig^2\kappa_I,\qquad \kappa_I(x)=\int_{I^c}J(x-y)\,dy\le C+\tfrac12\log_+\tfrac1{x-\alpha}+\tfrac12\log_+\tfrac1{\beta-x}.$$
*Proof.* Split $\mathbb R^2=(I\cup I^c)^2$. The weight $\kappa_I$ is integrable and $g$ is bounded. ∎

Order zero is what makes this work: a jump costs only $\int g^2\log(1/\mathrm{dist})$, which is finite. For $(-\Delta)^\sigma$ with $\sigma\ge\frac12$ it is infinite. The prior-art remark that a jump has infinite log energy is wrong.

**Lemma 3.4 (multipliers and commutator).** Let $\eta\in C^\infty$ with $\eta,\eta'$ bounded, and put $k_\eta(u)=J(u)\min(\|\eta'\|_\infty|u|,2\|\eta\|_\infty)\in L^1$.
- (a) $\eta\phi\in D(\mathcal E)$ for every $\phi\in D(\mathcal E)$.
- (b) $\mathcal E(\eta g,\phi)=\mathcal E(g,\eta\phi)+\langle r_\eta[g],\phi\rangle$, where $r_\eta[g]{(x)}=\int J(x-y)(\eta(x)-\eta(y))g(y)\,dy$ satisfies $|r_\eta[g]|\le k_\eta*|g|$.

*Proof.* Use $(\eta\phi)(x)-(\eta\phi)(y)=\eta(x)(\phi(x)-\phi(y))+\phi(y)(\eta(x)-\eta(y))$. For (b), use the pointwise identity
$$(\eta g(x)-\eta g(y))(\phi(x)-\phi(y))-(g(x)-g(y))(\eta\phi(x)-\eta\phi(y))=(\eta(x)-\eta(y))\big(\phi(x)g(y)-\phi(y)g(x)\big),$$
whose right side is dominated by $k_\eta(x-y)(|\phi(x)g(y)|+|\phi(y)g(x)|)$. Integrate against $\frac12J$ and use symmetry. ∎

**Lemma 3.5 (the bounded part).** Let $f$ be supported in a bounded interval $I''$ of length $\ell''$. Then $\|\mathbf 1_{I''}W_sf\|_p\le M(\ell'')\|f\|_p$ for $1\le p\le\infty$, and $|w_s(f,h)|\le M(\ell'')\|f\|_\infty\|h\|_1$ for $h$ supported in $I''$, where
$$M(\ell''):=|c|+2\sum_{\log n<\ell''}c_n+2|s|\,\ell''\cosh(\ell''/2).$$
*Proof.* A shift by $\log n\ge\ell''$ moves $f$ off $I''$, every shift has norm 1, and on $I''\times I''$ the pole kernel is at most $2\cosh(\ell''/2)$. ∎

Since $W_s$ commutes with translations, $M:=M(2L_{\max}+2)$ bounds $W_s$ for every function and window used below.

**Lemma 3.6 (Dirichlet-form facts).** *Hypothesis:* $J\ge0$ is even and $\Psi_a(t)=\int_{\mathbb R}(1-\cos tu)J(u)\,du$ (Lemma 4.1). The same holds for $(J_{VG},\frac12\log(1+t^2))$. Then:
- (a) For every $f\in L^2(\mathbb R)$, $\ \frac12\iint(f(x)-f(y))^2J(x-y)\,dx\,dy=\frac1{2\pi}\int\Psi_a|F|^2$ in $[0,\infty]$. Hence $D(\mathcal E)$ is the set of $f\in L^2$ for which the left side is finite, because $1+\Psi_a(t)\asymp\log(2+|t|)$ (Lemma 4.3(b)).
- (b) For $f,g\in D(\mathcal E)$, $\mathcal E(f,g)=\frac12\iint(f(x)-f(y))(g(x)-g(y))J(x-y)\,dx\,dy$, absolutely convergent.
- (c) (Normal contractions.) If $T:\mathbb R\to\mathbb R$ has $T(0)=0$ and $|T(a)-T(b)|\le|a-b|$, then for $f\in D(\mathcal E)$: $T\circ f\in D(\mathcal E)$, $\mathcal E(T\circ f)\le\mathcal E(f)$, and $T\circ f=0$ wherever $f=0$. This applies to $f^\pm$ and $|f|$.
- (d) For $F\in D(\mathcal E)$:
$$\mathcal E(F,F^+)=\mathcal E(F^+)+\iint F^+(x)F^-(y)J(x-y)\ge\mathcal E(F^+),\qquad \mathcal E(F,F^-)=-\mathcal E(F^-)-\iint F^+(x)F^-(y)J(x-y)\le-\mathcal E(F^-).$$
- (e) (Disjoint supports.) If $f,g\in D(\mathcal E)$, $fg=0$ a.e. and $\iint|f(x)||g(y)|J(x-y)<\infty$, then $\mathcal E(f,g)=-\iint f(x)g(y)J(x-y)$.

*Proof.*
- (a) By Tonelli and Plancherel, $\|f(\cdot+u)-f\|^2=\frac1{2\pi}\int|e^{-iut}-1|^2|F|^2$ with $|e^{-iut}-1|^2=2(1-\cos ut)$. So the left side is $\frac12\int J(u)\frac1{2\pi}\int2(1-\cos ut)|F(t)|^2dt\,du=\frac1{2\pi}\int\Psi_a|F|^2$.
- (b) Polarise (a). Absolute convergence follows from Cauchy–Schwarz.
- (c) Pointwise $|Tf(x)-Tf(y)|\le|f(x)-f(y)|$; then use (a).
- (d) Since $F^+F^-=0$ pointwise, $(F(x)-F(y))(F^+(x)-F^+(y))=(F^+(x)-F^+(y))^2+F^+(x)F^-(y)+F^+(y)F^-(x)$. Integrate against $\frac12J$ and use the symmetry $x\leftrightarrow y$; the cross term is finite because the other two terms are. The second identity is the same computation with $(F(x)-F(y))(F^-(x)-F^-(y))=-(F^-(x)-F^-(y))^2-F^+(x)F^-(y)-F^+(y)F^-(x)$.
- (e) A.e., $(f(x)-f(y))(g(x)-g(y))=-f(x)g(y)-f(y)g(x)$. Integrate using (b) and the assumed absolute convergence, then use symmetry. ∎

v1 used (a)–(e) without stating them: in Lemma 6.1, Lemma 8.1, Theorem 1 step 6 and Theorem 5.

## 4. The Wiener–Hopf factor and the renewal function

**Lemma 4.1.** $\Psi_a(t)=\varphi(t^2)$, with
$$\varphi(x)=\sum_{k\ge0}\frac{2x}{a_k(a_k^2+x)}=\int_{(0,\infty)}\frac{x}{x+\tau}\,\frac{m_0(d\tau)}{\tau},\qquad m_0=\sum_k2a_k\,\delta_{a_k^2}.$$
Since $\int\min(\tau^{-1},\tau^{-2})m_0(d\tau)<\infty$, $\varphi$ is a complete Bernstein function (CBF) [Kw11, Prop. 2.14; SSV, Thm 6.2]. Also $\Psi_a(t)=\int_{\mathbb R}(1-\cos tu)J(u)\,du$.

*Proof.* Use $\operatorname{Re}\psi(a+iy)-\psi(a)=\sum_n\frac{y^2}{(n+a)((n+a)^2+y^2)}$ with $a=\frac14$, $y=\frac t2$, together with $\int_0^\infty(1-\cos tu)2e^{-a_ku}du=\frac{2t^2}{a_k(a_k^2+t^2)}$. The series and the digamma form agree numerically to $10^{-12}$. ∎

Fix $q>0$ and put $\sigma_q(t):=q+\Psi_a(t)$.

**Lemma 4.2 (factorisation).** For $\xi>0$ put $K(\xi):=\exp\big(\frac1\pi\int_0^\infty\log\sigma_q(\xi\tau)\frac{d\tau}{1+\tau^2}\big)$; this is $(q+\varphi)^\dagger$ in Kwaśnicki's notation.
- (a) $K$ is a CBF [Kw11, Lemma 3.8], and $K(it)K(-it)=\sigma_q(t)$, so $|K(it)|^2=\sigma_q(t)$.
- (b) $K(0+)=\sqrt q$, by dominated convergence.
- (c) $1/K$ is a Stieltjes function with no constant term and no $1/\xi$ term [Kw11, Props 2.17(a), 2.18]. So $1/K(\xi)=\int_0^\infty e^{-\xi x}v(x)\,dx$, where $v=v_q$ is completely monotone, strictly positive and strictly decreasing, with $\int v=q^{-1/2}$.
- (d) $K$ extends continuously to $\operatorname{Re}z\ge0$, and $|K(z)|\le\frac{2e}{e-1}K(|z|)$ there.

*Proof of (d).* Write $K(z)=a+bz+\int(1-e^{-zx})\mu(dx)$ and use $|1-e^{-zx}|\le2\min(1,|z|x)$ and $\min(1,y)\le\frac e{e-1}(1-e^{-y})$. ∎

**Lemma 4.3 (symbol).**
- (a) $0\le t\Psi_a'(t)\le\min(2\Psi_a(t),\,1+2.6/t)$.
- (b) For $t\ge1$: $|\Psi_a(t)-\log t-c_a|\le C/t$, with $c_a=\gamma+\frac\pi2+2\log2\approx3.5343$ [DLMF 5.11.2].

*Proof.*
- (a) $t\Psi_a'=2x\varphi'(x)$ with $x=t^2$.
  - Concavity gives $x\varphi'\le\varphi$.
  - Also $x\varphi'(x)=\sum_kg(a_k)$ with $g(a)=2ax/(a^2+x)^2$. This $g$ is unimodal, with $\int_0^\infty g=1$ and $\max g=\frac9{8\sqrt3}x^{-1/2}$.
  - The nodes $a_k$ are spaced by 2, so $\sum g(a_k)\le\frac12+2\max g$. ∎

**Lemma 4.4.** There are $\xi_0$, $C_K$ and $C_\beta$ such that for $\xi\ge\xi_0$:
- (a) $|\log K(\xi)-\frac12\log\sigma_q(\xi)|\le C_K/\log\xi$;
- (b) $\beta(\xi):=\xi K'(\xi)/K(\xi)$ lies in $[0,1]$ for all $\xi>0$, and $\beta(\xi)\le C_\beta/\log\xi$.

*Proof.*
- (a) We have $\log K(\xi)-\frac12\log\sigma_q(\xi)=\frac1\pi\int_0^\infty\log\frac{\sigma_q(\xi\tau)}{\sigma_q(\xi)}\frac{d\tau}{1+\tau^2}$.
  - For $\tau<\xi^{-1/2}$, the Bernstein property bounds the log by $2|\log\tau|$.
  - For $\tau\ge\xi^{-1/2}$, Lemma 4.3(b) gives $|\log(\sigma_q(\xi\tau)/\sigma_q(\xi))|\le3(|\log\tau|+C\xi^{-1/2})/\log\xi$.
  - $|\log\tau|$ is integrable against $\frac{d\tau}{1+\tau^2}$.
- (b) $\beta(\xi)=\frac1\pi\int_0^\infty h(\xi\tau)\frac{d\tau}{1+\tau^2}$ with $h=t\sigma_q'/\sigma_q\in[0,2]$, and $h(t)\le3.6/\sigma_q(t)$ for $t\ge1$. Split at $\tau=\xi^{-1/2}$. ∎

**Lemma 4.5 (renewal function).** Let $V(x):=\int_0^xv$, so $V$ is increasing, concave, $V(0+)=0$ and $V\le q^{-1/2}$. Then:
- (a) for all $x>0$,
$$\frac1{K(1/x)}\le V(x)\le\frac{1+C_g\,\beta(1/x)}{K(1/x)},\qquad C_g:=\sup_{u>0}\tfrac{(1+u)^2}{u}\big(\tfrac1{1+u}-e^{-u}\big)\le\tfrac83 ;$$
- (b) $|V(x)\ell(x)^{1/2}-1|\le C_V/\ell(x)$ for $0<x\le e^{-1}$.

*Proof.*
- (a) Write $1/K(\xi)=\frac1\pi\int\frac{m(d\tau)}{\xi+\tau}$. Then
$$V(x)-\frac1{K(1/x)}=\frac1\pi\int\frac{m(d\tau)}\tau\Big(\frac1{1+\tau x}-e^{-\tau x}\Big).$$
  - The bracket is $\ge0$, which gives the lower bound.
  - The bracket is also $\le C_g\tau x/(1+\tau x)^2$, and $\frac1\pi\int\frac{x\,m(d\tau)}{(1+\tau x)^2}=\beta(1/x)/K(1/x)$.
- (b) Combine (a) with Lemma 4.4: $K(1/x)=\ell(x)^{1/2}(1+O(\ell^{-1}))$ and $\beta(1/x)=O(\ell^{-1})$. ∎

No Tauberian theorem is needed.

*Pure log.* For $\frac12\log(1+t^2)$ the same lemmas hold with $t\Psi'=t^2/(1+t^2)\le1$.

## 5. Half-line inversion and the edge lemma

*Written out in full in v2, with every hypothesis stated where it is used (final referee, item 4). The specialist check should start with Step 4 of Proposition 5.1.*

**Standing hypotheses of §5.**
- (WH1) $\Psi_a(t)=\varphi(t^2)$, where $\varphi$ is a complete Bernstein function (CBF), $\varphi(0+)=0$, and $\varphi(x)\to\infty$ as $x\to\infty$. *Source:* Lemma 4.1 (CBF), Lemma 4.3(b) ($\varphi(x)=\frac12\log x+c_a+O(x^{-1/2})$).
- (WH2) $q>0$ is fixed. Put $\sigma_q:=q+\Psi_a$ and $\mathcal E_q(f,g):=\mathcal E(f,g)+q\langle f,g\rangle=\frac1{2\pi}\int\sigma_qF\bar G$ on $D(\mathcal E)$.
- All functions are real-valued, so $\overline{\hat\phi(t)}=\hat\phi(-t)$. Convention: $\hat f(t)=\int f(x)e^{ixt}dx$.

**The factor $K:=(q+\varphi)^\dagger$** (Lemma 4.2). What is used, and where each fact comes from:
- (K1) *Definition and CBF property.* $q+\varphi$ is a CBF: CBFs form a convex cone [Kw11, Prop 2.17(b)], and a positive constant is a CBF (the term $c_1$ in [Kw11, (2.23)]). It is positive on $(0,\infty)$, and the integrability condition of [Kw11, Def 3.1] holds, because $\log q\le\log(q+\varphi(\xi))\le\log(q+C+\frac12\log(1+\xi))$. So $K$ is defined by [Kw11, (3.1)–(3.2)], i.e. by the formula of Lemma 4.2, and for $\operatorname{Re}\xi>0$ it is $\exp(\cdots)$, hence nonzero there. By [Kw11, Lemma 3.8], $K$ is a CBF, and $K(\xi)K(-\xi)=(q+\varphi)(-\xi^2)$ for $\xi\in\mathbb C\setminus\mathbb R$.
- (K2) *Factorisation on $i\mathbb R$.* Take $\xi=it$, $t\in\mathbb R\setminus\{0\}$, in (K1): $K(it)K(-it)=\sigma_q(t)$. A CBF is real on $(0,\infty)$, so its holomorphic extension to $\mathbb C\setminus(-\infty,0]$ satisfies $K(\bar z)=\overline{K(z)}$ (Schwarz reflection). Hence $|K(it)|^2=\sigma_q(t)\ge q$.
- (K3) *Boundary continuity and growth.* A CBF is a Bernstein function: $K(z)=a+bz+\int_{(0,\infty)}(1-e^{-zx})\mu(dx)$ with $a,b\ge0$ and $\int\min(1,x)\mu(dx)<\infty$. On $\{\operatorname{Re}z\ge0\}$ we have $|1-e^{-zx}|\le\min(2,|z|x)$, so the right side is continuous there (dominated convergence). It agrees with $K$ on $\{\operatorname{Re}z>0\}$ (both holomorphic, equal on $(0,\infty)$), hence on $i\mathbb R\setminus\{0\}$ by continuity of the holomorphic extension. Moreover $a=K(0+)=\sqrt q$ [Kw11, Prop 3.4(d)], and
$$|K(z)|\le a+b|z|+\max(2,|z|)\textstyle\int\min(1,x)\,\mu(dx)\le C_K(1+|z|)\qquad(\operatorname{Re}z\ge0).$$
  Lemma 4.2(d) and Lemma 4.4 give the sharper bound $|K(z)|=O(\log^{1/2}|z|)$. Linear growth is all that is used below.
- (K4) *The kernel $v$.* $1/K$ is a Stieltjes function [Kw11, Prop 2.17(a)]: $1/K(\xi)=\tilde c_1+\tilde c_2/\xi+\frac1\pi\int_{(0,\infty)}\frac{\tilde m_0(ds)}{\xi+s}$. By [Kw11, Prop 2.18, (2.25)]:
  - $\tilde c_1=\lim_{\xi\to\infty}1/K(\xi)=0$, because $K(\xi)\to\infty$ [Kw11, Prop 3.4(d)] by (WH1);
  - $\tilde c_2=\lim_{\xi\to0+}\xi/K(\xi)=0$, because $K(0+)=\sqrt q>0$ by (WH2).

  Hence, by Tonelli, $1/K(\xi)=\int_0^\infty e^{-\xi x}v(x)\,dx$ for $\xi>0$, with $v(x)=\frac1\pi\int e^{-sx}\tilde m_0(ds)$ completely monotone. Since $\tilde m_0\neq0$, $v>0$ and $v$ is strictly decreasing. By monotone convergence, $\int_0^\infty v=\lim_{\xi\to0+}1/K(\xi)=q^{-1/2}<\infty$.

  **This is where $q>0$ is essential:** for $q=0$ the same computation gives $\int v=\infty$, and Young's inequality below fails.

Extend $v$ by $0$ on $(-\infty,0)$, put $\tilde v(x):=v(-x)$, and let $P_\pm$ be multiplication by $\mathbf 1_{(0,\infty)}$ and $\mathbf 1_{(-\infty,0)}$. For $f\in L^2(0,\infty)$, extended by $0$, define
$$Gf:=v*P_+(\tilde v*f).$$

**Proposition 5.1 (Wiener–Hopf / Silverstein inversion).** Assume (WH1) and (WH2). For every real $f\in L^2(0,\infty)$:
1. $Gf\in D_+$, and $\mathcal E_q(Gf)=\|P_+(\tilde v*f)\|^2\le q^{-1}\|f\|^2$;
2. $\mathcal E_q(Gf,\phi)=\langle f,\phi\rangle$ for every $\phi\in D_+$;
3. $Gf$ is the only $u\in D_+$ with property 2;
4. $Gf(x)=\int_0^\infty G(x,y)f(y)\,dy$ for a.e. $x$, with $G(x,y)=\int_0^{x\wedge y}v(x-z)v(y-z)\,dz\ge0$.

This is Silverstein's half-line Green function [Ber96, Thm VI.20], derived here analytically.

*Proof.*

*Step 1 (transforms).* By (K4), $v\in L^1$. The function $\xi\mapsto\int_0^\infty e^{-\xi x}v(x)\,dx$ is continuous on $\{\operatorname{Re}\xi\ge0\}$ (dominated convergence) and holomorphic inside. The function $1/K$ is also continuous on $\{\operatorname{Re}\xi\ge0\}$: $K$ is continuous there by (K3), and it does not vanish there ($K=\exp(\cdots)$ inside by (K1), $|K(it)|^2\ge q$ by (K2), $K(0)=\sqrt q$). The two functions agree on $(0,\infty)$ by (K4), hence on $\{\operatorname{Re}\xi>0\}$ (identity theorem), hence on $i\mathbb R$ (continuity). With our convention this reads
$$\hat v(t)=1/K(-it),\qquad\hat{\tilde v}(t)=1/K(it).$$

*Step 2 (set-up).* Put $h:=\tilde v*f$. By Young, $\|h\|\le\|v\|_1\|f\|=q^{-1/2}\|f\|$, and $\hat h=\hat f/K(it)$. Put $u:=Gf=v*P_+h$. Both factors vanish on $(-\infty,0)$, so $u$ does, and $\|u\|\le q^{-1}\|f\|$. Also $\hat u=\widehat{P_+h}/K(-it)$. Multiply by $\sigma_q=K(it)K(-it)$ (K2; the point $t=0$ is a null set):
$$\sigma_q\hat u=K(it)\widehat{P_+h}=K(it)\big(\hat h-\widehat{P_-h}\big)=\hat f-K(it)\widehat{P_-h}.\tag{5.1}$$

*Step 3 (energy; item 1).* By (K2), $\sigma_q|\hat u|^2=\sigma_q|\widehat{P_+h}|^2/|K(-it)|^2=|\widehat{P_+h}|^2$. So $\frac1{2\pi}\int\sigma_q|\hat u|^2=\|P_+h\|^2\le\|h\|^2\le q^{-1}\|f\|^2$. Since $1+\Psi_a(t)\asymp\log(2+|t|)$, this gives $u\in D(\mathcal E)$, and with $u=0$ on $(-\infty,0)$, $u\in D_+$.

*Step 4 (the defect vanishes).* Let $\phi\in C_c^\infty(0,\infty)$ be real, with support in $[a_0,b_0]$, $a_0>0$. By (5.1),
$$\mathcal E_q(u,\phi)=\frac1{2\pi}\int\sigma_q\hat u\,\hat\phi(-t)\,dt=\langle f,\phi\rangle-\Delta(\phi),\qquad\Delta(\phi):=\frac1{2\pi}\int K(it)\,\widehat{P_-h}(t)\,\hat\phi(-t)\,dt.$$
All three integrals converge absolutely: the first by Cauchy–Schwarz in $L^2(\sigma_q\,dt)$ (since $u,\phi\in D(\mathcal E)$), the second by Plancherel, hence the third. We show $\Delta(\phi)=0$.
- (i) *Analyticity.* Put $g(t):=K(it)\hat\phi(-t)$. For $\operatorname{Im}t<0$ we have $\operatorname{Re}(it)=-\operatorname{Im}t>0$, so $K(it)$ is holomorphic (K1); $\hat\phi$ is entire. So $g$ is holomorphic on $\{\operatorname{Im}t<0\}$, and continuous on $\{\operatorname{Im}t\le0\}$ by (K3).
- (ii) *Bounds.* For $t=s-iy$ with $y\ge0$, $\hat\phi(-t)=\int\phi(x)e^{-ixs}e^{-xy}dx$, so $|\hat\phi(-t)|\le\|\phi\|_1e^{-a_0y}$. Integrating by parts twice (no boundary terms), $|t|^2|\hat\phi(-t)|\le\|\phi''\|_1e^{-a_0y}$. With (K3), $|g(t)|\le C_\phi(1+|t|)^{-1}$ on $\{\operatorname{Im}t\le0\}$, with $C_\phi$ independent of $y$. Hence $\sup_{y>0}\int|g(s-iy)|^2ds<\infty$.
- (iii) *Paley–Wiener.* Apply [Rud, Thm 19.2] to $G_0(z):=g(-z)$, which is holomorphic on the upper half-plane with uniformly bounded $L^2$ norms on horizontal lines. It gives $b_0\in L^2(0,\infty)$ with $G_0(z)=\int_0^\infty b_0(x)e^{ixz}dx$ for $\operatorname{Im}z>0$. So, for $y>0$, $g(s-iy)=\int_0^\infty b_0(x)e^{-xy}e^{-ixs}dx$. By Plancherel this tends in $L^2(ds)$, as $y\downarrow0$, to $\int_0^\infty b_0(x)e^{-ixs}dx=\hat b(s)$ with $b(x):=b_0(-x)$, which vanishes on $(0,\infty)$. By (i), (ii) and dominated convergence, $g(\cdot-iy)\to g$ in $L^2$ as well. Hence $g=\hat b$ a.e. on $\mathbb R$.
- (iv) *Parseval.* For $F_1,b\in L^2$, $\int\hat F_1\hat b\,dt=2\pi\int F_1(x)b(-x)\,dx$ (Plancherel, using $\hat b=\overline{\widehat{b^*}}$ with $b^*(x):=\overline{b(-x)}$). Take $F_1=P_-h$, which vanishes on $(0,\infty)$; $b(-x)$ vanishes for $x<0$. The integrand vanishes for $x\neq0$, so $\Delta(\phi)=\frac1{2\pi}\int\widehat{P_-h}\,\hat b=0$.

So $\mathcal E_q(u,\phi)=\langle f,\phi\rangle$ for all $\phi\in C_c^\infty(0,\infty)$.

*Step 5 (extension and uniqueness; items 2, 3).* Both sides are continuous in $\phi$ for the norm $\mathcal E_q(\phi)^{1/2}$: the left by Cauchy–Schwarz, the right because $|\langle f,\phi\rangle|\le\|f\|\,q^{-1/2}\mathcal E_q(\phi)^{1/2}$. $C_c^\infty(0,\infty)$ is dense in $D_+$ for this norm (Lemma 3.2(b)). This gives item 2. If $u_1,u_2\in D_+$ both satisfy item 2, then $w=u_1-u_2\in D_+$ and $\mathcal E_q(w,\phi)=0$ for all $\phi\in D_+$; with $\phi=w$, $q\|w\|^2\le\mathcal E_q(w)=0$.

*Step 6 (kernel; item 4).* For $z>0$, $(P_+h)(z)=\int v(y-z)f(y)\,dy$, and $v(y-z)=0$ for $y<z$. So $u(x)=\int_0^xv(x-z)\int_z^\infty v(y-z)f(y)\,dy\,dz$. The same expression with $|f|$ is $G|f|\in L^2$, finite a.e. (Tonelli); Fubini then gives item 4. ∎

**Lemma 5.2 (edge lemma).** Assume (WH1), (WH2), and let $V(x):=\int_0^xv$. Let $f\in L^2(0,\infty)$ be real and bounded on $(0,a)$ for some $a>0$, and let $u=Gf$. Put $k(z)=\int_0^\infty v(t)f(t+z)\,dt$ and $I=k(0)=\int_0^\infty vf$. Then $u(x)=\int_0^xv(x-z)k(z)\,dz$, and for $0<x\le a/2$
$$|u(x)-I\,V(x)|\le V(x)\big[2\|f\|_{L^\infty(0,a)}V(x)+v(a/2)\|f\|_2\sqrt x\big].$$
If $f\in L^\infty(0,\infty)$, then $u$ is uniformly continuous, $u=0$ on $(-\infty,0]$, and $|u-IV|\le2\|f\|_\infty V^2$.

*Proof.*
- *Absolute convergence.* $\int_0^\infty v|f|\le\|f\|_{L^\infty(0,a)}\|v\|_1+\|v\|_{L^2(a,\infty)}\|f\|_2$, and $v\in L^2(a,\infty)$ because $v$ is integrable and bounded by $v(a)$ there. The same bound holds for $k(z)$, $z\le a/2$.
- *Representation.* For $z>0$, $k(z)=(P_+(\tilde v*f))(z)$ (substitute $y=t+z$ in Step 6 above). So $u=v*(P_+k)$, and for $x\le a/2$, $u(x)=\int_0^xv(x-z)k(z)\,dz$, an absolutely convergent integral of a bounded function against $v\in L^1$. This defines the continuous representative of $u$ on $(0,a/2]$.
- *Near part.* $v$ is decreasing and integrable, so $\int_0^\infty|v(y-z)\mathbf 1_{y>z}-v(y)|\,dy=V(z)+\int_z^\infty(v(y-z)-v(y))\,dy=2V(z)$. The part $y<a$ of $|k(z)-I|$ is therefore at most $2\|f\|_{L^\infty(0,a)}V(z)$.
- *Far part.* For $y\ge a\ge2z$, $0\le v(y-z)-v(y)\le v(a/2)$, and $\int_a^\infty(v(y-z)-v(y))\,dy=\int_{a-z}^av\le z\,v(a/2)$. So $\|v(\cdot-z)-v\|_{L^2(a,\infty)}^2\le v(a/2)^2z$, and Cauchy–Schwarz bounds the part $y\ge a$ by $v(a/2)\|f\|_2\sqrt z$.
- *Conclusion.* $u(x)-IV(x)=\int_0^xv(x-z)(k(z)-I)\,dz$. Both bounds on $|k(z)-I|$ increase in $z$, and $\int_0^xv(x-z)\,dz=V(x)$.
- *Bounded $f$.* This is the case $a=\infty$. A convolution of $v\in L^1$ with a bounded function is uniformly continuous, and $u$ vanishes on $(-\infty,0]$ because both factors vanish on $(-\infty,0)$. ∎

Since $\sqrt x\,\ell(x)$ is bounded on $(0,e^{-1}]$, Lemma 4.5(b) gives $\sqrt x\le CV(x)^2$ there, so $u=IV+O(V^2)$ in both cases.

## 6. Boundedness of eigenfunctions

*Written out in full in v2 (final referee, item 4). Step 2 is the direct argument suggested by an internal referee of the Wiener–Hopf write-up; it replaces the Trotter-product and monotone-form-convergence citations of earlier drafts.*

**Standing hypotheses of §6.**
- (B1) $J\ge0$ is even, $\int\min(1,u^2)J(u)\,du<\infty$, and $\Psi_a(t)=\int(1-\cos tu)J(u)\,du$ (Lemma 4.1). So Lemma 3.6 applies.
- (B2) $\Psi_a(t)=\varphi(t^2)$ with $\varphi$ a Bernstein function, $\varphi(0+)=0$, and $\varphi(u)\ge\frac12\log u-C_\varphi$ for $u\ge1$. *Source:* Lemma 4.1, and Lemma 4.3(b), which gives $\Psi_a(t)\ge\log t+c_a-C/t$ for $t\ge1$.
- (B3) $I=(-L,L)$ with $L\le L_{\max}$. $W_L:=\mathbf 1_IW_s\mathbf 1_I$ is a bounded symmetric operator on $L^2(I)$, and $\|W_L\|_{r\to r}\le M$ for $2\le r\le\infty$ (Lemma 3.5, $M=M(2L_{\max}+2)$).
- (B4) $\psi\in D_L$ is real and $(\mathcal E+w_s)(\psi,\phi)=\lambda\langle\psi,\phi\rangle$ for all $\phi\in D_L$, with $|\lambda|\le\Lambda_0$.

**Operators.**
- $\mathcal A$ is the self-adjoint operator of the closed form $\mathcal E$ on $L^2(\mathbb R)$; it is the Fourier multiplier $\Psi_a$.
- $A_D$ is the self-adjoint operator on $L^2(I)$ of the form $\mathcal E|_{D_L}$. This form is closed: form-norm convergence implies $L^2$ convergence, and "$=0$ a.e. off $\bar I$" survives $L^2$ limits. It is densely defined, since $C_c^\infty(I)\subset D_L$.
- Both operators are $\ge0$, because $\mathcal E\ge0$.
- By Kato's first representation theorem [Kat, Thm VI.2.1]: $u\in D(A_D)$ and $A_Du=g$ if and only if $u\in D_L$ and $\mathcal E(u,\phi)=\langle g,\phi\rangle$ for all $\phi\in D_L$. The same holds for $\mathcal A$ with $D(\mathcal E)$ in place of $D_L$.
- $P(t):=e^{-t\mathcal A}$ and $S(t):=e^{-tA_D}$ (spectral calculus).

**Lemma 6.1.** Under (B1)–(B4), $\|\psi\|_\infty\le C_\infty\|\psi\|_2$, where $C_\infty$ depends only on $\Lambda_0$, $M$ and $C_\varphi$.

*Proof.*

*Step 1 (free kernel; uses (B2)).*
- By [SSV, Thm 5.2] there is a convolution semigroup $(\eta_t)_{t>0}$ of sub-probability measures on $[0,\infty)$ with $\int e^{-ur}\eta_t(dr)=e^{-t\varphi(u)}$ for $u\ge0$. They are probability measures because $\varphi(0+)=0$, and $\eta_t(\{0\})=\lim_{u\to\infty}e^{-t\varphi(u)}=0$ because $\varphi\to\infty$.
- Let $g_r(x)=(4\pi r)^{-1/2}e^{-x^2/(4r)}$, so $\hat g_r(\xi)=e^{-r\xi^2}$, and put $p_t:=\int_{(0,\infty)}g_r\,\eta_t(dr)$. Then $p_t\ge0$, $\int p_t=1$, and $\hat p_t(\xi)=\int e^{-r\xi^2}\eta_t(dr)=e^{-t\varphi(\xi^2)}=e^{-t\Psi_a(\xi)}$. So $P(t)g=p_t*g$.
- *$L^m$ norms.* For $1<m\le\infty$ put $\alpha=\frac12(1-\frac1m)\in(0,\frac12]$. Then $\|g_r\|_m=c_mr^{-\alpha}$ with $c_m=(4\pi)^{-\alpha}m^{-1/(2m)}$ ($c_\infty=(4\pi)^{-1/2}$). By Minkowski's integral inequality, $\|p_t\|_m\le c_m\int r^{-\alpha}\eta_t(dr)$.
- Using $r^{-\alpha}=\Gamma(\alpha)^{-1}\int_0^\infty u^{\alpha-1}e^{-ur}du$ and Tonelli,
$$\int r^{-\alpha}\eta_t(dr)=\frac1{\Gamma(\alpha)}\int_0^\infty u^{\alpha-1}e^{-t\varphi(u)}du\le\frac1{\Gamma(\alpha)}\Big[\frac1\alpha+e^{tC_\varphi}\int_1^\infty u^{\alpha-1-t/2}du\Big],$$
  which is finite when $\alpha<t/2$. Hence
$$\|p_t\|_m<\infty\quad\text{whenever}\quad1-\tfrac1m<t.\tag{6.1}$$
- *Resolvent kernel.* For $q>0$, $r_q:=\int_0^\infty e^{-qt}p_t\,dt\ge0$ has $\|r_q\|_1=1/q$ and $\hat r_q=1/(q+\Psi_a)$. So $(\mathcal A+q)^{-1}g=r_q*g$. (Also used in §7, step 5.)

*Step 2 (domination; uses (B1) through Lemma 3.6).* We show: for real $g\in L^2(I)$, extended by $0$,
$$|S(t)g|\le P(t)|g|\quad\text{a.e. on }I.\tag{6.2}$$
- *Resolvent comparison.* Let $q>0$ and $g\ge0$ in $L^2(I)$. Put $u_D:=(A_D+q)^{-1}g$ and $u:=(\mathcal A+q)^{-1}g=r_q*g\ge0$. So $u_D\in D_L$ with $\mathcal E_q(u_D,\phi)=\langle g,\phi\rangle$ for $\phi\in D_L$, and $u\in D(\mathcal E)$ with $\mathcal E_q(u,\phi)=\langle g,\phi\rangle$ for $\phi\in D(\mathcal E)$ (representation theorem).
- *$u_D\ge0$.* By Lemma 3.6(c), $u_D^-\in D(\mathcal E)$ and it vanishes off $\bar I$, so $u_D^-\in D_L$ is an admissible test function. Using Lemma 3.6(d) and $\langle u_D,u_D^-\rangle=-\|u_D^-\|^2$,
$$0\le\langle g,u_D^-\rangle=\mathcal E_q(u_D,u_D^-)\le-\mathcal E(u_D^-)-q\|u_D^-\|^2\le-q\|u_D^-\|^2 .$$
  So $u_D^-=0$.
- *$u_D\le u$.* Put $F:=u_D-u\in D(\mathcal E)$ and $w:=F^+$. By Lemma 3.6(c), $w\in D(\mathcal E)$. Off $\bar I$, $F=-u\le0$, so $w=0$ there, and $w\in D_L$. Testing both equations with $w$ and subtracting gives $\mathcal E_q(F,F^+)=0$. By Lemma 3.6(d), $0=\mathcal E_q(F,F^+)\ge\mathcal E(F^+)+q\|F^+\|^2\ge q\|w\|^2$. So $w=0$, i.e. $0\le u_D\le u$ a.e. on $I$.
- *Iteration.* $R_D:=(A_D+q)^{-1}$ and $R:=(\mathcal A+q)^{-1}$ are positivity preserving (the first by the previous bullet, the second because $r_q\ge0$). By induction, for $g\ge0$ in $L^2(I)$:
$$R_D^ng=R_D(R_D^{n-1}g)\le R_D(\mathbf 1_IR^{n-1}g)\le\mathbf 1_IR(\mathbf 1_IR^{n-1}g)\le\mathbf 1_IR^ng .$$
- *Exponential formula.* Take $q=n/t$. Then $(n/t)^nR_D^n=(1+tA_D/n)^{-n}\to S(t)$ strongly on $L^2(I)$, and $(1+t\mathcal A/n)^{-n}\to P(t)$ strongly on $L^2(\mathbb R)$. This is the spectral theorem with dominated convergence: for $x\ge0$, $0\le(1+tx/n)^{-n}\le1$ and $(1+tx/n)^{-n}\to e^{-tx}$; here $A_D,\mathcal A\ge0$ is used. Passing to a.e.-convergent subsequences gives $0\le S(t)g\le P(t)g$ a.e. on $I$ for $g\ge0$.
- *Real $g$.* Split $g=g^+-g^-$: $|S(t)g|\le S(t)g^++S(t)g^-\le P(t)|g|$. This is (6.2).
- *Consequence.* Let $2\le p\le r\le\infty$ and $1+\frac1r=\frac1m+\frac1p$. For $g\in L^p(I)$ (note $L^p(I)\subset L^2(I)$, since $I$ is bounded), (6.2) and Young give
$$\|S(t)g\|_{L^r(I)}\le\|p_t\|_m\|g\|_{L^p(I)}.\tag{6.3}$$
  With $m=1$: $\|S(t)\|_{r\to r}\le1$.

*Step 3 (Duhamel; uses (B3), (B4)).*
- By (B4), $\mathcal E(\psi,\phi)=\langle\lambda\psi-W_L\psi,\phi\rangle$ for all $\phi\in D_L$, and $\lambda\psi-W_L\psi\in L^2(I)$ by (B3). By the representation theorem, $\psi\in D(A_D)$ and $A_D\psi=\lambda\psi-W_L\psi$.
- For $\psi\in D(A_D)$, $\theta\mapsto S(\theta)\psi$ is $C^1$ from $[0,\infty)$ to $L^2(I)$, with derivative $-S(\theta)A_D\psi$ (spectral theorem). Hence $\frac{d}{d\theta}\big[e^{\theta\lambda}S(\theta)\psi\big]=e^{\theta\lambda}S(\theta)(\lambda\psi-A_D\psi)=e^{\theta\lambda}S(\theta)W_L\psi$. Integrating over $[0,\tau]$ (Riemann integral of a continuous $L^2$-valued function):
$$e^{\tau\lambda}S(\tau)\psi=(I+T_\tau)\psi,\qquad T_\tau g:=\int_0^\tau e^{\theta\lambda}S(\theta)W_Lg\,d\theta.\tag{6.4}$$
- *$L^r$ bound.* Let $2\le r\le\infty$, $g\in L^r(I)$ and $h\in L^2(I)$. By (6.3) with $m=1$ and (B3),
$$|\langle T_\tau g,h\rangle|\le\int_0^\tau e^{\theta|\lambda|}\,|\langle S(\theta)W_Lg,h\rangle|\,d\theta\le\tau e^{\tau\Lambda_0}M\|g\|_r\|h\|_{r^*},\qquad\tfrac1r+\tfrac1{r^*}=1 .$$
  Since $L^2(I)$ is dense in $L^{r^*}(I)$ ($1\le r^*\le2$), $\|T_\tau g\|_r\le\tau e^{\tau\Lambda_0}M\|g\|_r$.
- *Inversion.* Fix $\tau\in(0,1]$ with $\tau e^{\tau\Lambda_0}M\le\frac12$. Then $\sum_k(-T_\tau)^k$ converges in operator norm on each $L^r(I)$, $2\le r\le\infty$, to an inverse of $I+T_\tau$ of norm $\le2$. On $L^r(I)\subset L^2(I)$ the series also converges in $L^2$, since $\|\cdot\|_2\le(2L)^{\frac12-\frac1r}\|\cdot\|_r$. So all these inverses are restrictions of the $L^2$ inverse.

*Step 4 (bootstrap).*
- Put $\kappa:=\tau/2$, $\frac1{p_0}:=\frac12$ and $\frac1{p_{k+1}}:=\max\big(\frac1{p_k}-\kappa,0\big)$. Then $p_K=\infty$ for $K:=\lceil1/\tau\rceil$. Define $m_k$ by $\frac1{m_k}=1-\big(\frac1{p_k}-\frac1{p_{k+1}}\big)$, so $1-\frac1{m_k}\le\kappa<\tau$ and $\|p_\tau\|_{m_k}<\infty$ by (6.1).
- Suppose $\psi\in L^{p_k}(I)$. By (6.3), $e^{\tau\lambda}S(\tau)\psi\in L^{p_{k+1}}(I)$ with norm $\le e^{\tau\Lambda_0}\|p_\tau\|_{m_k}\|\psi\|_{p_k}$. By (6.4) and Step 3, $\psi=(I+T_\tau)^{-1}e^{\tau\lambda}S(\tau)\psi\in L^{p_{k+1}}(I)$, and
$$\|\psi\|_{p_{k+1}}\le2e^{\tau\Lambda_0}\|p_\tau\|_{m_k}\|\psi\|_{p_k}.$$
- After $K$ steps, $\|\psi\|_\infty\le C_\infty\|\psi\|_2$ with $C_\infty:=\prod_{k<K}2e^{\tau\Lambda_0}\|p_\tau\|_{m_k}$. This depends only on $\tau$ (that is, on $\Lambda_0$ and $M$) and on $C_\varphi$. ∎

**Where each hypothesis is used.** (B1): Step 2, through Lemma 3.6. (B2): Step 1. (B3): Step 3. (B4): Steps 3–4. Boundedness of $I$: Step 2 ($L^p(I)\subset L^2(I)$) and Step 3 (consistency of the inverses). Positivity of $J$ is used only in Step 2; neither the primes nor the pole need any sign, because they enter only through $W_L$ in Step 3.

*Pure log.*
- (B1) holds with $J_{VG}(u)=e^{-|u|}/(2|u|)$.
- (B2) holds with $\varphi_{VG}(u)=\frac12\log(1+u)$ (gamma subordinator, $e^{-t\varphi_{VG}(u)}=(1+u)^{-t/2}$).
- (B3) holds with $W_L$ replaced by $f\mapsto-\mathbf 1_I(k*f)$. On $L^r(I)$ its norm is at most $\int_{-2L}^{2L}k\le2L$, because $0<k\le\frac12$. This needs the bounded window (§1).

## 7. Proof of Theorem 1

Fix one even $\chi\in C_c^\infty(\mathbb R)$ with $0\le\chi\le1$, $\chi=1$ on $[-\rho_0,\rho_0]$ and $\operatorname{supp}\chi\subset[-2\rho_0,2\rho_0]$. Use it for every $L\in[L_{\min},L_{\max}]$. Take $q=1$.

1. **Boundedness.** Lemma 6.1.
2. **Localisation.** $\tilde\psi=\psi(L-\cdot)$ is an eigenfunction on $D_{(0,2L)}$, by translation and reflection invariance. For $\phi\in D_+$ we have $\chi\phi\in D_{(0,2L)}$ (Lemma 3.4(a)), so $\mathcal E(\tilde\psi,\chi\phi)=\langle\lambda\tilde\psi-W_s\tilde\psi,\chi\phi\rangle$.
3. **Commutator.** By Lemma 3.4(b), $u:=\chi\tilde\psi\in D_+$ satisfies $\mathcal E_q(u,\phi)=\langle f_+,\phi\rangle$ for all $\phi\in D_+$, where
$$f_+=\mathbf 1_{(0,\infty)}\big[\chi\big((q+\lambda)\tilde\psi-W_s\tilde\psi\big)+r_\chi[\tilde\psi]\big].$$
   We have $f_+\in L^2\cap L^\infty$ with $\|f_+\|_\infty\le(q+\Lambda_0+M+\|k_\chi\|_1)C_\infty$. By uniqueness in Proposition 5.1, $u=Gf_+$.
4. **Edge expansion.** Lemma 5.2 gives $|\tilde\psi-A_+V|\le2\|f_+\|_\infty V^2$ on $(0,\rho_0]$, with $A_+=\int v f_+$. Lemma 4.5(b) converts this to the $\ell^{-1/2}$ form with error $O(\ell^{-1/2})$ after multiplying by $\ell^{1/2}$. Continuity near the edge and $\psi(L-)=0$ follow from Lemma 5.2.
5. **Interior continuity.** Take $\chi_1\in C_c^\infty(-L,L)$. Then $\chi_1\psi=r_q*f_1$ with $f_1\in L^\infty$ and $r_q=\int_0^\infty e^{-qt}p_t\,dt\in L^1$. A convolution of $L^1$ with $L^\infty$ is uniformly continuous.
6. **Explicit formula (item 3).** Fix $q>0$ and $\phi\in C_c^\infty(0,\infty)$, and split $\phi=\mathbf 1_{(0,2L)}\phi+\mathbf 1_{(2L,\infty)}\phi$ (Lemma 3.3).
   - The first piece lies in $D_{(0,2L)}$, so the eigen-equation applies.
   - The second piece has support disjoint from $\tilde\psi$, so $\mathcal E(\tilde\psi,\mathbf 1_{(2L,\infty)}\phi)=-\int\mu\phi$, absolutely convergent.
   - $\mu=O(\log_+\frac1{y-2L})$ near $2L$ and $O(e^{-y/2})$ at infinity, so $f_q\in L^2$ and $f_q$ is bounded on $(0,L)$.
   - Hence $\tilde\psi=G_qf_q$, and Lemma 5.2 (with $a=L$) together with $V_q\ell^{1/2}\to1$ for every $q$ gives $A_+=\int v_qf_q$. ∎

The primes and the pole enter only through $W_s\tilde\psi\in L^\infty$. That is why no arithmetic condition on $L$ appears.

## 8. The cross identity and the proof of Theorem 2

For $\psi$ supported in $\bar I$ and $y\notin\bar I$, write $(J\psi)(y)=\int_IJ(y-x)\psi(x)\,dx$.

**Lemma 8.1 (cross identity, exact).** Let $I,I'$ be bounded intervals, and let $\psi\in D_I\cap L^\infty$ and $\psi'\in D_{I'}\cap L^\infty$ be eigenfunctions of $\mathcal E+w_s$ on $D_I$ and $D_{I'}$ with eigenvalues $\mu,\mu'$. Then
$$(\mu-\mu')\langle\psi,\psi'\rangle=\int_{I^c}(J\psi)\psi'-\int_{I'^c}(J\psi')\psi-w_s(\psi,\mathbf 1_{I^c}\psi')+w_s(\psi',\mathbf 1_{I'^c}\psi).$$
For nested windows $I_L\subset I_{L'}$ this becomes
$$(\lambda(L')-\lambda(L))\langle\psi_L,\psi_{L'}\rangle=-\int_{L<|y|<L'}(J\psi_L)\psi_{L'}+w_s(\psi_L,\mathbf 1_{I_L^c}\psi_{L'}).$$
*Proof.*
- Split $\psi'=\mathbf 1_I\psi'+\mathbf 1_{I^c}\psi'$ (Lemma 3.3).
- Test the equation for $\psi$ with $\mathbf 1_I\psi'\in D_I$.
- Use $\mathcal E(\psi,\mathbf 1_{I^c}\psi')=-\int_{I^c}(J\psi)\psi'$ (disjoint supports; absolutely convergent since $\iint_{[0,1]^2}\frac{ds\,dt}{s+t}<\infty$).
- Do the same with the roles exchanged and subtract. ∎

This is the order-zero, continuum analogue of Krein's resolvent-derivative identity [Den, Lemma 2.3] and of the finite-$N$ commutator identities [CCM, Lemma 5.2], [CvS, Lemma 5.1]. Prime terms that activate between $L$ and $L'$ need no special treatment: they are part of $w_s$.

**Lemma 8.2 (exterior field).** Let $\psi$ be as in Theorem 1, and let $K_\psi$ bound its constants. For $0<\eta\le\rho_0$,
$$(J\psi)(L+\eta)=A_+m(\eta)+R(\eta),\qquad m(\eta)=\int_0^{\rho_0}J(\eta+r)V(r)\,dr,$$
with $|m(\eta)-\ell(\eta)^{1/2}|\le C$ and $|R(\eta)|\le CK_\psi(1+\log\ell(\eta))$.

*Proof.*
- Write $\tilde\psi=A_+V+e$ on $(0,\rho_0]$ with $|e|\le C\ell^{-1}$.
- Use $J(u)\le\frac1{2u}+C$ for $u\le1$, and $\int_\eta^{\rho_0}\frac{dr}{r\ell(r)}=\log\ell(\eta)-\log\ell(\rho_0)$; this bounds the contribution of $e$.
- For $m$: $\int_\eta^{\rho_0}\frac{\ell(r)^{-1/2}}{2r}dr=\ell(\eta)^{1/2}-\ell(\rho_0)^{1/2}$, and $V=\ell^{-1/2}(1+O(\ell^{-1}))$. ∎

The coefficient 1 in $m\sim\ell^{1/2}$ comes from $J\sim\frac1{2u}$ against $V\sim\ell^{-1/2}$, since $\frac12\cdot2=1$.

**Lemma 8.3 (layer integral).** Let $\psi_1,\psi_2$ be as in Theorem 1 for windows $L_1<L_2=L_1+\delta$, $\delta\le\rho_0$, with constants and traces bounded by $K$. Then
$$\Big|\int_0^\delta(J\psi_1)(L_1+\eta)\,\psi_2(L_1+\eta)\,d\eta-A_+^{(1)}A_+^{(2)}\delta\Big|\le CK^2\delta(1+\log\ell(\delta))\ell(\delta)^{-1/2}.$$
*Proof.*
- $\psi_2(L_1+\eta)=A_+^{(2)}V(\delta-\eta)+O(V^2)$. Insert Lemma 8.2.
- The main integral is $\delta\int_0^1m(\delta t)V(\delta(1-t))\,dt=\delta\big(1+O(\ell(\delta)^{-1/2})\big)$. This uses $\ell(\delta t)=\ell(\delta)+\ell(t)$, $\int_0^1\ell=1$, and $\big(\frac{\ell(\delta)+\ell(t)}{\ell(\delta)+\ell(1-t)}\big)^{1/2}=1+O(\frac{\ell(t)+\ell(1-t)}{\ell(\delta)})$.
- The error terms are bounded with $\int_0^\delta(1+\log\ell(\eta))\,d\eta\le C\delta(1+\log\ell(\delta))$. ∎

The same holds at $-L$ by reflection. It also holds for translated windows, where each endpoint has the same geometry: one window edge, and the other window's edge at distance $h$.

**Lemma 8.4 (continuity in $L$).** Fix a sector and an index.
1. $\lambda^\sigma_j(L)$ is non-increasing and continuous, and bounded below by $-M$.
2. If $\lambda^\sigma_k(L_0)$ is sector-simple, there is an interval $N\ni L_0$ on which:
   - it stays simple;
   - $|\langle\psi_L,\psi_{L_0}\rangle|\ge\frac12$;
   - with the sign fixed by $\langle\psi_L,\psi_{L_0}\rangle>0$, the map $L\mapsto\psi_L$ is $L^2$-continuous;
   - the constants of Theorem 1 are uniform, and $A_\pm(L)$ is continuous.

*Proof.*
- **Monotonicity.** $D_L\subset D_{L'}$ with the same form, so min-max gives it.
- **Left continuity.** Dilation, using Lemma 3.2(c).
- **Right continuity.** Kolmogorov–Riesz precompactness of form-bounded families supported in $[-R,R]$ (tails $\int_{|t|>T}|F|^2\le C/\log T$), together with lower semicontinuity of $\mathcal E$ and $L^2$-continuity of $w_s$.
- **Eigenvector convergence.** Test with $\phi\in D_{L_1}$, $L_1<L_0$, and use density and simplicity.
- **Continuity of $A_\pm$.** $A_+(L)=\int vf_{+,L}$ and
$$\Big|\int v(f_{+,L}-f_{+,L_1})\Big|\le2\sup_N\|f_+\|_\infty V(\varepsilon)+\|v\mathbf 1_{(\varepsilon,\infty)}\|_2\|f_{+,L}-f_{+,L_1}\|_2 ,$$
  where $f_{+,L}\to f_{+,L_1}$ in $L^2$. ∎

**Proof of Theorem 2.** Apply the nested identity of Lemma 8.1 with $\psi_{L_1},\psi_{L_2}$.
- The layers $(L_1,L_2)$ and $(-L_2,-L_1)$ give $\sum_\pm A_\pm^{(1)}A_\pm^{(2)}\delta$ up to the error of Lemma 8.3.
- The $w_s$-term is at most $M\,C_\infty\cdot2\delta\cdot2KV(\delta)=O(\delta\ell(\delta)^{-1/2})$, by Lemma 3.5.
- Divide by $\delta\langle\psi_{L_1},\psi_{L_2}\rangle$, which is $\ge\frac12$ and tends to 1. Then let $L_1,L_2\to L$ and use the continuity of $A_\pm$.
- So $\lambda$ is strictly differentiable on $N$ with continuous derivative $-(A_+^2+A_-^2)$. For parity states $A_-^2=A_+^2$. ∎

**The constant 2.** It is one $A^2$ per endpoint. In the renewal normalisation each endpoint contributes exactly $(\lim\psi/V)^2$, which is the 1-D Djitte–Fall–Weth formula $\Gamma(1+\sigma)^2(u/\delta^\sigma)^2=(u/V_\sigma)^2$ [DFW21] at order zero. No $\sqrt2$ appears, because no fractional regularisation is used; compare the PL-310 conversion $\tau_s/\sqrt s\to\sqrt2\,C$. The constant is fixed analytically by Lemmas 8.2–8.3. **Theorem 4 does not confirm it independently** (v1 said it did): its proof uses Lemma 8.3, and with a layer constant $\kappa A^2$ in place of $A^2$ it would give $A^2=1/(2\kappa L)$ alongside the exact $\lambda'=-1/L$. Which numerical checks do test the constant is said in §13.1.

**Virial form.** The fixed-$L$ "Pohozaev = virial" version is the renormalised virial limit
$$\mathcal V(\psi)=\lim_{\rho\downarrow1}\frac{(K^{(\rho)}-K)(\psi_{1/\rho},\psi)}{\rho-1}=1-L(A_+^2+A_-^2)$$
(internal Pohozaev-direct write-up, Prop. G; not included). With prime atoms, the Fourier virial $\langle F,t\Psi_L'F\rangle$ is not absolutely convergent. That is why the cross identity, not the virial, is the working tool.

## 9. Proof of Theorem 3

Apply Lemma 8.1 with $I=I_L$, $\psi=\psi_1$, $I'=I_L+h$ and $\psi'=\tau_h\psi_2$; the latter is an eigenfunction on $D_{I'}$ by translation invariance.
- $I^c\cap I'=(L,L+h)$ gives $A_+^{(1)}A_+^{(2)}h$.
- $I'^c\cap I=(-L,-L+h)$ gives $A_-^{(1)}A_-^{(2)}h$.
- The $w_s$-terms are $O(hV(h))$.

Consequences:
- (a) Take $\psi_1=\psi_2$; the left side vanishes.
- (b) Within $E_\lambda$ the left side vanishes, so the image of the trace map is totally isotropic for the form $aa'-bb'$. That form has signature $(1,1)$, so the image has dimension $\le1$.
- (c) For parity states $A_+^{(e)}A_+^{(o)}-A_-^{(e)}A_-^{(o)}=2A_eA_o$, and $\langle\psi_e,\tau_h\psi_o\rangle=\Phi(h)$.
- (d) Immediate from (c).
- (e) Combine (c) with Theorem 2. ∎

## 10. Proof of Theorem 4 (pure log symbol)

Theorems 1–3 hold with the replacements of §1. Now let $\psi$ be any eigenfunction on $I=(-L,L)$ with eigenvalue $\lambda$.

*Construction.* For $\theta>1$, dilate about the left endpoint: $\psi_\theta(x):=\psi(-L+(x+L)/\theta)$, supported on $I'=(-L,-L+2L\theta)\supset I$. By exact dilation covariance,
$$Q^{\log}(f(\cdot/\theta))=\theta\big[Q^{\log}(f)-\log\theta\,\|f\|^2\big],$$
together with translation invariance, $\psi_\theta$ is an eigenfunction on $D_{I'}$ with eigenvalue $\lambda-\log\theta$.

*The identity.* Lemma 8.1 applies, with only the right layer $(L,L+\delta)$, $\delta=2L(\theta-1)$, present:
$$\log\theta\,\langle\psi,\psi_\theta\rangle=\int_L^{L+\delta}(J_{VG}\psi)\psi_\theta-w_{\log}(\psi,\mathbf 1_{I^c}\psi_\theta).$$
- $\psi_\theta(L+\delta-r)=\psi(L-r/\theta)$, so $\psi_\theta$ has trace $A_+(\psi)$ and uniform constants. The difference $V(r)-V(r/\theta)$ is at most $(\theta-1)V(r)$, by concavity.
- Lemma 8.3 gives a right side of $A_+(\psi)^2\delta(1+o(1))$.
- $\langle\psi,\psi_\theta\rangle\to1$ and $\log\theta=\frac\delta{2L}(1+o(1))$.

Hence $A_+^2=\frac1{2L}$. Dilating about the right endpoint gives $A_-^2=\frac1{2L}$.

*Simplicity.* $\psi\mapsto A_+(\psi)$ is linear on $E_\lambda$ and does not vanish on any unit vector. A nonzero linear functional on a space of dimension $\ge2$ has a nontrivial kernel, so $\dim E_\lambda=1$.

*Hadamard.* Then $\lambda_k'=-1/L$, consistent with exact scaling. ∎

This mechanism is the order-zero analogue of Kwaśnicki's one-page proof of simplicity for $(-\Delta)^\sigma$ on an interval [Kw23]; see also [FGMP23]. We found the log-Laplacian statement nowhere in the literature (§14.3); absence in a search is not proof of novelty.

## 11. Proof of Theorem 5

*Global representation.* Theorem 1(3) holds for every $q>0$, and $v_q$ is positive and strictly decreasing.

**(a) $s\le0$.**
- *Positive eigenfunctions have $A_+>0$.* Let $\psi\ge0$, $\psi\not\equiv0$, be an eigenfunction. On $(0,2L)$,
$$-W_s\tilde\psi=-c\tilde\psi-2s\!\int\!\cosh\tfrac{\cdot-y}2\,\tilde\psi(y)\,dy+\sum_nc_n(\text{shifts of }\tilde\psi)\ \ge\ -c\tilde\psi ,$$
  and $\mu\ge0$. For $q\ge c-\lambda$,
$$A_+\ \ge\ v_q(2L)\Big[(q+\lambda-c)\!\int\psi-\int_0^{2L}\tilde\psi\,\kappa\Big],\qquad\kappa(r)=\int_{2L-r}^\infty J,$$
  where $\int\tilde\psi\kappa\le C_\infty\int_0^{2L}\kappa<\infty$ does not depend on $q$. Taking $q$ large gives $A_+>0$; reflection gives $A_->0$.
- *The ground state.* For $f\in D_L$:
  - $\mathcal E(f)-\mathcal E(|f|)=4\iint J(x-y)f^+(x)f^-(y)\,dx\,dy$;
  - the shift terms satisfy $-2c_n\int|f||f(\cdot-\log n)|\le-2c_n\int f\,f(\cdot-\log n)$;
  - for $s\le0$ the pole term does not increase either.

  So $|f|$ is a minimiser whenever $f$ is. Because $J>0$ everywhere, equality forces $f$ to have one sign. Then $f\mapsto\int f$ is nonzero on every nonzero minimiser, so $\lambda_0$ is simple. Its eigenfunction is $\ge0$, and it is even because its reflection is also a ground state.
- *Conclusion.* By Theorem 2 at every $L$, $\lambda_0'=-2A^2<0$.

**(b) $2L\le\log2$, $s\ge0$.** No prime term acts on $D_L$.
- *Positive odd eigenfunctions have $A_+>0$.* Let $\psi$ be odd with $\psi\ge0$ on $(0,L)$ and $\psi\not\equiv0$. Then $\tilde\psi(2L-r)=-\tilde\psi(r)$, and on odd functions the pole acts as $-2sS'\sinh\frac x2$ with $S'=2\int_0^L\sinh\frac y2\,\psi\ge0$. Pairing $r$ with $2L-r$:
  - $\int_0^{2L}v_q\tilde\psi=\int_0^L(v_q(r)-v_q(2L-r))\tilde\psi(r)\,dr>0$;
  - the pole contributes $2sS'\int_0^L(v_q(r)-v_q(2L-r))\sinh\frac{L-r}2\,dr\ge0$;
  - $\mu(y)=\int_0^L\big(J(y-r)-J(y-2L+r)\big)\tilde\psi(r)\,dr\le0$ for $y>2L$.

  So $A_+>0$ for any $q>c-\lambda$.
- *The odd ground state.* For odd $f$ put $f^\sharp=\operatorname{sign}(x)|f(x)|$. With $a=f(x)$, $b=f(y)$, $J_\mp=J(x\mp y)$, $x,y>0$,
$$\mathcal E(f)=\iint_{x,y>0}\big[(a^2+b^2)(J_-+J_+)-2ab(J_--J_+)\big],\qquad J_->J_+ .$$
  - So $\mathcal E(f)-\mathcal E(f^\sharp)=2\iint(|ab|-ab)(J_--J_+)\ge0$, with equality only if $ab\ge0$ a.e.
  - The pole $-2s(\int f\sinh\frac x2)^2$ does not increase under $f\mapsto f^\sharp$.
  - Hence odd minimisers have one sign on $(0,L)$, and $f\mapsto\int_0^Lf$ separates them, which gives simplicity.

**(c)** By Theorem 3(d), $A_eA_o=0$ at the common level, and $A_o\ne0$ by (b).

**(d)** Let $s=1$, and let $U$ be an open interval on which the lowest eigenvalue $\lambda_{\min}(L)$ of $A^{(1)}_L$ is simple with an even eigenfunction.
- *Strict monotonicity (every $L$, no hypothesis).* Suppose $\lambda_{\min}(L)=\lambda_{\min}(L')$ with $L<L'$, and let $\psi$ be a minimiser at $L$.
  - For $|h|\le L'-L$, $\tau_h\psi\in D_{L'}$ and $Q^{(1)}(\tau_h\psi)=Q^{(1)}(\psi)$ (Lemma 3.1). So every such translate is a minimiser at $L'$, and lies in the eigenspace of $\lambda_{\min}(L')$, which is finite-dimensional (compact resolvent).
  - But the functions $e^{iht}F(t)$, for distinct $h$, are linearly independent: $F$ is entire and not identically zero, so a vanishing finite combination $\sum c_je^{ih_jt}F(t)$ forces $\sum c_je^{ih_jt}=0$ off the discrete zero set of $F$, hence everywhere, hence $c_j=0$. Infinitely many independent vectors in a finite-dimensional space is a contradiction.
  - So $\lambda_{\min}$ is strictly decreasing on $(0,\infty)$.
- *$C^1$ on $U$.* For $L_0\in U$, $\lambda_{\min}=\lambda^e_0$ near $L_0$ and it is simple in the even sector, so Theorem 2 applies: $\lambda_{\min}$ is $C^1$ near $L_0$ with $\lambda_{\min}'=-2A_e^2$. The function $A_e^2=-\lambda_{\min}'/2$ does not depend on the sign convention for $\psi_e$ and is continuous on $U$. So $Z:=\{L\in U:A_e(L)=0\}$ is relatively closed in $U$.
- *Empty interior.* If $Z$ contained an open interval $J$, then $\lambda_{\min}'=0$ on $J$, so $\lambda_{\min}$ would be constant on $J$. This contradicts strict monotonicity. ∎
- *The input [GS].* [GS, §3, Theorem] certifies: for every $L\in(0,1.19]$, the lowest eigenvalue of Weil's quadratic form on $L^2(-L,L)$, with pole terms and all prime powers $\log n<2L$, is simple with an even eigenfunction. Its form is that of [GS, §2], which is $Q^{(1)}_L$ by Lemma 3.1; the final referee checked the position-side formula against the P0 matrix to $10^{-16}$. So $U=(0,1.19)$ qualifies, conditional on [GS] (computer-assisted, unrefereed).
- *Remark.* By Lemma 8.4(1) every $\lambda^\sigma_j(L)$ is continuous in $L$. So the strict inequalities $\lambda^e_0<\lambda^e_1$ and $\lambda^e_0<\lambda^o_0$ persist near any point where they hold, and the set of $L$ with a simple even ground state is open. [GS] therefore gives an open set containing $(0,1.19]$. We state the open interval $(0,1.19)$, as the referee asked.

*What stops $s=1$ in the even sector.* The pole kernel $+2\cosh$ has the wrong sign for Beurling–Deny, so neither the $|f|$ step nor the large-$q$ bound works. Numerically the true even ground state stays positive, but $A_e$ is small: $A_e\approx0.062$ at $L=0.4$ and $2.4\cdot10^{-4}$ at $L=0.6$. See §15 for why this is not a pure analysis question.

## 12. What the proof uses, and what is conditional

Everything above is proved here, except the following standard results. Referees checked items 1, 2 and 4 against the source texts.
1. **Kwaśnicki 2011** [Kw11]:
   - Lemma 3.8: the Wiener–Hopf factor $\psi^\dagger$ of a CBF is a CBF, and $\psi^\dagger(\xi)\psi^\dagger(-\xi)=\psi(-\xi^2)$;
   - Props 2.14, 2.17(a) and 2.18: CBF $\leftrightarrow$ Stieltjes, and the representation constants.
2. **Paley–Wiener** for $H^2$ of a half-plane [Rud, Thm 19.2].
3. **Kato's first representation theorem** for closed semibounded forms [Kat, Thm VI.2.1], the spectral theorem, and the existence of the convolution semigroup (subordinator) of a Bernstein function [SSV, Thm 5.2]. (v1 cited Pazy for the exponential formula and Duhamel's formula. §6 now derives both from the spectral theorem, so [Paz] is no longer needed.)
4. **Digamma asymptotics** [DLMF 5.11.2].
5. **The Kolmogorov–Riesz compactness criterion.**
6. **For Theorem 5(d) on $(0,1.19)$ only:** the project's computer-assisted simple-even theorem [GS] (unrefereed). It is an input, not a standard result.

The Trotter-product and monotone-form-convergence citations of earlier drafts are no longer used. An internal referee noted that Kato's version needs a densely defined limit form; Step 2 of Lemma 6.1 avoids the issue.

**Other refereed write-ups: closely related, not independent.** Three further internal write-ups prove the same theorems: a probabilistic one, a Pohozaev-direct one and a Krein–Sakhnovich one. Each went through an attempt, a referee, a repair and a second referee (all AI), and every verdict was "correct with minor gaps". v1 called these "four independent routes". That overstated it:
- all four share the cross-identity / Silverstein mechanism (the probabilistic write-up uses Silverstein's formula [Ber96, VI.20], [GR12, Lemma 4.3] in place of Proposition 5.1);
- all their numerics ran on the same hp-FEM solver of [BC], whose constant-term bug is recorded in §13.

The honest description is **four internally refereed write-ups of closely related arguments**. Before the final referee's report, no fully independent numerical implementation existed; the final referee's P0 code is the first (§13.1).

The other write-ups rely on more citations: FOT §4.4, and Karamata or KMR Prop 4.3. They give the $q=0$ explicit formula $A_+=\int_0^\infty V_0'(b)\,g(L-b)\,db$, where $V_0$ is the renewal function of the Lévy process with exponent $\Psi_a$. The Wiener–Hopf argument above is the one with the fewest external inputs. The other write-ups are not included here.

**Hypotheses actually used.**
- (E): none.
- (H): simplicity in the parity sector at $L_0$.
- "$e^{2L}$ not a prime power" is never used.

**Open.**
1. $A_e(L)\ne0$ at a given $L$ for the even ground state of the true form ($s=1$). Equivalently $\lambda_e'(L)\ne0$.
2. $A_o\ne0$ once $2L>\log2$; the primes break the odd Beurling–Deny property.
3. Edge asymptotics of $\psi'$, and $\psi\in BV$ or $W^{1,1}$.
4. The sharp remainder. Numerically $\psi=AV(1+\kappa_\lambda/\ell+\dots)$, an absolute $O(V^3)$; only $O(V^2)$ is proved.
5. The kink law and the tail law themselves (§15).

## 13. Numerical confirmation

N1–N10 are uncertified double-precision runs with the hp-FEM solver of [BC] (graded discontinuous Legendre elements, $p=8$–$10$, mesh down to $10^{-14}$), made by the internal write-ups and their referees. The solver and the raw outputs are not included here.
- **What they test.** The fit-free checks (N1–N5) test the exact identities. They are **blind to the constant 2** of (H) (§13.1). N7 tests the explicit formula of Theorem 1(3). The constant is tested only by absolute amplitudes: N9 here, and, independently, the final referee's code in §13.1.
- **Fitted amplitudes.** They carry about 1% model uncertainty, because the fit basis matters. When primes are active, they also carry a 0.2–1% resolution bias unless the mesh is graded at the prime images $\pm(L-\log n)$ (§13.1). This applies to N5 and N9 at $L\ge0.4$.

- **N1. Exact cross identity, nested windows**. Seven cases, all with primes, pole off or at true strength, both sectors, $L=0.4\to0.405,0.42$ and $0.6\to0.61$. Left side equals right side to relative $2$–$3.5\cdot10^{-8}$. The two solves use different meshes, so this agreement is not Galerkin-automatic; it rules out a missing point term.
- **N2. Exact cross identity, translated windows**. Four cases, $h=10^{-2}$ to $10^{-6}$, relative error $\le7.3\cdot10^{-8}$.
  - The $w$-terms are not small at accessible $h$: $w$-part$/h$ ranges from $-0.54$ to $+0.03$. They cancel a matching $\ell^{-1/2}$ drift of the $J$-part. Any numerical test that drops primes and pole at finite $h$ is off by 15–55%.
- **N3. Edge-free identity** $X^2/(\lambda_e'\lambda_o')$, with $X=(\lambda_e-\lambda_o)\Phi'(0)$ (Theorem 3(e), no fitted $A$; blind to the constant):

  | $L$ | $s$ | ratio |
  |---|---|---|
  | 0.4 | 0 | 0.99973 |
  | 0.4 | 1 | 0.99801 |
  | 0.6 | 0 | 1.00064 |
  | 0.3 | 1 | 0.99956 |

  The Krein–Sakhnovich write-up's $s=0$, $L=0.4$ run, Richardson-extrapolated in $h$, gives $0.707498$–$0.707521$ against $\sqrt{\lambda_e'\lambda_o'}/2=0.707537$.
- **N4. Pure log** ($L=0.5$ and $L=1$ runs). $L(\lambda_e-\lambda_o)\langle u_o,u_e'\rangle=\pm1.00000$ to $\pm1.00061$ for all 9 even/odd pairs, as Theorem 4 predicts ($|A_eA_o|=\frac1{2L}$), with no fitting. This tests the mixed identity and Theorem 4 *jointly*; it is blind to the constant, since a layer constant $\kappa$ would change both sides in the same way. All eigenvalues are distinct, consistent with simplicity. The hp-FEM pure-log model drops the $L$-dependent constant $\log(2L)+\gamma$, so its printed eigenvalues at $L=0.5$ and $L=1$ coincide to all digits. That is exactly what dilation covariance predicts.
- **N5. Sector ratio** ($V$ cancels): $(A_o/A_e)^2$ against $\lambda_o'/\lambda_e'$. Blind to the constant. At $L\ge0.4$, read with the extra prime-image resolution uncertainty of §13.1.

  | $L$ | $s$ | $(A_o/A_e)^2$ | $\lambda_o'/\lambda_e'$ | source |
  |---|---|---|---|---|
  | 0.4 | 0 | 0.082675 | 0.082587 | Wiener–Hopf write-up (referee run) |
  | 0.6 | 0 | 0.027850 | 0.027777 | Wiener–Hopf write-up (referee run) |
  | 0.4 | 1 | 0.016496–0.016539 | 0.016505 | probabilistic write-up (referee run) |
  | 0.6 | 1 | 0.002777–0.002794 | 0.002781 | probabilistic write-up |

- **N6. Through a prime activation**. At $L_0=\frac12\log2$, $s=0$, for $h=10^{-3}$ to $10^{-7}$:
  - the left slope tends to $-2A^2$: $-3.3415$ against $-3.3471$ (even);
  - the right slope approaches the same value with gap$\cdot\ell(2h)\approx$ const: $-3.5$ (even) and $+3.0$ (odd), against the predicted $-4c_2A_+A_-$, i.e. $-3.28$ (even) and $+2.87$ (odd). This prediction comes from the activation term $-2c_2g(\log2)\approx-4c_2A_+A_-h/\ell(2h)$, which is $o(h)$.

  So $\lambda$ is $C^1$ across the activation (Theorem 2). The logarithmic modulus is a numerical observation, not proved. The mechanism, the contribution of order $\delta/\log(1/\delta)$ of the newly born channel, was analysed in mathia PL-338 (§14.2).
- **N7. Explicit formula**. This checks the $q=0$ explicit-formula machinery and the normalisation of $V_0$. It tests Theorem 1(3), not the constant of (H). For the torsion function of the archimedean part, the flux identity holds to 8 digits, and the explicit trace $A_{\rm pred}=0.57290615$ ($L=0.4$) matches the edge fit to $(1$–$3)\cdot10^{-5}$.
- **N8. Rates** (Wiener–Hopf write-up and referee reruns).
  - $1\le VK(1/x)\le1+C_g\beta(1/x)$ holds at all test points, and $(V\ell^{1/2}-1)\ell$ stays bounded.
  - Numerically $V_q\approx(\ell+q+c_a-\gamma)^{-1/2}$. The constant that $(V\ell^{1/2}-1)\ell$ approaches is $(\gamma-c_1)/2$, not $-c_1/2$, as an internal referee corrected.
- **N9. Hadamard ratios with fitted $A$**, which carry about 1% model uncertainty (referee runs, excited states $k=0,1$, both sectors, $s=0,1$). These are absolute checks of the constant, from the project's own solver. At $L\ge0.4$ add the prime-image resolution uncertainty of §13.1.
  - $-\lambda'/(2A^2)\in[0.9987,1.0024]$ at $L=0.36,0.4,0.6,0.7$, including $L=0.7$, just after the activation of $n=4$.
  - One exception: the true even ground state at $L=0.7$, where $\lambda'=-3.5\cdot10^{-11}$ is at the double-precision floor (ratio 0.9915).
- **N10. Positivity**. Every case covered by Theorem 5 has a one-signed ground state and $\lambda'<0$. Contrast cases not covered by any proof:
  - even, true pole, $L=0.4$: positive ground state, $\lambda'=-0.0077$;
  - odd with primes, $L=0.6$: $\lambda'=-4\cdot10^{-5}$.

### 13.1 Which checks test the constant 2, and the independent check

**What each check tests** (final referee, M2). Suppose the layer integral of Lemma 8.3 were $\kappa A^{(1)}A^{(2)}\delta$ instead of $A^{(1)}A^{(2)}\delta$. Then the following would all still hold exactly, with the same predicted numbers:
- N1, N2: the exact cross identity (Lemma 8.1). No $A$ appears in it.
- N3: $X^2=\lambda_e'\lambda_o'$. Both sides would scale by $\kappa^2$.
- N4: $L(\lambda_e-\lambda_o)\Phi'(0)=\pm1$. Theorem 4 would give $A^2=1/(2\kappa L)$, and the mixed identity would read $2\kappa A_eA_o$.
- N5: the sector ratio $(A_o/A_e)^2=\lambda_o'/\lambda_e'$.
- Theorem 4 itself.

So "primary evidence is fit-free" (v1) is true, but that evidence cannot confirm the constant, and v1's "the pure-log scaling in Theorem 4 confirms the constant independently" was circular.

**What does test it.** Only an absolute determination of $A$, compared with $\lambda'$; for the pure log, compared with the exact $\lambda'=-1/L$, which needs no Hadamard formula. There are three such checks:
1. *The project's hp-FEM fits:*
   - N9;
   - the Wiener–Hopf write-up's $\psi/V$ extrapolation at $L=0.4$, $s=0$: $A_e=1.5703$–$1.5705$ against $\sqrt{-\lambda_e'/2}=1.5694$, and $A_o=0.4477$–$0.4519$ against $0.4510$;
   - the pure-log fit $A=1.0007$ against $1/\sqrt{2L}=1$.

   These carry about 1% model uncertainty and, with primes, the prime-image bias below. They use the same solver as everything else.
2. *The final referee's P0 code*, which is independent (table below).
3. *An analytic heuristic* (not a proof). [Kw11, Lemma 4.27] applies to $\psi(\xi)=\frac12\log(1+\xi)$, which has the same high-frequency behaviour as the pure log symbol. It gives, for the half-line generalised eigenfunction, $F_\lambda(x)\sim\big(\tfrac{\lambda^2}{2(1+\lambda^2)}\big)^{1/2}\ell(x)^{-1/2}\to(2\ell(x))^{-1/2}$ for large $\lambda$. Away from the edge $F_\lambda\approx\sin(\lambda x+\vartheta_\lambda)$. With the high-frequency normalisation $\psi\approx L^{-1/2}F_\lambda(L-\cdot)$ near each edge of $(-L,L)$, this gives $A^2=1/(2L)$, i.e. $\kappa=1$. The normalisation step is a WKB-type approximation; it is not proved.

**The independent check** (the internal final referee's own code; scripts and outputs in [`checks/p0/`](checks/p0/), mainly `p0_edge.py` and `p0_anchor.py`).
- *Method.* Piecewise-constant (P0) Galerkin, which is conforming because P0 functions lie in the form domain of an order-zero form. It shares no code, discretisation or fitting with the hp-FEM.
- *Edge mesh.* Cells are stored by their offset from an anchor point, so the edge mesh reaches $r=10^{-150}$ ($\ell\approx345$), against $\ell\le32$ for the hp-FEM.
- *Edge trace.* $A$ is fitted from $\psi\ell^{1/2}=A+\sum_{k=1}^3b_k\ell^{-k}$ on $\ell\in[30,345]$, then extrapolated in the grading ratio $\rho\to1$ (error assumed $\propto(\log\rho)^2$, from $\rho=1.5,1.25$).
- *Derivative.* $\lambda'$ is a central difference with $\delta=10^{-3}$ (or $2\cdot10^{-3}$), on meshes that move with $L$.
- *Pure log.* Computed through the exact identity $Q^{\log}(f)=\frac12\iint_{|x-y|<2L}\frac{(f(x)-f(y))^2}{2|x-y|}-(\gamma+\log2L)\|f\|^2$.

*External normalisation check.* The referee's pure-log eigenvalues, converted to $L_\Delta=2Q^{\log}$ on $(-1,1)$, are $-0.68799,\ 1.73295,\ 2.72749,\ 3.41233,\ 3.90925,\ 4.31449$. The published FEM values ([HJSS], arXiv 2311.13079 v3, stated right after Prop 1.3) are $-0.6878,\ 1.7331,\ 2.7275,\ 3.4122,\ 3.9091,\ 4.3142$.

| Case | Prediction | Result | Source file (`checks/p0/`) |
|---|---|---|---|
| Pure log, $L=0.5$; states e0, o0, e1 | $2LA^2=1$ (Thm 4; $\lambda'=-1/L$ exact) | $1.00020,\ 1.00043,\ 1.00062$ at $h_0=L/500$; $1.00029,\ 1.00074,\ 1.00116$ at $h_0=L/250$. The excess shrinks by a factor $0.54$–$0.68$ when $h_0$ is halved. | `conv_purelog.out` |
| Weil form, $L=0.3$ (no prime active); $s=0$ e/o, $s=1$ e/o | $-\lambda'/(2A^2)=1$ | $0.99982,\ 0.99958,\ 0.99949,\ 0.99959$ | `weil_L0.3.out` ($\delta=10^{-3}$) |
| Weil form, $L=0.4$ (prime 2 active), mesh graded at $\pm(L-\log2)$, $h_0=L/500$; $s=0$ e/o, $s=1$ e/o | 1 | $0.99975,\ 0.99876,\ 0.99812,\ 0.99887$ | `anchor_L0.4_NH500.out` |
| same, $s=0$ e/o, $h_0=L/2000$ (with the $\rho$-shift measured at $h_0=L/500$) | 1 | $1.00020,\ 1.00026$ | `anchor_conv_L0.4.out`; recomputed in `checks/evidence.out` |
| Weil form, $L=0.6$, $s=0$ (primes 2 and 3), graded; e/o | 1 | $\rho\to1$ at $h_0=L/500$: $0.99969,\ 0.99724$; plus the $h_0$-shift to $L/2000$: $1.00007,\ 0.99943$ | `anchor_L0.6.out`, `anchor_L0.6_A.out`; `checks/evidence.out` |
| $L=0.6$, $s=1$ | — | not resolvable with P0: $\lambda\sim10^{-6}$–$10^{-5}$, below the Galerkin error of about $10^{-5}$ | `anchor_L0.6.out` |
| *Contrast:* $L=0.4$, uniform cells at the prime images (not graded) | 1 | $0.995$–$0.998$ at $h_0=L/500$; $0.9996$–$1.006$ at $h_0=L/1000$ | `weil_L0.4.out`, `weil_L0.4_NH1000.out` |

*Edge traces.* At $L=0.4$, $s=0$, the referee's edge traces are $A_e=1.5696$ and $A_o=0.4510$. The Hadamard predictions are $\sqrt{-\lambda'/2}=1.5694$ and $0.4507$, and the earlier hp-FEM fits were $1.567$ and $0.447$. For $s=1$, $A_e=0.0621$, in line with the $0.062$ of §11.

*Reproducibility.* [`checks/evidence.py`](checks/evidence.py) reruns two pure-log cases of the referee's code. It reproduces `conv_purelog.out` to $2\cdot10^{-6}$ (all printed digits), and it recomputes the derived ratios in the table from the printed numbers (`checks/evidence.out`).

*Reading.* There are thirteen cases: the pure log (three states); the Weil form at $L=0.3$ with and without the pole, both sectors; $L=0.4$ with primes, $s=0,1$, both sectors; and $L=0.6$ with primes, $s=0$, both sectors. At the base meshes ($h_0=L/500$, $\rho\to1$) the ratio is within $3\cdot10^{-3}$ of 1 in all of them. Where the $h_0$-refinement was run ($L=0.4$, $0.6$, $s=0$), it is within $6\cdot10^{-4}$ of 1 after it. This confirms $\kappa=1$ at the $10^{-3}$ level. $\kappa=1$ itself is part of the proof (Lemmas 8.2–8.3).

*Limits of the check.*
- The corrections assume smooth, additive mesh errors.
- At $L=0.6$, $\lambda'$ comes from a single mesh ($h_0=L/500$, $\rho=1.5$), while $\lambda_o$ itself moves by 2% between $h_0=L/500$ and $L/2000$. So the $L=0.6$ odd entry is the weakest.
- The referee's report summarises the corrected $L=0.4$ and $0.6$ values as "$1.000\pm0.001$". The recomputation above agrees.

*The referee's own bug, for the record.* The first version of `p0_anchor.py` computed the killing integral to the far edge from rounded absolute coordinates, and gave a spurious 1% deviation for cells below $10^{-16}$. A non-smooth residual in the edge profile exposed it (`anchor_profile_PREFIX_buggy_killing.out`). All numbers above come from the fixed code.

**Prime-image resolution bias in fitted amplitudes** (`zone_test.out`). At $L=0.4$, with primes, a mesh not graded at $y_2=L-\log2$ gives $A_e=1.57316$ and $A_o=0.45306$, against $1.57085$ and $0.45160$ graded: shifts of $0.15\%$ and $0.32\%$. With primes switched off, grading makes no difference ($1.215611$ against $1.215610$).
- *Mechanism.* The edge equation sees $\psi(y_n-r)$ through the prime shift, and $\psi$ has a one-sided $\ell^{-3/2}$ germ at $y_n$ (the kink, §15). [Superseded: the germ is two-sided, $(\frac23,-\frac13)c_nA\ell^{-3/2}$; see Theorem K3 of the companion note.] A uniform cell of size $h$ averages that germ, which gives a source error of order $c_nA\,V(h)\,\ell(h)^{-3/2}$.
- *Consequences.* This does not affect any proof. Fitted amplitudes with primes (N5, N9 at $L\ge0.4$) should carry an extra ~1% resolution uncertainty, and future numerics with primes should grade the mesh at $\pm(L-\log n)$.

**A solver bug, for the record.** The constant-term routine of the [BC] hp-FEM integrates across a cancelling $1/x$ singularity. At some $L$ (near 0.12 and 0.21) it is wrong by up to $10^{-3}$, which makes $\lambda(L)$ non-monotone and finite differences spurious. Every $L$ used above was checked to agree with a stable evaluation to 12 digits. (Two statements in the internal [BC] report were also corrected: the even/odd edge ratio drifts like $1/\ell$ rather than being constant, and the existence of $A$ is now proved.)

## 14. Relation to other work; what is new

*Rewritten in v2 (final referee, M1 and M5). v1's sentence "No published result gives either the exact boundary limit (E) … for any order-zero or log-type operator" was false as written: see [Kw11] and [GK18] below. Every citation in this section was re-checked on 2026-10-31 (§14.4).*

### 14.1 Boundary behaviour of order-zero operators: what was already known

- **The exact edge law on the half-line [Kw11].** Kwaśnicki studies the process with Lévy–Khintchine exponent $\psi(\xi^2)$, $\psi$ a CBF, killed on leaving $(0,\infty)$. Its transition operators have bounded generalised eigenfunctions $F_\lambda(x)=\sin(\lambda x+\vartheta_\lambda)-G_\lambda(x)$ (Thm 1.1).
  - **Lemma 4.27:** if $\psi$ is unbounded and regularly varying at infinity of order $\alpha\in[0,1]$ (**order 0 included**), then $F_\lambda(x)\sim\Gamma(1+\alpha)^{-1}\big(\lambda^2\psi'(\lambda^2)/\psi(x^{-2})\big)^{1/2}$ as $x\to0^+$.
  - **Example 6.4** (variance gamma, $\psi=\log(1+\xi)$): $F_\lambda(x)\sim C_\lambda/\sqrt{|\log x|}$ with $C_\lambda=\lambda/\sqrt{2+2\lambda^2}$; "in particular, $F_\lambda$ is not Hölder continuous".
  - Our $\varphi$ is an unbounded, slowly varying CBF (Lemmas 4.1, 4.3(b)), so Lemma 4.27 applies to the archimedean symbol.
  - So **the exact $\ell^{-1/2}$ edge law, with an explicit constant, is known on the half-line**, for generalised eigenfunctions of the archimedean part alone.
  - Not covered by [Kw11]: bounded intervals; $L^2$ eigenfunctions; any perturbation.
- **Boundary limits of ratios [GK18].** Grzywny–Kwaśnicki, **Thm 1.11**, covers isotropic unimodal Lévy processes satisfying their (1.10), (1.11) and (1.13), log-type densities included.
  - The archimedean process satisfies these hypotheses with $\alpha=0$. This was checked in the project's internal prior-art review (not included).
  - Conclusion of the theorem: every **nonnegative** regular harmonic function $f$ that vanishes outside $D$ has a finite limit $\lim_{x\to z}f(x)/\mathbb E^x\tau_{D\cap B}$ at every boundary point.
  - Remark 1.12(b) extends this to killing by a nonnegative Schrödinger potential.
  - Not covered by [GK18]: sign-changing functions; sign-changing or nonlocal perturbations (prime shifts, pole); eigenfunctions above the bottom of the spectrum, which are harmonic only for a potential of the wrong sign; and a limit relative to $\ell^{-1/2}$ rather than to the expected exit time.
- **Two-sided bounds of order $\ell^{-1/2}$.**
  - Grzywny–Ryznar [GR12]: geometric stable processes (Green function, Poisson kernel, $V$).
  - Kim–Mimica [KM14]: boundary-Harnack-type comparability.
  - Bogdan–Grzywny–Ryznar [BGR15]: torsion and survival, (2.17) and Prop 2.4.
  - For the log-Laplacian, Hernández-Santamaría–López Ríos–Saldaña [HLS24]:
    - Thm 1.1: $|u|\le C\ell^{-1/2}$ for bounded weak solutions with bounded right side, under an exterior sphere condition;
    - Thm 1.2: the exponent $\frac12$ is optimal, shown via the torsion function of a ball;
    - Thm 1.4: a Hopf lemma, $\liminf u/\ell^{-1/2}>0$, for nonnegative supersolutions.
  - None of these proves that the limit exists for an eigenfunction.
- **[FJW22], Remark 1.2(iii).**
  - What it says: for the fractional eigenfunctions $\varphi_{k,s}$, $s\in(0,\frac14]$, there is a uniform decay envelope $h_k$, but "the optimal rate of the uniform boundary [decay] remains open". It conjectures $h_k(x)\sim(-\ln\operatorname{dist}(x,\Omega^c))^{-\tau}$.
  - Remark 1.5 there: eigenfunctions of the log-Laplacian satisfy $|\varphi|=O(\ell^{-\tau})$ for every $\tau\in(0,\frac12)$.
  - *Correction to v1.* v1 said this remark lists the optimal boundary rate *of the log-Laplacian* as open. It is about the uniform-in-$s$ decay of the fractional eigenfunctions. The log-Laplacian bound with the sharp exponent $\frac12$ came later, in [HLS24, Thm 1.1].
- **Pohozaev and Hadamard formulas.**
  - Proved Hadamard formulas exist for $(-\Delta)^s$, $s>0$: [DFW21, Thm 1.1], [RS14], [DFW22]. In renewal normalisation the DFW boundary constant $\Gamma(1+s)^2$ is 1 per endpoint (§8).
  - The only claimed log-Laplacian Pohozaev identity, [AGV], was **withdrawn on 26 Apr 2025** (v2), "due to a crucial error in Proof of Pohozaev identity". According to the project's internal prior-art review, its claimed boundary term is of the type of Theorem 4. We did not re-derive its 1-D form from the withdrawn v1.
- **Simplicity on an interval.** For $(-\Delta)^s$: [FGMP23], with a one-page proof in [Kw23]. The simplicity argument of Theorem 4 is the order-zero analogue of [Kw23].
- **Tools.** All classical:
  - Wiener–Hopf factorisation of CBF symbols [Kw11, §3, Lemma 3.8];
  - Silverstein's half-line Green function [Ber96, Thm VI.20];
  - Krein's resolvent-derivative identity [Den, Lemma 2.3], and the finite-$N$ commutator identities [CCM, Lemma 5.2], [CvS, Lemma 5.1].
- **Reformulation.** Suzuki [Suz] treats the principal part of the localized Weil form as a Beurling–Deny form. Haran's potential-theoretic reading of the local terms is older.

### 14.2 Earlier work in and around the project

- **mathia** (github.com/murillo128/mathia, `research/prime_lattice/findings/`) **had (E) in substance.**
  - The chain:
    - PL-319 gives an exact endpoint identity for the logarithmic profile.
    - PL-320–322 show that the $Q^{-1/2}$ coefficient is forced, and control the residual moment.
    - PL-323 closes the pointwise flux gate by a coercive tail comparison (a maximum-principle argument).
    - PL-329 gives a sharp source-amplitude threshold.
    - PL-336 shows that, given a uniform $L^\infty$ bound, the quotient expansion $u_0(1-2e^{-Q})=C_0Q^{-1/2}+O(Q^{-1})$ holds (PL336-6). This is (E) with our rate, in mathia's coordinates $Q=\log\frac2{1-x}$ on $(-1,1)$.
    - PL-337 supplies that $L^\infty$ bound through every prime activation, via Jarohs–Kassmann–Weth and the positive-atomic-jump form of the prime shifts.
    - PL-332 gives continuity of the coefficient across the first activation.
  - The chain has one unwritten step: the pointwise realisation of the singular-integral comparison in PL-323. Our proof of (E) does not use it (Green function, no maximum principle), and it adds the explicit formula.
  - **PL-319–337 should be credited as an earlier derivation of the same law.**
- **mathia PL-338: the prime-activation mechanism.**
  - PL-338 proves norm-resolvent continuity through every finite prime-power activation.
  - It computes the contribution of the newly born channel on odd states: $4\frac{\Lambda(q)}{\sqrt q}C_0^2\frac{\delta}{L_\delta}(1+o(1))$ with $L_\delta=\log(a_\delta/\delta)$ (PL338-10). This is first-order flat, of order $\delta/\log(1/\delta)$.
  - This is the mechanism behind the activation term $-4c_nA_+A_-h/\ell$ of N6 (for odd states $A_-=-A_+$). **Credit PL-338 for it.**
- **mathia does not have an unconditional (H).** The final referee confirmed this.
  - PL-297 is fractional.
  - **PL-306** shows that any zero-order Hadamard law compatible with Suzuki's form forces the boundary stress from the virial residual. That is a consistency statement between Hadamard and virial, **conditional on the Hadamard law**.
  - PL-307/308 give the fixed-$\sigma$ virial.
  - The zero-order reduction was blocked by gates G1–G3: small-$\sigma$ uniformity; BV and Feynman–Hellmann of the actual branch; identification of the fractional and log traces (the $\sqrt2$ of PL-310). The cross identity bypasses all three.
- **Shared with mathia.** Theorem 5(b) is close to PL-324 and PL-335 (the odd-sector Beurling–Deny threshold $2L\le\log2$, and Hopf at the threshold). It is proved here by a different argument.
- **Eberwein** [Eb] (Zenodo 23177438, v1, 6 Oct 2026, §13 "Numerical pitfalls"; code `sem.py`).
  - He writes that "near-null eigenvectors have weak singularities at every log n and L − log n". His window is $[0,L_{\rm Eb}]$ with $L_{\rm Eb}=2L$, so these are exactly our $\pm(L-\log n)$. He grades his meshes there.
  - **Eberwein found the locations of the weak singular points.** Theorem 1 supplies the edge germ those points inherit. The amplitude law there (the kink law) is open (§15).
- **[BC]**, an earlier unpublished numerical study in this project, formulated (H), the mixed identity and the edge-free test, and supplied the first numerics. Its hypotheses now stand as follows:

| Hypothesis | Status |
|---|---|
| H0 (the identity) | Theorem 3(c) (with $\langle\psi_o,\psi_e'\rangle:=\Phi'(0)$) |
| H1 (existence of $A$) | Theorem 1 |
| H4 ($\psi_e'$ in the form domain) | not needed |
| H6 | Theorem 5(c), for $2L\le\log2$ |
| H2, H3, H5 | still hypotheses |

### 14.3 What appears new

This is narrower than v1 claimed. *Note added 2026-10-31:* items 1 (existence, but not the rate or the explicit formula), 2, 3 ($|A_+|=|A_-|$ and rank $\le1$) and 4 were obtained earlier in rStation paper 67 by bramble_trace (see the priority note at the top). What remains here is the rate and explicit formula in item 1, the mixed and edge-free identities in item 3, and the dilation proof of the trace value. "New" here means: not found in the search listed in §14.1–§14.4.
1. **(E) on a bounded interval, with primes and pole.** The setting: every $L^2$ Dirichlet eigenfunction of $\mathcal E+w_s$ on $(-L,L)$, where $\mathcal E$ is an order-zero CBF jump form and $w_s$ adds sign-changing bounded nonlocal terms (all prime shifts, the rank-2 pole).
   - The limit $A_\pm$ exists, with rate $O(\ell^{-1})$ and the explicit formula of Theorem 1(3).
   - No sign, simplicity, parity or arithmetic condition is needed.
   - Closest prior work: [Kw11] (half-line, generalised eigenfunctions, no perturbation); [GK18] (nonnegative harmonic functions, limit relative to $\mathbb E^x\tau$); mathia PL-319–337 (the same law for this form, with one step unwritten).
2. **(H) for an order-zero operator.** We found no Hadamard formula for any log-type or order-zero operator.
3. **Theorem 3**: the translation identity; $|A_+|=|A_-|$; rank $\le1$; the mixed and edge-free identities.
4. **Theorem 4**: for the 1-D log-Laplacian, every Dirichlet eigenvalue is simple, and $A^2=1/(2L)$ for every eigenfunction. This is the result most suitable for a short separate paper (final referee, item 7).
5. Theorem 5(c) and (d): consequences specific to this project.

**Not new:**
- the tools (§14.1);
- the $\ell^{-1/2}$ scale, and the half-line law [Kw11];
- the locations of the weak singular points [Eb];
- the activation mechanism (PL-338).

**Assessment.** Apparently new results, proved with known tools. Absence in our searches is not evidence of novelty.

**Before any public claim:**
- **An external specialist read.** Ask someone from Kwaśnicki's CBF/Wiener–Hopf circle and someone from the Weth/Saldaña log-Laplacian circle. Focus on:
  - Prop 5.1, Step 4;
  - Lemma 6.1, Steps 2–4;
  - Lemmas 8.3–8.4 (uniformity in $L$).
- **Targeted searches:** Kwaśnicki and coauthors on CBF operators on intervals; the Weth group on log-Laplacian spectra; Chen–Véron, arXiv 2011.05692. Two light web searches on 2026-10-31 ("Hadamard formula … logarithmic Laplacian"; "simplicity of Dirichlet eigenvalues logarithmic Laplacian interval") found nothing that covers (H) or Theorem 4.

### 14.4 Citation check (2026-10-31)

| Citation | Cited for | How checked | Result |
|---|---|---|---|
| [Kw11] Kwaśnicki, Studia Math. 206(3) (2011) 211–271, DOI 10.4064/sm206-3-2, arXiv 1006.0524 | Lemma 4.27; Example 6.4; Lemma 3.8; Props 2.14, 2.17, 2.18, 3.4 | arXiv abstract page (journal ref, DOI); statements read in a local copy of the text of arXiv v4 | As cited. The numbering is that of arXiv v4 (22 Oct 2011, "major revision"). We did not check the numbering of the journal version. |
| [GK18] Grzywny, Kwaśnicki, SPA 128(1) (2018) 1–38, DOI 10.1016/j.spa.2017.04.004, arXiv 1611.10304 | Thm 1.11; Remark 1.12(b) | arXiv page; RePEc record (volume, pages); statement read in the local text of arXiv v2 | As cited. |
| [FJW22] Feulefack, Jarohs, Weth, J. Fourier Anal. Appl. 28 (2022) 18, arXiv 2010.10448 | Remark 1.2(iii); Remark 1.5 | arXiv v2 PDF read | Exists. **v1's description was inaccurate**; corrected in §14.1. |
| [AGV] Arora, Giacomoni, Vaishnavi, arXiv 2411.15985 | withdrawal | arXiv abstract page | v1 dated 24 Nov 2024; v2 (26 Apr 2025) is a withdrawal "by the authors due to a crucial error in Proof of Pohozaev identity". |
| [HLS24] Hernández-Santamaría, López Ríos, Saldaña, arXiv 2401.18033 | Thms 1.1, 1.2, 1.4 | arXiv HTML of v2 | As cited. No journal reference is listed on arXiv. |
| [HJSS] Hernández-Santamaría, Jarohs, Saldaña, Sinsch, arXiv 2311.13079 | log-Laplacian eigenvalues on $(-1,1)$ | arXiv HTML of v3 | The six values are stated right after Prop 1.3. The final referee wrote "Prop. 1.3". |
| mathia PL-306, PL-319–338 | as in §14.2 | repository files (github.com/murillo128/mathia) | As cited. |
| [Eb] Eberwein, Zenodo 23177438 | §13 | Zenodo record (title, author, 6 Oct 2026, v1); text of §13 read in a local copy | As cited. |
| [Kw23] arXiv 2311.00713; [FGMP23] Calc. Var. 62 (2023) 233 | simplicity on an interval (fractional) | web search | As cited. |
| [GR12], [KM14], [BGR15], [DFW21] | two-sided bounds; fractional Hadamard formula | local copies | Present. Statements as summarised by the internal prior-art review; not re-read here. |

## 15. What this gives for the kink and tail laws, and what blocks next

(E) and (H) were the two inputs that an internal novelty audit named. Both are now proved. They do not yet turn the two laws into theorems; each law needs one more lemma of its own. A third item, $A_e\ne0$, decides whether the laws are informative for the true even ground state.

**N-tail (blocks the 1/T tail law).** The audit's statement of the tail law (its items S4–S5) needs two inputs.
- **(H1) Fourier-side edge law.** For a sector-simple eigenfunction,
$$\frac1T\int_T^{2T}t^2\,\sigma(t)\,|F(t)|^2\,dt\to A_+^2+A_-^2=2A^2,$$
  with $\sigma=\Psi_a+$const, and the interior singular points contributing $o(1)$.
- **(H2)** $\int_T^\infty|F|^2\,dS_N=o(1/T)$, where $S_N$ is the oscillating part of the zero count.

With (H) now proved, (H1) and (H2) give $\pi T(1-S(T))\to|d\ln\lambda_0/dL|$.

Route for (H1): the Wiener–Hopf representation $\hat u=\hat k/K(-it)$ with $k=A+O(V)$ near 0 (Prop 5.1, Lemma 5.2). It needs mean-square control of the interior (kink) germs; those are $O(\ell^{-3/2})$, so their contribution is relatively $O(1/\log^2T)$.

Route for (H2): partial summation, using $S_N(T)=O(\log T)$ and Landau–Gonek for the $\cos(2Lt)$ and $\cos(t\log n)$ interference terms.

**N-kink (blocks the kink amplitude law).** This is the audit's K2. Near a generation-1 point $y_n=L-\log n$ that is isolated from the other generation-1 points,
$$\psi(y)=g(y)+c_nA\,\mathbf 1_{\{y<y_n\}}\,\ell(y_n-y)^{-3/2}(1+o(1)),$$
with $g$ carrying only weaker singularities.

Route: interior localisation $\chi_1\psi=r_q*f_1$ (§7, step 5). The source contains the one-sided germ $c_nA\,V(y_n-\cdot)\mathbf 1_{\{\cdot<y_n\}}$, by Theorem 1. What remains is an Abelian lemma for the free resolvent kernel $r_q(x)\sim\frac1{2|x|\ell(|x|)^2}$ acting on one-sided slowly varying germs, with error control. This is the same kind of estimate as Lemmas 5.2 and 8.2.

**N-sign: $A_e\ne0$ for the true even ground state ($s=1$).** This is the one sub-target of the original task that is *not* proved. It is not a pure analysis lemma.
- On the even sector the pole is rank one, $2s(\int f\cosh\frac x2)^2$.
- So $\psi_e(s)\propto(A^{(0)}_e-\lambda_e(s))^{-1}\eta$ with $\eta=\cosh\frac x2$ (Aronszajn–Krein). Hence $A_e(s)$ is proportional to $\tau(\lambda_e(s))$, where $\tau(\lambda):=A_+[(A^{(0)}_e-\lambda)^{-1}\eta]$ is computed in the pole-free (Markovian) form.
- By Theorem 3(d) and 5(c), $\tau(\lambda_o)=0$ whenever H6 holds.
- So "$A_e(s)\ne0$ on $[0,1]$" is the same as "$\tau$ has no zero on $(\lambda_0^{(0)e},\lambda_e(1)]$". That is the equivalence with simple-even noted in [BC]. It is the same hard core as Andrade's open positivity lemma (Zenodo 20682834), and $A_e(1)\propto s_{\rm up}-1$ is tiny.

Three approaches from other fields, with kill criteria:
1. **Rank-one spectral theory** (Aronszajn–Donoghue; Simon's rank-one notes).
   - *Idea:* prove that $\tau$ has a single zero in the first even gap of the Markovian form, using the formal representation $\tau(\lambda)=\sum_k\frac{\langle\varphi_k,\eta\rangle A_+(\varphi_k)}{\lambda_k-\lambda}$ (its convergence is not established) and $A_+(\varphi_0)>0$, $\langle\varphi_0,\eta\rangle>0$ (Theorem 5(a)).
   - *First step:* compute $\tau$ on the gap at $L=0.3,0.4,0.6$ with the existing hp-FEM, and count its zeros.
   - *Kill criterion:* $\tau$ has $\ge2$ zeros in the gap at some $L$, or the single-zero statement needs $\lambda_e(1)<\lambda_o$ as input. The latter is circular with simple-even.
2. **Nodal theory via extension** (Frank–Lenzmann, Acta Math. 2013; Kwaśnicki–Mucha extension for CBF symbols [KM18]).
   - *Idea:* realise $\varphi(-\partial^2)$ as the Dirichlet-to-Neumann map of a Krein string, and run a Sturm/Courant nodal count for the even branch in $s$. The aim is to exclude an interior node for $s<s_{\rm up}$, which is H3 of [BC], and so $A_e\ne0$.
   - *First step:* write the Krein string for $\varphi$; its spectral measure is explicit, with atoms at $a_k^2$.
   - *Kill criterion:* the pole and prime shifts cannot be encoded as boundary data that preserve the nodal-count monotonicity. This is likely for $s>0$.
3. **Computer-assisted proof** (interval arithmetic; the project's Arb pipeline).
   - *Idea:* certify $A_e(L_j)>0$ on a grid through the explicit formula $A_+=\int v_qf_q$ with certified $L^\infty$ enclosures of $\psi$. Cover the gaps between grid points with a modulus of continuity of $A(L)$.
   - *First step:* certified $A_e$ at $L=0.4$ to relative $10^{-3}$.
   - *Kill criterion:* $A_e\propto s_{\rm up}-1$ is about $4\cdot10^{-7}$ at $L=0.6$ and below $10^{-14}$ at $L\ge0.8$, and $A(L)$ has only a $1/\log$ modulus at activations (N6). If the enclosure width at $L=0.6$ cannot be pushed below $10^{-7}$ within 4 GB, stop. Theorem 5(d) already gives the nowhere-dense statement for free.

**Recommendation.** Do N-kink and (H1) next. Both look like the same kind of analysis as §§5–8, and both run on the existing hp-FEM for checks. Treat N-sign as part of the simple-even problem, not as a lemma for this line.

---

## References

**External**
- [AGV] R. Arora, J. Giacomoni, A. Vaishnavi, *Nonlocal elliptic equations involving logarithmic Laplacian: existence, non-existence and uniqueness results*, arXiv 2411.15985 (v1 24 Nov 2024; **withdrawn** 26 Apr 2025).
- [Ber96] J. Bertoin, *Lévy Processes*, CUP 1996, Thm VI.20 (Silverstein).
- [BGR15] Bogdan, Grzywny, Ryznar, PTRF 162 (2015), arXiv 1307.0270.
- [CCM] Connes, Consani, Moscovici, arXiv 2511.22755, Lemma 5.2.
- [CvS] Connes, van Suijlekom, arXiv 2511.23257, Lemma 5.1.
- [CW19] H. Chen, T. Weth, CPDE 44 (2019), arXiv 1710.03416.
- [Den] S. Denisov, arXiv 0908.4049, Lemmas 2.1, 2.3.
- [DFW21] Djitte, Fall, Weth, *A fractional Hadamard formula and applications*, Calc. Var. 60 (2021) 231, arXiv 2002.07719.
- [DFW22] Djitte, Fall, Weth, arXiv 2112.10653.
- [DLMF] NIST DLMF 5.11.2.
- [FGMP23] Fall, Ghimenti, Micheletti, Pistoia, Calc. Var. 62 (2023) 233.
- [FJW22] Feulefack, Jarohs, Weth, *Small order asymptotics of the Dirichlet eigenvalue problem for the fractional Laplacian*, J. Fourier Anal. Appl. 28 (2022) 18, arXiv 2010.10448, Remarks 1.2(iii) and 1.5.
- [FL13] Frank, Lenzmann, Acta Math. 210 (2013).
- [FOT] Fukushima, Oshima, Takeda, *Dirichlet Forms and Symmetric Markov Processes*, 2nd ed., §4.4 (other write-ups only).
- [GK18] T. Grzywny, M. Kwaśnicki, *Potential kernels, probabilities of hitting a ball, harmonic functions and the boundary Harnack inequality for unimodal Lévy processes*, Stoch. Proc. Appl. 128 (2018) 1–38, arXiv 1611.10304, Thm 1.11, Remark 1.12(b).
- [GR12] Grzywny, Ryznar, Colloq. Math. 129 (2012), arXiv 1107.0745, Lemma 4.3.
- [HJSS] Hernández-Santamaría, Jarohs, Saldaña, Sinsch, *FEM for 1D-problems involving the logarithmic Laplacian*, arXiv 2311.13079 (v3), eigenvalues after Prop 1.3.
- [HLS24] Hernández-Santamaría, López Ríos, Saldaña, *Optimal boundary regularity and a Hopf-type lemma for Dirichlet problems involving the logarithmic Laplacian*, arXiv 2401.18033, Thms 1.1, 1.2, 1.4.
- [JKW] Jarohs, Kassmann, Weth, arXiv 2311.15337.
- [Kat] T. Kato, *Perturbation Theory for Linear Operators*, 2nd ed., Thm VI.2.1 (first representation theorem).
- [KM14] Kim, Mimica, TAMS 366 (2014), arXiv 1208.5112.
- [KM18] Kwaśnicki, Mucha, J. Evol. Equ. 18 (2018), arXiv 1707.02475.
- [KMR13] Kwaśnicki, Małecki, Ryznar, Ann. Probab. 41 (2013), arXiv 1103.0935, Props 4.3, 4.5.
- [Kw11] M. Kwaśnicki, *Spectral analysis of subordinate Brownian motions on the half-line*, Studia Math. 206(3) (2011) 211–271, arXiv 1006.0524 (numbering of v4): Def 3.1, Lemma 3.8, Props 2.14, 2.17, 2.18, 3.4, Lemma 4.27, Example 6.4.
- [Kw23] M. Kwaśnicki, *Simplicity of eigenvalues of the fractional Laplace operator in an interval*, arXiv 2311.00713.
- [Paz] A. Pazy, *Semigroups of Linear Operators*, §§1.8, 3.1 (cited in v1; no longer needed, §12).
- [RS14] Ros-Oton, Serra, ARMA 213 (2014), arXiv 1207.5986, Prop 1.6, Thm 1.9.
- [Rud] W. Rudin, *Real and Complex Analysis*, 3rd ed., Thm 19.2.
- [SSV] Schilling, Song, Vondraček, *Bernstein Functions*, 2nd ed., Thm 6.2 (CBF representation) and Thm 5.2 (convolution semigroup of a Bernstein function). The number 5.2 was not re-checked against the book; the statement is the standard correspondence between Bernstein functions and subordinators.
- [Suz] M. Suzuki, arXiv 2606.09096.
- [Eb] L. Eberwein, *The truncated Weil quadratic form: inertia, visibility, structural measurements, and no-go theorems for the Riemann Hypothesis*, Zenodo 23177438 (v1, 6 Oct 2026), §13 (locations of the weak singular points at $\log n$ and $L-\log n$ of his window, i.e. our $\pm(L-\log n)$); code `sem.py`.

**Author's and internal**
- [GS] J. A. Botha, *A certified simple, even ground state of the localized Weil quadratic form for all windows $L\in(0,1.19]$*, computer-assisted note, release 2026-10-26 (github.com/AlexGenusCore/weil-ground-state-simple-even, NOTE.md §3; the paper source, §2, fixes the normalisation and defines $A_L$ as the closure on $C_c^\infty$). Unrefereed. Input to Theorem 5(d), which uses only the range $(0,1.19]$.
- [BC] An earlier unpublished numerical study in this project (report §§2–5 and an hp-FEM solver). Not public.
- mathia, github.com/murillo128/mathia, `prime_lattice/findings`: PL-268, PL-297, PL-305–313, PL-319–338 (in particular PL-306, PL-319–323, PL-329, PL-332, PL-336–338).
- An internal novelty audit of the kink and tail laws (not public).
- The internal final referee's report on v1 (not public; verdict "accept as proved"), with its scripts and outputs in [`checks/p0/`](checks/p0/).

## Appendix: provenance

The internal write-ups named below are working documents and are not included in this repository. All referees were AI referees.

| Piece | Source | Refereed by |
|---|---|---|
| §§3–9 (E), (H), Theorem 3(c)–(e), rate | Wiener–Hopf write-up | two internal referees |
| Lemma 6.1 Step 2 (direct domination) | an internal referee's suggested fix | written here |
| (E)/(H), second proofs | probabilistic, Pohozaev-direct and Krein–Sakhnovich write-ups | two internal referees each |
| Theorem 3(a),(b) (isotropy, rank $\le1$) | Krein–Sakhnovich Cor 4.1; Pohozaev-direct C5 | internal referees |
| Theorem 4 (all eigenfunctions, simplicity) | Pohozaev-direct Thm B and Cor B2; Krein–Sakhnovich Thm 5; left-endpoint dilation (a referee's suggestion) | written here |
| Theorem 5(a) | Wiener–Hopf Cor 10.5(a); Krein–Sakhnovich Thm 6; probabilistic Thm E; strictness and simplicity written here | internal referees |
| Theorem 5(b) | Wiener–Hopf Cor 10.5(b); probabilistic Prop E2 | internal referees |
| Theorem 5(c) | combination of Pohozaev-direct C4 and Wiener–Hopf 10.5(b) | synthesis; checked by the final referee |
| Theorem 5(d) | a referee's suggestion; strict monotonicity proof; v2: open interval, [GS] named as input | synthesis; checked by the final referee (v1 form) |
| Lemma 3.6, Prop 5.1 and Lemma 6.1 in full (v2) | expansion of the Wiener–Hopf write-up §§3, 5 and of v1; no new mathematics | written out in v2; not yet refereed in this form |
| §13.1 table | final referee's P0 code and outputs (`checks/p0/`); derived ratios recomputed, two runs reproduced (`checks/evidence.py`) | — |
| Activation modulus, constant-term bug | Krein–Sakhnovich referee | — |
| Explicit-formula check, $V$ normalisation | probabilistic-write-up referee | — |

**Consistency of the combination.**
- All write-ups use the same $J=b/2$, $c=\psi(\frac14)-\log\pi$, $\ell$ and $A$.
- The renewal functions differ: $V_1$ here, $V_0$ in the probabilistic write-up. Both satisfy $V\ell^{1/2}\to1$, so $A$ does not depend on the choice.
- Every write-up obtains the constant 2 from $J\sim\frac1{2u}$. Their pure-log "check" of the constant is not independent of it (§13.1); the absolute-amplitude numerics are.
- They are four refereed write-ups of closely related arguments, not four independent proofs (§12).
