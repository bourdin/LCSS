#PBS -A hpc_vfrac2017c
#PBS -q workq
#PBS -l walltime=06:00:00
#PBS -o $PBS_JOBID.out
#PBS -j oe
#PBS -N LCSS6
#PBS -V
if [ -f ${HOME}/cubitenv.sh ]; then
    source ${HOME}/cubitenv.sh
fi
cd $PBS_O_WORKDIR
echo "now running"
echo ${LCSS_DIR}/LCSS_slurm.py --internalLength ${ELL} --fractureToughness ${GC} --order 1 --hf ${HF} --hc ${HC} --width ${WIDTH} --height ${HEIGHT} --lc ${LC} --lf ${LF} --r ${R} --intensity ${INTENSITY} --initialPos ${X0} 0 0 --finalPos ${XF} 0 0 --time_min ${TMIN} --time_max ${TMAX} --time_numstep ${NSTEP} --mpiexec mpirun --geofile ${LCSS_DIR}/LCSS7.jou --yamlfile ${LCSS_DIR}/${YAMLFILE} --meshdir ${PBS_O_WORKDIR}/Meshes 
echo "   "
${LCSS_DIR}/LCSS_slurm.py --internalLength ${ELL} --fractureToughness ${GC} --order 1 --hf ${HF} --hc ${HC} --width ${WIDTH} --height ${HEIGHT} --lc ${LC} --lf ${LF} --r ${R} --intensity ${INTENSITY} --initialPos ${X0} 0 0 --finalPos ${XF} 0 0 --time_min ${TMIN} --time_max ${TMAX} --time_numstep ${NSTEP} --mpiexec mpirun --geofile ${LCSS_DIR}/LCSS7.jou --yamlfile ${LCSS_DIR}/${YAMLFILE} --meshdir ${PBS_O_WORKDIR}/Meshes 


