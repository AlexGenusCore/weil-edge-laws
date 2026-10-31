# Pre-registered numerics: kink-law and tail-law constants

An independent float64 test of the constants predicted by the kink and tail laws, with a new continuous piecewise-linear (P1) Galerkin solver. Nothing here is certified, and nothing here is a statement about the Riemann hypothesis. Like the rest of this repository, it was produced largely with an AI assistant and has been checked only by AI referees (see [`../README.md`](../README.md)).

- [`numerics.md`](numerics.md): the report (method, gates, results, deviations from the registration).
- [`PREREG.md`](PREREG.md): the pre-registration, kept byte-for-byte. Its internal labels kink-wienerhopf, kink-levy, tail-abelian and tail-explicit are the write-ups [KW], [KL], [TA], [TE] of the notes.

## Checksums

```
head -1 PREREG.md5 | md5sum -c -        # PREREG.md: OK
tail -n +3 PREREG.md5 | md5sum -c -     # registered code; kink_analyze.py FAILS, see below
md5sum -c out/final_md5.txt             # final code: all OK
```

`kink_analyze.py` was changed after registration (md5 `8404f5dc…` → `87a74c8b…`): a pairing fix, disclosed in `numerics.md` §6. The right-side values are unchanged. The registration time is in `PREREG.md5` (04:27:15 SAST; the text of `PREREG.md` says 04:30).

## How to run

Requirements: Python 3.10+, numpy, scipy, mpmath. python-flint is needed only to regenerate the zeros. Each run in the batches is limited to 4 GB (`ulimit -v`) and 1 hour, and the runs are sequential.

```
python3 p1weil.py zeros.txt          # gates: jump form, prime shifts, pole, Weil's explicit formula with 10 500 zeros
python3 zeros_make.py 10500          # optional: regenerate zeros.txt (Arb) and zeros_check.out (mpmath cross-check)
python3 prereg_table.py              # constants c_n, beta_n, chain weights (prereg_table.out)

./conv_batch.sh > conv_batch.log     # convergence study (writes out/kconv_*.json, out/tconv_*.npz)
./prod_batch.sh > prod_batch.log     # registered production runs (several hours)
./diag_batch.sh > diag_batch.log     # post-registration diagnostic at L = 1.0 (waits for prod_batch.log)

python3 kink_summary.py > out/kink_summary.out   # registered kink verdicts
python3 kink_table.py   > out/kink_table.out
python3 tail_summary.py > out/tail_summary.out   # registered tail verdicts
python3 tail_posthoc.py > out/tail_posthoc.out   # post hoc, not registered
```

The batch scripts use `$PY` (default `python3`). Run all commands from this folder.

## What is included

- All scripts (solver, runs, analysis, pilots and surveys) and the 10 500 zeta zeros (`zeros.txt`, 30 digits, Arb; checked against mpmath at 259 indices).
- The small outputs: verdicts and tables (`out/*.out`), batch logs and final checksums.
- **Not included:** the raw run data `out/*.json` and `out/*.npz` (about 27 MB). The batch scripts regenerate them; the summary scripts need them.
