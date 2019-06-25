#!/bin/bash
#PBS -A hpc_vfrac2017b
#PBS -q workq
#PBS -l nodes=10:ppn=16
#PBS -l walltime=00:30:00
#PBS -o $PBS_JOBID.out
#PBS -j oe
#PBS -N LCSS
#PBS -V

cd $PBS_O_WORKDIR
echo "now running"
echo   ../python/LCSS_slurm.py --order ${ORDER} --scanningSpeed ${SCANNINGSPEED} --hf ${HF} --hc ${HC} --width ${WIDTH} --height ${HEIGHT} --lc ${LC} --r ${R} --position 0 --mpiexec mpirun --geofile ../python/LCSS2.geo --yamlfile ../python/LCSS2.yaml --meshdir ../Meshes
echo "   "
python ../python/LCSS_slurm.py --order ${ORDER} --scanningSpeed ${SCANNINGSPEED} --hf ${HF} --hc ${HC} --width ${WIDTH} --height ${HEIGHT} --lc ${LC} --r ${R} --position 0 --mpiexec mpirun --geofile ../python/LCSS2.geo --yamlfile ../python/LCSS2.yaml --meshdir ../Meshes

