#! /bin/bash

# Update User Define Parameters
PARAMETER_DESIGN_FILE='Latin_model_parameters_mask.txt'
SIM_START_N=61 # Starting Simulation Number from the File
SIM_STOP_N=65 # Last Simulation to run (inclusive)

# Simulation Template DIR
temp_sim="../temp_sim"

# Simulation DIR Prefix
SIM_DIR_PREFIX="sim"

# Slurm File Name
SLURM_FILE_PATH="titan_run.slurm"

# Path to model_parameters.py
model_parameters="../model_parameters.py"

n=1
# Looping over Parameter Design File
while read line; do
    line=$(echo $line | sed 's/\,/ /g')
    para1=$(echo $line | awk '{print $1}')
    para2=$(echo $line | awk '{print $2}')
    para3=$(echo $line | awk '{print $3}')
    para4=$(echo $line | awk '{print $4}')
    para5=$(echo $line | awk '{print $5}')
    para6=$(echo $line | awk '{print $6}')

    if [ $n -gt $((SIM_START_N-1)) ]
    then
        # Exceuting Model Parameters File 
        python $model_parameters $para1 $para2 $para3 $para4 $para5 $para6
        sim_dir_name="${SIM_DIR_PREFIX}_${n}"
        mkdir $sim_dir_name
        mv parameters.bin $sim_dir_name/
        cd $sim_dir_name
        cp -r $temp_sim/* ./
        sbatch $SLURM_FILE_PATH
        cd ..
    fi

    n=$((n+1))
    if [ $n -gt $SIM_STOP_N ]
    then
        break
    fi
done < $PARAMETER_DESIGN_FILE

echo "Done"