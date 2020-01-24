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
echo mpirun vDef -prefix ${PREFIX} -options_file_yaml ${PREFIX}.yaml -time_skip ${SKIP}
cp $PREFIX_out.ener $PREFIX_out.ener.1
mpirun vDef -prefix ${PREFIX} -options_file_yaml ${PREFIX}.yaml -time_skip ${SKIP}

