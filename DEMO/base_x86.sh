#!/bin/bash
#SBATCH -p <Placeholder>
#SBATCH -o <Placeholder>
#SBATCH -N <Placeholder>
#SBATCH --ntasks-per-node=<Placeholder>
#SBATCH -c <Placeholder>
#SBATCH -t 0:10:0
#SBATCH --mem-per-cpu= <Placeholder>
# Modifica la solitud de recursos para que se ajuste a tu ejecución

# Fijas estas variables para obtener más rendimiento
export SLURM_WHOLE=1
export OMP_NUM_THREADS=<Placeholder>
export QULACS_NUM_THREADS=<Placeholder>
export OMP_PROC_BIND=<Placeholder>

# Localiza el modulo y comprueba si necesitas cargar algo antes
module load <Placeholder>
module load <Placeholder>

# Hay algo más que le puedas indicar al comando de mpirun?
time mpirun python ghz.py
