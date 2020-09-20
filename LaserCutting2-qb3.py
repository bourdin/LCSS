#!/usr/bin/env python
#SBATCH -N 7
#SBATCH -p workq
#SBATCH -A loni_vfrac2020
#SBATCH -J LaserCutting2D

import sys
import json
import os

os.chdir(os.getenv("SLURM_SUBMIT_DIR"))
jobid = os.getenv("SLURM_JOB_ID")
D = json.load(open("00_INFO.json"))
lcssdir = os.getenv("LCSS_DIR")
nnodes = os.getenv("SLURM_NNODES")
ntasks = os.getenv("SLURM_NTASKS")

cmd1 = "{lcssdir}/LCSS_flux4.py -i {geometry:s} -o {result:s} --pathfile {pathfile:s} --cs 1 2 --d {d:.4e} --alpha {alpha:.4e} --r0 {r0:.4e}  --x0 {x0:.4e} --t0 {t0:.4e}  --dt {dt:.4e} --force | tee {jobid:s}.txt".format(jobid=jobid,lcssdir=lcssdir,**D)
cmd2 = "srun -N {nnodes} -n {ntasks} vDef -geometry {geometry:s} -result {result:s} -options_file_yaml {yamlfile:s} | tee {jobid:s}.txt".format(nnodes = nnodes,ntasks=ntasks,jobid=jobid,**D)
print(cmd1)
os.system(cmd1)
print(cmd2)
os.system(cmd2)


