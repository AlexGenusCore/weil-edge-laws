# Numerical supplement

Supplement to *Edge laws, a Hadamard formula and kink singularities for eigenfunctions of the localized Weil
quadratic form*, by Johann Alexander Botha (contact: info@genuscore.com), draft of 31 October 2026.

Everything here is an **uncertified double-precision computation**, written with AI assistance and checked so far
only by AI reviewers. The error bands are systematic estimates, not rigorous bounds. Nothing here is used in the
proofs, and nothing here is a statement about the Riemann hypothesis.

All paths below are relative to this folder. Every script finds its own inputs relative to its own location or to
the folder it is run from, as stated; no absolute paths are needed.

## Contents

| Path | What it is |
|---|---|
| `registered/` | The first pre-registered P1 study ("[NUM]" in the notes): registration `PREREG.md` + `PREREG.md5`, the P1 solver `p1weil.py` with `runlib.py`, the drivers `kink_run.py`, `tail_run.py`, the analysis `kink_analyze.py`, `tail_analyze.py`, the verdict scripts `kink_summary.py`, `kink_table.py`, `tail_summary.py`, `tail_posthoc.py`, the batch scripts `conv_batch.sh`, `prod_batch.sh`, `diag_batch.sh`, the zeros `zeros.txt` (made by `zeros_make.py`; `zeros_check.out`, `zeros_make.log`), the working notes `numerics.md`, and pilot scripts (`pilot_*.py`, `survey*.py`, `prof_x8.py`, `xcheck.py`, `kink_conv.py`, `prereg_table.py`). |
| `registered/kink_analyze_as_registered.py` | The version of `kink_analyze.py` that was registered (md5 `8404f5dc…`); see "Deviations". |
| `registered/out/` | Raw output of every run: kink runs `k06_r*.json` ($L=0.6$, right side), `k06m_r*.json` ($L=0.6$, with mirror points), `k08_r*.json`, `k10_r*.json` (registered $L=1.0$ mesh), `k10g_r1.25.json` (registered sensitivity mesh), `k10d_r*.json` (post-registration diagnostic), `kconv_*.json` (pre-registration convergence runs), `test_kink*.json` (smoke tests); tail runs `tail_X{6,8,10}_{base,fine}.npz`, `tconv_*.npz` (pre-registration), `tail_smoke.npz`; batch logs; `final_md5.txt` (md5 of the scripts as used); and the verdict/summary outputs `kink_summary.out`, `kink_table.out`, `tail_summary.out`, `tail_posthoc.out`, `tail_conv.out`, `xcheck.out`. |
| `numerics/k5_L1/` | The second registered study, the $L=1.0$ rerun: `PREREG_K5_L1.md` + `.md5`, solver copies (byte-identical to `registered/`), `k5_run.py`, `k5_summary.py`, `k5_batch.sh`, `k5_batch.log`, raw output `out/k5L1_r{1.5,1.25,1.15}.json`, verdicts `out/k5_summary_{primary,supp}.out` (and the two empty files of the first summary attempt, `*_EMPTY_title_bug.out`). |
| `numerics/` | Paper tables and figure: `consolidate_kink.py` (error bands; writes `kink_errors.json`, prints `kink_errors.out`), `make_tables.py` (writes the `tab_*.tex` from data), `fig_kink_split.py` (writes `fig_kink_split.pdf`), the generated `tab_*.tex`, the hand-copied `tab_H.tex`, `tab_cX.tex`, `tab_detect.tex`, `tables.tex` and `preview.tex` (a compile check), and the working notes `numerics.md`. |
| `snap_check/` | Check of the anchor-identification rule of P1 (Methods paragraph): `snap_check.py`, `snap_check.out`. |
| `unregistered/p0/` | The piecewise-constant (P0) code of the final internal review (`p0_edge.py`, `p0_anchor.py`), its drivers and outputs, and `evidence.py`/`evidence.out`, which derives the P0 rows of Table 2. |
| `unregistered/hp/` | The hp-FEM code (`hpfem.py`), its edge fit (`edgetools.py`), the Hadamard driver `ref_excited_hadamard.py` and its outputs `excited_L{0.36,0.4,0.6,0.7}.out` (Table 2, hp-FEM row); the explicit-formula check of Section 10.1, `check_explicit_and_Vfit.py` (with `renewal_V.py` and its input `ref_hadamard_central_L0.4.out`) and its output `check_explicit_and_Vfit_L0.4.out`. |
| `unregistered/zero_side/` | Zero-side checks of the term $\varepsilon c_X$ at $X=2,3,4$ (`zero_side_split.py`, `split_x4_check.py`, `mesh_x4_check.py` with outputs), `fr_constants.py`/`.out` (constants, Landau sign check on the zeros, boosts $\beta_n$), and `zeros.json` (the first 1500 zeros, 100 digits; equal to the first 1500 entries of `registered/zeros.txt` after rounding to double precision). |
| `check_paper_numbers.py` | Recomputes the numbers quoted in Section 10 (Tables 2–6, the figure caption and the text) from the files above and compares them with the printed values. |
| `SHA256SUMS` | SHA-256 of every other file (`sha256sum -c SHA256SUMS`). |

