#!/bin/bash
# POST-REGISTRATION diagnostic (not part of PREREG): L=1.0 with every right-side generation-2 point
# graded as deep as the generation-1 points, so that no grading truncation falls inside the fit window.
cd "$(dirname "$0")"
until grep -q "all done" prod_batch.log; do sleep 20; done
export OPENBLAS_NUM_THREADS=4 OMP_NUM_THREADS=4 MKL_NUM_THREADS=4
PY=${PY:-python3}
run() { echo "=== $(date +%T) $*"; (ulimit -v 4194304; nice -n 15 timeout 3600 $PY "$@"); echo "=== exit $?"; }
KINK_GEN2=1e-30,1.5 run kink_run.py 1.0 1.5 1e-30 40 all1,q6/1 0,5 3 out/k10d_r1.5.json 0
KINK_GEN2=1e-24,1.35 run kink_run.py 1.0 1.35 1e-24 40 all1,q6/1 0,5 3 out/k10d_r1.35.json 0
echo "=== all done $(date +%T)"
