#!/bin/bash
for d in $@; do 
    sbatch -n 1 --wrap "visit -cli -nowin -s ${LCSS_DIR}/LCSS_PNGDamage.py $d/${d}_out.gen --force --output $d/${d}_out-Ref.png      --displacementScaling 0 --damageThreshold 1. --BB -26 26 -26 26 --step 1";
    sbatch -n 1 --wrap "visit -cli -nowin -s ${LCSS_DIR}/LCSS_PNGDamage.py $d/${d}_out.gen --force --output $d/${d}_out-Refzoom.png  --displacementScaling 0 --damageThreshold 1. --BB -20 15 -5 5    --step 1"; 
done