## Environment

- **Recorded runs** (all of `registered/out/`, `numerics/k5_L1/out/`): 31 October 2026, on a Linux virtual machine
  (10 vCPUs, 48 GB), Python 3.12.16, numpy 2.5.4, SciPy 1.18.1 (OpenBLAS 0.3.34), mpmath 1.4.1, python-flint 0.9.0.
  These versions were read from that environment after the runs; they were not logged at run time. Batches ran one
  process at a time with 4 BLAS threads (`registered/`) or 3 (`k5_L1/`).
- **Unregistered P0, hp-FEM and zero-side outputs** (`unregistered/`): 30–31 October 2026, on the author's laptop
  or the same VM; package versions not recorded.
- **Re-checks for this supplement** (see "Fresh-extraction check"): the author's laptop, Python 3.12.13 with
  numpy 2.5.4 and mpmath 1.4.1 (no SciPy), and Python 3.14.4 with numpy 2.5.1 and matplotlib 3.11.1 for the figure.
- **Packages needed:** numpy for everything; SciPy optional (`p1weil.py` uses `scipy.linalg.eigh(subset_by_index=…)`
  and `lu_factor` when present, otherwise full `numpy.linalg.eigh`, which is much slower for large meshes);
  mpmath for `p1weil.py`'s constants, `hpfem.py`, `edgetools.py`, `mesh_x4_check.py`, `fr_constants.py`;
  python-flint only for `zeros_make.py`; matplotlib only for `fig_kink_split.py`. `check_paper_numbers.py` needs
  only the standard library.

## Quick check

```bash
sha256sum -c SHA256SUMS
(cd registered && md5sum -c PREREG.md5)         # kink_analyze.py FAILS by design: corrected after registration
md5sum registered/kink_analyze_as_registered.py # 8404f5dcb8e5f0fce807e1936d56d3b0 = the registered value
(cd numerics/k5_L1 && md5sum -c PREREG_K5_L1.md5) # PREREG_K5_L1.md and k5_batch.sh FAIL: redacted (see below)
python3 check_paper_numbers.py                   # every quoted number: OK / DIFF
```

(`md5sum -c` also warns about the line with the registration time; that line is not a checksum.)

## Regenerating Section 10 from the stored output

`python` is an interpreter with numpy and mpmath. Times are wall-clock on the laptop under load; memory < 0.5 GB.

