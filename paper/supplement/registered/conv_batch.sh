#!/bin/bash
# Convergence study (run sequentially, one process at a time).
cd "$(dirname "$0")"
export OPENBLAS_NUM_THREADS=4 OMP_NUM_THREADS=4 MKL_NUM_THREADS=4
PY=${PY:-python3}
run() { echo "=== $(date +%T) $*"; (ulimit -v 4194304; nice -n 15 timeout 3600 $PY "$@"); echo "=== exit $?"; }
mkdir -p out
# kink, L=0.6, right side deep at y2, y3, L-log1.5; s=0; three grading ratios, one H refinement
run kink_run.py 0.6 1.5  1e-40 40 n2,n3,q3/2 0 3 out/kconv_r150.json 0
run kink_run.py 0.6 1.25 1e-40 40 n2,n3,q3/2 0 3 out/kconv_r125.json 0
run kink_run.py 0.6 1.25 1e-40 80 n2,n3,q3/2 0 3 out/kconv_r125_H80.json 0
run kink_run.py 0.6 1.15 1e-40 40 n2,n3,q3/2 0 3 out/kconv_r115.json 0
# tail, X=8: base / fine / no generation-2 grading
run tail_run.py 8 base   1.25 1e-9 2.0 1e-7 60  0.001 out/tconv_base.npz
run tail_run.py 8 nogen2 1.25 1e-9 0   0    60  0.001 out/tconv_nogen2.npz
run tail_run.py 8 fine   1.15 1e-9 1.5 1e-8 120 0.001 out/tconv_fine.npz
echo "=== all done $(date +%T)"
