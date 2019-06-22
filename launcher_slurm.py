#!/usr/bin/env python
import numpy as np
import os

width = 100
height= 50
scanningSpeed=1.0
hf=0.025 
hc=1.0

for l in np.linspace(30,70,201):
   cmd = "sbatch -n 36 ../python/LCSS_slurm.py --scanningSpeed {0} --hf {1} --hc {2} --width {3} --height {4} --lc {5} --position 0  --postprocess --mpiexec srun --geofile ../python/LCSS2.geo --yamlfile ../python/LCSS.yaml --meshdir ../Meshes --forcemesh ".format(scanningSpeed,hf,hc,width,height,l)
   #os.system(cmd)
   print(cmd)