| Paper item | Command | Input files | Time |
|---|---|---|---|
| Registered kink verdicts (Tables 3–6, text) | `cd registered && python kink_summary.py > out/kink_summary.out` and `python kink_table.py > out/kink_table.out` | `out/k06_r*.json`, `out/k06m_r*.json`, `out/k08_r*.json`, `out/k10_r*.json`, `out/k10g_r1.25.json` (+ `out/k10d_r*.json` for `kink_table.out`) | 2 s each |
| Registered tail verdicts (Section 10.3 text; Table 2, P1 row: the "Hadamard" value of the 12 primary states) | `cd registered && python tail_summary.py > out/tail_summary.out`; `python tail_posthoc.py > out/tail_posthoc.out`; `python tail_analyze.py conv out/tconv_fine.npz out/tconv_base.npz out/tconv_nogen2.npz > out/tail_conv.out` | `out/tail_X{6,8,10}_{base,fine}.npz`, `out/tconv_*.npz` | < 2 s each |
| Rerun verdicts (Tables 3–6, rows marked ‡) | `cd numerics/k5_L1 && python k5_summary.py 'PRIMARY L1.0 rho 1.5 and 1.25=out/k5L1_r1.[25]*.json' > out/k5_summary_primary.out` and `python k5_summary.py 'SUPPLEMENTARY L1.0 rho 1.5 1.25 1.15=out/k5L1_r*.json' > out/k5_summary_supp.out` | `out/k5L1_r*.json` | 1 s each |
| Error bands | `python numerics/consolidate_kink.py registered > numerics/kink_errors.out` (writes `numerics/kink_errors.json`) | the kink files above and `numerics/k5_L1/out/k5L1_r*.json` | 7 s |
| Table 3 (generation 1), Table 4 (generation 2), Table 5 (edge offset $D$) | `python numerics/make_tables.py registered` → `numerics/tab_kink_gen1.tex`, `tab_kink_gen2.tex`, `tab_k0.tex` (the paper inputs these three files) | `numerics/kink_errors.json`, `registered/out/tail_summary.out` | < 1 s |
| Table 6 (jump ratio) | same command → `numerics/tab_k5.tex`; Table 6 in the paper is a hand condensation of it (one row per family; bands rounded to nearest there, rounded up in `tab_k5.tex`) | same | — |
| Figure 1 | `python numerics/fig_kink_split.py registered` → `numerics/fig_kink_split.pdf`; the script asserts that its fits equal the registered values in `registered/out/kink_table.out` | `registered/out/k06_r1.15.json` | 5 s |
| Table 2 (Hadamard constant) | assembled by hand (`numerics/tab_H.tex`) from: P0 pure log `unregistered/p0/conv_purelog.out`; P0 $L=0.3$ `weil_L0.3.out`; P0 $L=0.4$ graded `anchor_L0.4_NH500.out`; P0 refined $L=0.4$ and both $L=0.6$ entries `evidence.out` (from `anchor_L0.4_NH500.out`, `anchor_conv_L0.4.out`, `anchor_L0.6.out`, `anchor_L0.6_A.out`); contrast row `weil_L0.4.out`, `weil_L0.4_NH1000.out`; P1 row `registered/out/tail_summary.out`; hp-FEM row `unregistered/hp/excited_L*.out`. `cd unregistered/p0 && python evidence.py` recomputes the derived entries and reruns two P0 cases | as listed | 15 s (`evidence.py`) |
| Section 10.1, explicit formula at $L=0.4$ | `cd unregistered/hp && python check_explicit_and_Vfit.py 0.4 > check_explicit_and_Vfit_L0.4.out` (lines "A_fit/A_pred", four fit bases) | `ref_hadamard_central_L0.4.out` | minutes (hp-FEM solve) |
| Anchor rule (Methods) | `python snap_check/snap_check.py numerics/k5_L1 > snap_check/snap_check.out` | none (meshes rebuilt from the registered arguments) | 10 s |
| Every number quoted in Section 10 | `python3 check_paper_numbers.py` | all of the above, `unregistered/zero_side/*.out` | < 1 s |

