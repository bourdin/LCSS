#!/bin/bash
#PBS -A hpc_vfrac2017b
#PBS -q workq
#PBS -l nodes=10:ppn=16
#PBS -l walltime=02:00:00
#PBS -o $PBS_JOBID.out
#PBS -j oe
#PBS -N LCSS
#PBS -V

cd $PBS_O_WORKDIR
echo "now running"
echo   ../python/LCSS_slurm.py --internalLength ${ELL} --fractureToughness ${GC} --order ${ORDER} --scanningSpeed ${SCANNINGSPEED} --hf ${HF} --hc ${HC} --width ${WIDTH} --height ${HEIGHT} --lc ${LC} --lf ${LF} --r ${R} --intensity ${INTENSITY} --position 0 --mpiexec mpirun --geofile ../python/LCSS4.geo --yamlfile ../python/LCSS4-AT1StaticHD.yaml --meshdir ../Meshes
echo "   "
python ../python/LCSS_slurm.py --internalLength ${ELL} --fractureToughness ${GC} --order ${ORDER} --scanningSpeed ${SCANNINGSPEED} --hf ${HF} --hc ${HC} --width ${WIDTH} --height ${HEIGHT} --lc ${LC} --lf ${LF} --r ${R} --intensity ${INTENSITY} --position 0 --mpiexec mpirun --geofile ../python/LCSS4.geo --yamlfile ../python/LCSS4-AT1StaticHD.yaml --meshdir ../Meshes

