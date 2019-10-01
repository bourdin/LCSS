#!/usr/bin/env python
import numpy as np
import os

width = 100
height= 50
scanningSpeed=0.1
hf=0.1
hc=0.5
r=8
order=2

nl = 301
lmin = 10
lmax = 70
ll = np.linspace(lmin,lmax,nl)

nc = 100
step = 0

for l in ll[nc*step:nc*(step+1)]:
#for l in [-5,0,5]:
   cmd = "SCANNINGSPEED={0} HF={1} HC={2} WIDTH={3} HEIGHT={4} LC={5} ORDER={6} R={7} qsub ${LCSS_DIR}/LCSS_pbs.sh".format(scanningSpeed,hf,hc,width,height,l,order,r)
   print(cmd)
   os.system(cmd)