The P0 fit-model comparison and the flatness diagnostic in the paragraph on the second-order edge law
($D_{\rm fit}-D=+0.008$ to $+0.011$, $-0.03$ to $-0.06$ with a term $c/\ell$; flatness to $10^{-4}$) were computed
by the last internal review with code that was not kept. They are **not reproducible from this supplement**.

## Re-running the computations

All P1 runs are deterministic up to BLAS rounding; a re-run reproduces the stored JSON to about $10^{-13}$.

```bash
cd registered
python zeros_make.py 10500        # zeros.txt, zeros_check.out (python-flint; 125 s). Overwrites the stored files.
python p1weil.py zeros.txt        # self-check gates, incl. Weil's explicit formula with the 10 500 zeros
bash conv_batch.sh > out/conv_batch.log 2>&1   # pre-registration convergence runs (14 min)
bash prod_batch.sh > prod_batch.log 2>&1       # all registered kink and tail runs (61 min)
bash diag_batch.sh > out/diag_batch.log 2>&1   # post-registration L=1.0 diagnostic (2 min); waits for prod_batch.log
cd ../numerics/k5_L1
bash k5_batch.sh > k5_batch.log 2>&1           # registered rerun (26 min; needs /usr/bin/time)
```

The batch scripts use the interpreter in `$PY` (default `python3`) and run from their own folder. Recorded run
times (VM, 4 threads; from the logs): kink runs 3–81 s ($N=1906$–$6678$), tail runs
2.4–19 min each, address space capped at 4 GB. Rerun (3 threads): $\rho=1.5$ 96 s / 1.8 GB, $\rho=1.25$ 335 s /
4.9 GB, $\rho=1.15$ 1125 s / 11.1 GB peak RSS. A single kink run, e.g. the coarsest:
`python kink_run.py 0.6 1.5 1e-40 40 n2,n3,q3/2 0,5 3 out/k06_r1.5.json 0`.

Unregistered checks (from their folders; invocations as recorded in the output headers):

```bash
cd unregistered/p0
python conv_purelog.py > conv_purelog.out          # ~40 s
python run_weil.py 0.3 500 > weil_L0.3.out         # ~5 min
python run_weil.py 0.4 500 > weil_L0.4.out         # ~5 min
python run_weil.py 0.4 1000 > weil_L0.4_NH1000.out # ~5 min
python p0_anchor.py 0.4 500 > anchor_L0.4_NH500.out  # ~5 min
python anchor_L06.py > anchor_L0.6.out             # ~80 s
python anchor_L06_A.py > anchor_L0.6_A.out
python evidence.py > evidence.out                  # 15 s
cd ../hp
python ref_excited_hadamard.py 0.36 0.002 > excited_L0.36.out   # and (0.4, 0.005), (0.6, 0.005), (0.7, 0.002)
cd ../zero_side
python zero_side_split.py > zero_side_split.out    # X = 2, 3 and the L = 0.4 control
python split_x4_check.py > split_x4_check.out      # X = 4
python mesh_x4_check.py > mesh_x4_check.out        # X = 4, two meshes
python fr_constants.py > fr_constants.out          # Landau sign check on the zeros (section F), boosts (G)
```

The other P0 scripts and outputs (`anchor_conv.py`, `anchor_glitch*`, `anchor_profile*`, `diag_conv.py`,
`zone_test.py`, `run_purelog.py`) are the review's working files, kept for completeness; their exact invocations
were not recorded.

## Registration timeline (31 October 2026, SAST = UTC+2)

