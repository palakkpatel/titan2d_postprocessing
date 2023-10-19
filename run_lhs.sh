#! /bin/bash

filename='Latin_model_parameters_mask.txt'

n=1

# Starting Simulation Number from the File
n_start=61

# Last Simulation to run (inclusive)
n_stop=65

# Simulation Template DIR
temp_sim="../temp_sim"

# Simulation DIR Prefix
sim_dir="sim_noAMR"

# Slurm File Name
slurm_file = "titan_run.slurm"


while read line; do
    line=$(echo $line | sed 's/\,/ /g')
    para1=$(echo $line | awk '{print $1}')
    para2=$(echo $line | awk '{print $2}')
    para3=$(echo $line | awk '{print $3}')
    para4=$(echo $line | awk '{print $4}')
    para5=$(echo $line | awk '{print $5}')
    para6=$(echo $line | awk '{print $6}')

    if [ $n -gt $((n_start-1)) ]
    then
        python3 model_parameters.py $para1 $para2 $para3 $para4 $para5 $para6
        foldername="${sim_dir}_${n}"
        mkdir $foldername
        mv parameters.bin $foldername/
        cd $foldername
        cp -r $temp_sim/* ./
        sbatch $slurm_file
        cd ..
    fi
    #echo "Line no: $n = $line"
    n=$((n+1))
    if [ $n -gt $n_stop ]
    then
        break
    fi
done < $filename

