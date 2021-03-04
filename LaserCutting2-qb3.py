#!/usr/bin/env python
#SBATCH -A loni_vfrac2021
#SBATCH -p workq
###SBATCH -N 8 
#SBATCH -n 576
###SBATCH -c 1
#SBATCH -t 72:00:00
#SBATCH -o %j.out
#SBATCH -e %j.err
#SBATCH -J LaserCutting



import sys
import json
import os

#os.system("printenv")
os.chdir(os.getenv("SLURM_SUBMIT_DIR"))
jobid = os.getenv("SLURM_JOBID")
D = json.load(open("00_INFO.json"))
lcssdir = os.getenv("LCSS_DIR")


if not 'skip' in D.keys():
    D['skip'] = 0
if D['skip'] == 0:
    # we do a first computation with only heat transfer
    cmd1 = "{lcssdir}/LCSS_flux4.py -i {geometry:s} -o {result:s} --pathfile {pathfile:s} --cs 1 2 --d {d:.4e} --alpha {alpha:.4e} --r0 {r0:.4e}  --x0 {x0:.4e} --t0 {t0:.4e}  --dt {dt:.4e} --force | tee {jobid:s}.txt".format(jobid=jobid,lcssdir=lcssdir,**D)
    cmd2 = "srun -N {N} -n {n} HeatXfer -geometry {geometry:s} -result {result:s} -options_file_yaml {yamlfile:s} | tee -a {jobid:s}-heatXfer.txt".format(N=os.getenv("SLURM_NNODES"),n=os.getenv("SLURM_NTASKS"),jobid=jobid,**D)
    cmd3 = "srun -N {N} -n {n} vDef     -geometry {geometry:s} -result {result:s} -options_file_yaml {yamlfile:s} -cs0001_temp_BC yes -cs0002_temp_BC yes| tee -a {jobid:s}-vDef.txt".format(N=os.getenv("SLURM_NNODES"),n=os.getenv("SLURM_NTASKS"),jobid=jobid,**D)
    print(cmd1)
    os.system(cmd1)
    print(cmd2)
    os.system(cmd2)
    print(cmd3)
    os.system(cmd3)
else:
    # We save the energy file and resume the computation:
    prefix = os.path.splitext(D['result'])[0]
    for i in range(50):
        print ('looking for {0:s}.ener'.format(prefix), os.path.exists('{0:s}.ener'.format(prefix)) and not os.path.exists('{0:s}-{1:04d}.ener \n'.format(prefix,i)))
        if os.path.exists('{0:s}.ener'.format(prefix)) and not os.path.exists('{0:s}-{1:04d}.ener'.format(prefix,i)):
            cmd = 'mv {0:s}.ener {0:s}-{1:04d}.ener'.format(prefix,i)
            print(cmd)
            os.system(cmd)
            cmd3 = "srun -N {N} -n {n} vDef -geometry {geometry:s} -result {result:s} -options_file_yaml {yamlfile:s} -cs0001_temp_BC yes -cs0002_temp_BC yes -time_skip {skip:d} | tee -a {jobid:s}-vDef.txt".format(N=os.getenv("SLURM_NNODES"),n=os.getenv("SLURM_NTASKS"),jobid=jobid,**D)
            print(cmd3)
            os.system(cmd3)
            break