| Time | Event | Record |
|---|---|---|
| 03:49–03:55 | 10 500 zeros computed with Arb and checked against mpmath at 259 indices (max difference $4.7\cdot10^{-26}$) | `zeros_make.log`, `zeros_check.out` |
| 04:07–04:21 | Pre-registration convergence runs ($L=0.6$ kink, $X=8$ tail). Seen before registration: the kink constants of these runs and $\lambda'$ against $2A^2$ at $X=8$; no tail statistic was compared with a prediction | `out/conv_batch.log`, `PREREG.md` §0 |
| **04:27:15** | **First registration**: md5 of `PREREG.md` and of every script and `zeros.txt` | `PREREG.md5` |
| 04:27:16–05:28:18 | Registered production batch | `out/prod_batch.log` |
| 04:34 | `kink_analyze.py` corrected (pairing of the two sides; see Deviations) | `out/final_md5.txt` |
| 05:28:35–05:30:30 | Post-registration diagnostic at $L=1.0$ (not a registered test) | `out/diag_batch.log` |
| **06:31:23** | **Second registration** (rerun at $L=1.0$), written after the first study's failure was diagnosed and before its batch; checksums verified at 06:31:24 | `PREREG_K5_L1.md5` |
| 06:31:26–06:57:22 | Registered rerun batch; summaries repeated right after (Deviations, item 3) | `k5_batch.log` |
| 06:37–06:58 | Error bands and tables (post hoc) | `numerics/kink_errors.*`, `tab_*.tex` |
| 10:20 | Anchor-rule check (post hoc) | `snap_check/` |

## Verdicts, including the failures

- **Registered FAIL, kept in the record:** the jump-ratio test (route label K5, Corollary 7.6(a) of the paper) at
  $L=1.0$ failed on 17 of its 20 graded rows (8 on the registered mesh, 9 on the registered sensitivity mesh).
  The cause found afterwards is a mesh defect (coupled generation-2 points graded only to $10^{-16}$, inside the fit
  window). The rerun registered at 06:31 grades every coupled chain point through the fit window and passes 10/10
  (primary and supplementary); it is a separate test and does not convert the original FAIL.
