#!/bin/bash
# Production runs registered in PREREG.md (sequential, one process at a time).
cd "$(dirname "$0")"
export OPENBLAS_NUM_THREADS=4 OMP_NUM_THREADS=4 MKL_NUM_THREADS=4
PY=${PY:-python3}
run() { echo "=== $(date +%T) $*"; (ulimit -v 4194304; nice -n 15 timeout 3600 $PY "$@"); echo "=== exit $?"; }
mkdir -p out
# kink L=0.6 right side
for r in 1.5 1.25 1.15; do run kink_run.py 0.6 $r 1e-40 40 n2,n3,q3/2 0,5 3 out/k06_r$r.json 0; done
# kink L=0.6 symmetric (mirror points)
for r in 1.5 1.25; do run kink_run.py 0.6 $r 1e-40 40 all1,q3/2 0,5 3 out/k06m_r$r.json 1; done
# kink L=0.8 right side
for r in 1.5 1.25 1.15; do KINK_GEN2=1e-16,1.6 run kink_run.py 0.8 $r 1e-30 40 all1,q3/2,q4/3 0,5 3 out/k08_r$r.json 0; done
# kink L=1.0 right side
for r in 1.5 1.25; do KINK_GEN2=1e-16,1.6 run kink_run.py 1.0 $r 1e-30 40 all1,q6/1 0,5 3 out/k10_r$r.json 0; done
KINK_GEN2=1e-8,2.0 run kink_run.py 1.0 1.25 1e-30 40 all1,q6/1 0,5 3 out/k10g_r1.25.json 0
# tail
for X in 8 6 10; do run tail_run.py $X fine 1.15 1e-9 1.5 1e-8 120 0.001 out/tail_X${X}_fine.npz; done
for X in 8 6 10; do run tail_run.py $X base 1.25 1e-9 2.0 1e-7 60 0.001 out/tail_X${X}_base.npz; done
echo "=== all done $(date +%T)"
