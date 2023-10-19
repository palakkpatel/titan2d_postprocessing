#!/bin/bash
#SBATCH --account=normal
#SBATCH --job-name=sanysidro
#SBATCH --output=run.out
#SBATCH --error=run.err
#SBATCH --nodes=1
##SBATCH --cpus-per-task=1
##SBATCH --exclusive
##SBATCH --partition=patralab
#SBATCH --qos=normal
#SBATCH --constraint=rhel7
#SBATCH --mem=64g
#SBATCH --ntasks-per-node=32
#SBATCH --time=3600

echo "SLURM_JOBID="$SLURM_JOBID
echo "SLURM_JOB_NODELIST"=$SLURM_JOB_NODELIST
echo "SLURM_NNODES"=$SLURM_NNODES
echo "SLURMTMPDIR="$SLURMTMPDIR
echo "Working Directory="$SLURM_SUBMIT_DIR
NPROCS=`srun --nodes=${SLURM_NNODES} bash -c 'hostname' |wc -l`
echo "NPROCS="$NPROCS
echo $LD_LIBRARY_PATH
module load gcc/9.3.0
echo $LD_LIBRARY_PATH
export OMP_NUM_THREADS=$NPROCS
export titan=/cluster/tufts/patralab/ppatel20/titan2d/titan_wsp/titan2d_bld/iccoptompmpi/bin/titan

NOW=`date`
echo "Simulation Starting Time: "$NOW
echo "====================================================="
$titan -nt 32 input_2piles.py
echo "*****************************************************"
NOW=`date`
echo "Simulation Ending Time: "$NOW
echo "Done"