- **Registered FAIL, open:** the edge offset (K0$'$, Theorem 7.1(c)) fails for the odd $s=5$ state in the rerun:
  $D_{\rm fit}-D=+0.00510$ (primary) and $+0.005005$ (supplementary) against the tolerance 0.005.
- **Registered FAIL on the sensitivity mesh:** K0$'$ fails on 10 of 50 rows there ($+0.0081$, $+0.0094$).
- Passes: kink generation 1 50/50 and generation 2 20/20 (plus 10/10 and 2/2 in the rerun); tail T1 11/11
  (generous tolerance); sector split T2 10/10 ($X=8$ pairs high by $2.6\sigma$ and $3.0\sigma$, the second inside the
  $3\sigma$ rule by less than 0.003). State O5 at $X=6$ missed the validity gate narrowly and is reported, not graded.

## Deviations from the registrations, and changes made for this supplement

1. `kink_analyze.py` was corrected after the first registration (md5 `8404f5dc…` → `87a74c8b…`): the two sides of a
   measured point are matched by common offsets instead of by prefix. The registered version is included as
   `registered/kink_analyze_as_registered.py`. It stops with `AssertionError: asymmetric zone` on the runs with mirror
   points (`k06m_r1.25.json`) and on `k08_r1.5.json` and `k08_r1.15.json`; on every other kink file its output is
   byte-identical to that of the corrected version (checked for this supplement).
2. Scripts written after the first registration only apply the registered criteria or make tables
   (`kink_summary.py`, `kink_table.py`, `tail_summary.py`, `tail_posthoc.py`, and everything in `numerics/`).
3. Rerun: `k5_batch.sh` passed summary titles containing "=" to `k5_summary.py`, which splits at the first "=", so
   its two summary files came out empty (kept as `*_EMPTY_title_bug.out`). The summaries were repeated with the
   same, checksum-verified code and titles without "=" (commands above); no code or data changed.
4. **Redactions for release.** The name of the virtual machine and its home-folder paths were removed:
   - `numerics/k5_L1/PREREG_K5_L1.md` (registered): the machine name → `[VM]` (twice), and its working folder
     → `[workdir]/` (once). Its registered md5 therefore no longer matches.
   - `numerics/k5_L1/k5_batch.sh` (registered): in the comment, the machine name → `[VM]`; `cd ~/<folder>` →
     `cd "$(dirname "$0")"`; the hard-coded interpreter `~/<folder>/.venv/bin/python` → `${PY:-python3}`. Its
     registered md5 therefore no longer matches. Nothing else in these two files changed.
   - `registered/{conv,prod,diag}_batch.sh` (not checksummed): the same two path changes.
   - `registered/numerics.md`, `numerics/numerics.md` (notes): the machine name → `[VM]`; one sentence naming other
     machines that were not used was deleted. `unregistered/zero_side/mesh_x4_check.py`: machine name in the usage
     line → `[VM]`.
   - Absolute import paths were replaced by paths relative to the script in `unregistered/hp/edgetools.py`,
     `ref_excited_hadamard.py`, `unregistered/zero_side/zero_side_split.py`, `split_x4_check.py`,
     `mesh_x4_check.py`, `fr_constants.py`, `unregistered/hp/check_explicit_and_Vfit.py` and
     `unregistered/p0/evidence.py`; and the 1500-zero file they read was copied in as
     `unregistered/zero_side/zeros.json`. No computational line changed. In the output
     `check_explicit_and_Vfit_L0.4.out`, a NumPy warning line printed the script's absolute path; the path was
     replaced by the file name.
   All registered checksums other than these two, and the `kink_analyze.py` entry of item 1, match.
5. The working notes (`numerics.md` in both folders) refer to folders of the author's project; in this supplement
   `scratch_archive/proof_laws/numerics/` is `registered/`, `papers/weil-edge/numerics/` is `numerics/`,
   `proof_EH/final-referee/` is `unregistered/p0/`, and the hp-FEM, `referee*-tail-*`, `repair-tail-abelian` and
   `final-referee` (constants) folders are `unregistered/hp/` and `unregistered/zero_side/`.

## Fresh-extraction check (31 October 2026)

The archive was extracted into an empty temporary folder and the following was run there. "Identical" means
byte-identical (for outputs that print a run time: identical apart from the time).

*Laptop (Python 3.12.13, numpy 2.5.4, mpmath 1.4.1, no SciPy; matplotlib on Python 3.14.4):*

- Checksums: all registered md5 values match except the three expected ones (Quick check).
- `kink_summary.out`, `kink_table.out`, `tail_summary.out`, `tail_posthoc.out`, `tail_conv.out`,
  `k5_summary_primary.out`, `k5_summary_supp.out`: regenerated, identical. With a title containing "=",
  `k5_summary.py` again writes only the tally header, as in Deviation 3.
- `kink_errors.json`, `kink_errors.out` and all six `tab_*.tex` written by `make_tables.py`: identical to the
  files the paper inputs (Tables 3–5) and to `tab_k5.tex` (Table 6 condenses it).
- `fig_kink_split.pdf`: regenerated; its text layer and a 100-dpi rendering are identical to the paper's figure,
  and the script's own assertions against the registered table pass (fitted limits 0.66679 and −0.33335).
- `snap_check.out`, `evidence.out` (which reruns two P0 cases), `fr_constants.out`: identical.
- `check_paper_numbers.py`: every number checked agrees with the paper. Two numbers in the draft did not and
  were corrected in the paper: $\Upsilon(6400)$ was printed as $0.47$–$0.81$ (the range at $X=8$ only; over the
  12 tail states it is $0.42$–$0.88$), and the explicit-formula agreement at $L=0.4$ was printed as
  $(1$–$3)\cdot10^{-5}$ (two of the four fit bases; over all four it is $1\cdot10^{-5}$ to $2.3\cdot10^{-4}$, and the
  computation is for the torsion function of the archimedean part). The Landau check holds to 0.5 % at
  $T=10\,303$, not at every $T$ in the output (at $T=2000$, $X=4$ is off by 1.6 %); the paper now says so.
- Registered against corrected `kink_analyze.py` on all kink files: see Deviation 1.
- One P1 solve (`kink_run.py 0.6 1.5 …`, the smallest registered run): every number in the JSON agrees with
  `registered/out/k06_r1.5.json` to $9\cdot10^{-14}$, and its analysis output is identical (155 s here, because
  without SciPy the full dense eigenproblem is solved; 5 s with SciPy).
- The other unregistered re-runs exceeded a 330 s cap on the laptop, which was fully loaded by unrelated jobs;
  they were repeated on the VM below.

*VM (the recorded environment; one job at a time on 2 cores, address space ≤ 8 GB):*

| Re-run | Wall time | Peak RSS | Result |
|---|---|---|---|
| `kink_run.py 0.6 1.5 …` | 5 s | 0.25 GB | as on the laptop |
| `tail_run.py 8 nogen2 …` (a pre-registration tail run) | 242 s | 0.4 GB | every array of the stored `tconv_nogen2.npz` reproduced to $4\cdot10^{-13}$; the registered `tail_run.py` also writes two states (Em1, O20) that the pre-registration version did not |
| `ref_excited_hadamard.py 0.4 0.005` (hp-FEM) | 37 s | 0.1 GB | identical to `excited_L0.4.out` |
| `check_explicit_and_Vfit.py 0.4` (hp-FEM) | 125 s | 0.1 GB | identical (the stored file also holds a NumPy warning that now goes to stderr) |
| `conv_purelog.py` (P0) | 67 s | 0.8 GB | identical |
| `anchor_L06.py` (P0) | 190 s | 0.9 GB | identical |
| `run_weil.py 0.3 500` (P0) | 513 s | 1.0 GB | identical |
| `zero_side_split.py` | 160 s | 0.35 GB | identical |
| `split_x4_check.py` | 525 s | 0.36 GB | identical |
| All 13 registered and diagnostic kink runs (`prod_batch.sh` and `diag_batch.sh` kink lines), then `kink_summary.py`, `kink_table.py`, `consolidate_kink.py`, `make_tables.py` on the new files (rerun rows from the stored `k5L1_r*.json`) | 5–96 s each, 10 min in all | 1.84 GB | `tab_kink_gen1.tex`, `tab_kink_gen2.tex`, `tab_k0.tex`, `tab_k5.tex`, `kink_errors.out` and `kink_table.out` identical; `kink_summary.out` identical in every verdict and tally line. The JSON files agree with the stored ones to $10^{-8}$; the only differences above $10^{-11}$ are in ungraded states with $\lambda\approx10^{-6}$, $\lvert A\rvert<0.003$ (rounding from the different BLAS thread count), which change a few last digits of their ungraded rows in `kink_summary.out` |

*Not re-run, and why:* the registered tail runs (`tail_X*_{base,fine}`: 4.7–19 min each on 4 threads, 13 runs in
all with the convergence runs), the rerun meshes $\rho=1.25$ and $1.15$ (335 s / 4.9 GB and 1125 s / 11.1 GB), the
remaining P0 runs (`run_weil.py 0.4 …`, `p0_anchor.py 0.4 500`, `anchor_L06_A.py`: about 5 min or more each),
`mesh_x4_check.py` (two P0 meshes, the finer at $h_0=L/2000$), the other hp-FEM cases ($L=0.36,0.6,0.7$; same code
as the $L=0.4$ case), and `zeros_make.py` (it would overwrite `zeros.txt`; its checksum matches the registered one).
Their stored outputs are the ones the tables use.

## Not included

- The code and output of the P0 fit-model comparison and flatness diagnostic (see above).
- The other hp-FEM checks of the internal notes (cross identities, sector ratios, positivity); they are not
  quoted in Section 10.
