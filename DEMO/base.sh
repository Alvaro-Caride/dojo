#!/bin/bash
#SBATCH -p <placeholder>
#SBATCH -o <placeholder>.txt
#SBATCH -N <placeholder>
#SBATCH --ntasks-per-node=<placeholder>
#SBATCH -c <placeholder>
#SBATCH -t 0:10:0
#SBATCH --mem-per-cpu=<placeholder>
# Modifica la solitud de recursos para que se ajuste a tu ejecución

source /etc/profile.d/lmod.sh

# Fijas estas variables para obtener más rendimiento
export SLURM_WHOLE=1
export OMP_NUM_THREADS=<placeholder>
export QULACS_NUM_THREADS=<placeholder>
#export OMP_PROC_BIND=<placeholder>
#numactl -N 0-3?

# Localiza el modulo y comprueba si necesitas cargar algo antes
module load <placeholder>

# Hay algo más que le puedas indicar al comando de mpirun?
time mpirun python ghz.py
