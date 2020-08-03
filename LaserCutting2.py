#!/usr/bin/env python
#PBS -A hpc_vfrac2017c
#PBS -q workq
#PBS -l nodes=4:ppn=16
#PBS -l walltime=12:00:00
#PBS -o $PBS_JOBID.out
#PBS -j oe
#PBS -N LaserCutting
#PBS -V


import sys
import json
import os

os.chdir(os.getenv("PBS_O_WORKDIR"))
jobid = os.getenv("PBS_JOBID")
D = json.load(open("00_INFO.json"))
lcssdir = os.getenv("LCSS_DIR")

cmd1 = "{lcssdir}/LCSS_flux4.py -i {geometry:s} -o {result:s} --pathfile {pathfile:s} --cs 1 2 --d {d:.4e} --alpha {alpha:.4e} --r0 {r0:.4e}  --x0 {x0:.4e} --t0 {t0:.4e}  --dt {dt:.4e} --force | tee {jobid:s}.txt".format(jobid=jobid,lcssdir=lcssdir,**D)
cmd2 = "mpirun vDef -geometry {geometry:s} -result {result:s} -options_file_yaml {yamlfile:s} | tee {jobid:s}.txt".format(jobid=jobid,**D)
print(cmd1)
os.system(cmd1)
print(cmd2)
os.system(cmd2)


