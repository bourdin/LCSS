#PBS -V
cd $PBS_O_WORKDIR
echo "now running"
echo   ${LCSS_DIR}/LCSS_slurm.py --internalLength ${ELL} --fractureToughness ${GC} --order ${ORDER} --scanningSpeed ${SCANNINGSPEED} --hf ${HF} --hc ${HC} --width ${WIDTH} --height ${HEIGHT} --lc ${LC} --lf ${LF} --r ${R} --intensity ${INTENSITY} --initialPos ${X0} 0 0 --finalPos ${XF} 0 0 --time_numstep ${NSTEP} --mpiexec mpirun --geofile ${LCSS_DIR}/LCSS6.geo --yamlfile ${LCSS_DIR}/LCSS5-AT1StaticHD.yaml --meshdir ${PBS_O_WORKDIR}/Meshes
echo "   "
python ${LCSS_DIR}/LCSS_slurm.py --internalLength ${ELL} --fractureToughness ${GC} --order ${ORDER} --scanningSpeed ${SCANNINGSPEED} --hf ${HF} --hc ${HC} --width ${WIDTH} --height ${HEIGHT} --lc ${LC} --lf ${LF} --r ${R} --intensity ${INTENSITY} --initialPos ${X0} 0 0 --finalPos ${XF} 0 0 --time_numstep ${NSTEP} --mpiexec mpirun --geofile ${LCSS_DIR}/LCSS6.geo --yamlfile ${LCSS_DIR}/LCSS5-AT1StaticHD.yaml --meshdir ${PBS_O_WORKDIR}/Meshes

#python ${LCSS_DIR}/LCSS_slurm.py --internalLength ${ELL} --fractureToughness ${GC} --order ${ORDER} --scanningSpeed ${SCANNINGSPEED} --hf ${HF} --hc ${HC} --width ${WIDTH} --height ${HEIGHT} --lc ${LC} --lf ${LF} --r ${R} --intensity ${INTENSITY} --initialPos ${X0} 0 0 --finalPos ${XF} 0 0 --time_numstep ${NSTEP} --mpiexec mpirun --geofile ${LCSS_DIR}/LCSS6.geo --yamlfile ${LCSS_DIR}/LCSS5-AT1StaticHD.yaml --meshdir ${PBS_O_WORKDIR}/Meshes

