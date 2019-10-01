#!/usr/bin/env python
import numpy as np
import os

width = 100
height= 50
scanningSpeed=10.
hf=0.1
hc=0.5
r=8
order=2

nl = 201
lmin = 30
lmax = 50
ll = np.linspace(lmin,lmax,nl)

nc = 50
step = 0

for l in ll[nc*step:nc*(step+1)]:
   cmd = "sbatch -N 4 -n 192 -p normal -t 00:20:00 -A TG-DMS060014 ${LCSS_DIR}/LCSS_slurm.py --scanningSpeed {0} --hf {1} --hc {2} --width {3} --height {4} --lc {5} --position 0  --mpiexec ibrun --geofile ${LCSS_DIR}/LCSS2.geo --yamlfile ${LCSS_DIR}/LCSS2.yaml --meshdir ${LCSS_DIR}/Meshes --order {6} --r {7}".format(scanningSpeed,hf,hc,width,height,l,order,r)
   os.system(cmd)
   #print(cmd)

