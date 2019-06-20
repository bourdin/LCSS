#!/usr/bin/env python
import numpy as np
import os

width = 100
height= 50
scanningSpeed=5.0
#hf=0.025 
#hc=1.0
#order=1
hf=0.05 
hc=2.0
order=2
numl=101

for l in np.linspace(30,50,numl):
   cmd = "SCANNINGSPEED={0} HF={1} HC={2} WIDTH={3} HEIGHT={4} LC={5} ORDER={6} qsub ../python/LCSS_pbs.sh".format(scanningSpeed,hf,hc,width,height,l,order)
   print(cmd)
   os.system(cmd)
