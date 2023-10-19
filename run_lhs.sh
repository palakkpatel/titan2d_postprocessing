#! /bin/bash

filename='Latin_model_parameters_mask.txt'
n=1
n_start=61
n_stop=65
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
        foldername="sim_noAMR_${n}"
        mkdir $foldername
        mv parameters.bin $foldername/
        cd $foldername
        cp -r ../temp_sim/* ./
        sbatch titan_run.slurm
        cd ..
    fi
    #echo "Line no: $n = $line"
    n=$((n+1))
    if [ $n -gt $n_stop ]
    then
        break
    fi
done < $filename

