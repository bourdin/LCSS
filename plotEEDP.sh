#!/bin/bash
for d in $@; do 
    sbatch -n 1 --wrap "visit -cli -nowin -s ../python/LCSS_PNGEED.py $d/${d}_out.gen --force --output $d/${d}_out-EEDP.png      --displacementScaling 0 --damageThreshold 1. --BB -26 26 -26 26 --step 1";
    sbatch -n 1 --wrap "visit -cli -nowin -s ../python/LCSS_PNGEED.py $d/${d}_out.gen --force --output $d/${d}_out-EEDPzoom.png  --displacementScaling 0 --damageThreshold 1. --BB -20 5 -5 5    --step 1"; 
done
