#!/bin/bash
for d in $@; do 
    sbatch --wrap "visit -cli -nowin -s ${LCSS_DIR}/LCSS_CrackLength.py ${d}/${d}_out.gen --out ${d}/${d}_out-crackLength.txt --force --step 1"
done
