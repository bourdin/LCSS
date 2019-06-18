#!/bin/bash
#PBS -A hpc_vfrac2017b
#PBS -q workq
#PBS -l nodes=2:ppn=16
#PBS -l walltime=06:00:00
#PBS -o $PBS_JOBID.out
#PBS -j oe
#PBS -N LCSS
#PBS -V

cd $PBS_O_WORKDIR
../python/LCSS_slurm.py --order ${ORDER} --scanningSpeed ${SCANNINGSPEEG} --hf ${HF} --hc ${HC} --width ${WIDTH} --height ${HEIGHT} --lc ${LC} --position 0  --postprocess --mpiexec mpirun --geofile ../python/LCSS2.geo --yamlfile ../python/LCSS.yaml --meshdir ../Meshes --forcemesh