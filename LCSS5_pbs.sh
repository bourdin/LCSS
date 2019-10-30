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
echo   ${LCSS_DIR}/LCSS_slurm.py --internalLength ${ELL} --fractureToughness ${GC} --order ${ORDER} --scanningSpeed ${SCANNINGSPEED} --hf ${HF} --hc ${HC} --width ${WIDTH} --height ${HEIGHT} --lc ${LC} --lf ${LF} --r ${R} --intensity ${INTENSITY} --initialPos 0 0 0 --finalPos 0 0 0 --time_numstep 1 --mpiexec mpirun --geofile ${LCSS_DIR}/LCSS5.geo --yamlfile ${LCSS_DIR}/LCSS5-AT1StaticHD.yaml --meshdir ${PBS_O_WORKDIR}/Meshes
echo "   "
python ${LCSS_DIR}/LCSS_slurm.py --internalLength ${ELL} --fractureToughness ${GC} --order ${ORDER} --scanningSpeed ${SCANNINGSPEED} --hf ${HF} --hc ${HC} --width ${WIDTH} --height ${HEIGHT} --lc ${LC} --lf ${LF} --r ${R} --intensity ${INTENSITY} --initialPos 0 0 0 --finalPos 0 0 0 --time_numstep 1 --mpiexec mpirun --geofile ${LCSS_DIR}/LCSS5.geo --yamlfile ${LCSS_DIR}/LCSS5-AT1StaticHD.yaml --meshdir ${PBS_O_WORKDIR}/Meshes

