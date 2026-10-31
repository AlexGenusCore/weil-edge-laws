#!/bin/bash
# K5 rerun at L = 1.0, registered in PREREG_K5_L1.md. One process at a time.
# [VM] limits: 3 BLAS threads, address space <= 12 GB (ulimit -v), nice 10, timeout 3 h per run.
cd "$(dirname "$0")"
export OPENBLAS_NUM_THREADS=3 OMP_NUM_THREADS=3 MKL_NUM_THREADS=3
PY=${PY:-python3}
run() { echo "=== $(date '+%F %T') $*"; (ulimit -v 12582912; nice -n 10 timeout 10800 /usr/bin/time -f 'maxrss_kb=%M wall=%e' $PY "$@"); echo "=== exit $?"; }
for r in 1.5 1.25 1.15; do run k5_run.py 1.0 $r 1e-30 40 0,5 3 out/k5L1_r$r.json; done
nice -n 10 $PY k5_summary.py 'PRIMARY: L=1.0, rho in {1.5, 1.25}=out/k5L1_r1.[25]*.json' > out/k5_summary_primary.out
nice -n 10 $PY k5_summary.py 'SUPPLEMENTARY: L=1.0, rho in {1.5, 1.25, 1.15}=out/k5L1_r*.json' > out/k5_summary_supp.out
echo "=== all done $(date '+%F %T')"
