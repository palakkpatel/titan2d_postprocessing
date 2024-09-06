#! /bin/bash  

# ==============================================================================
# Description: 
#   This script organizes simulation outputs from Titan2D  by  copying  specific
#   output files into a directory. It is designed to handle batch of simulations
#   and group their output files based on the simulation parameters.
#
# Usage: 
#   ./copy_titan_outputs.sh [force]
#   If 'force' is provided as an argument, the script bypasses the user prompts
#   and uses the default or predefined values for all parameters.
#
# Author: 
#   Palak Patel
# ==============================================================================

# Define simulation parameters
dem_short="" # Short identifier for the Digital Elevation Model (DEM)
field="max_height" # Field of interest from the simulation output
titan_output_file="pileheightrecord.-00001" # Titan2D output file to be copied
sim_dir_prefix="sim_" # Prefix for simulation directories
N_START=1
N_STOP=64

# If the first argument is not "force", prompt the user to confirm or modify the parameters
if [ "$1" != "force" ]
then
    echo "Modify parameters as needed or press Enter to accept the default values."

    read -p "Is dem_short = '${dem_short}': " user_input
    if [ -n "$user_input" ]; then
        dem_short=$user_input
    fi

    read -p "Is field = '${field}': " user_input
    if [ -n "$field" ]; then
        field=$user_input
    fi

    read -p "Is titan_output_file = '${titan_output_file}': " user_input
    if [ -n "$user_input" ]; then
        titan_output_file=$user_input
    fi

    read -p "Is sim_dir_prefix = '${sim_dir_prefix}': " user_input
    if [ -n "$user_input" ]; then
        sim_dir_prefix=$user_input
    fi

    read -p "Is N_START = '${N_START}': " user_input
    if [ -n "$user_input" ]; then
        N_START=$user_input
    fi

    read -p "Is N_STOP = '${N_STOP}': " user_input
    if [ -n "$user_input" ]; then
        N_STOP=$user_input
    fi
fi

# Directory to store copied files
parent_dir="${field}_${dem_short}" 


# Check if the parent directory exists, create it if not
if ! [ -d $parent_dir ]; then
    mkdir $parent_dir
    echo "Created Dir ${parent_dir}"
fi

# Loop through each simulation directory and copy the output file to the parent directory
for i in $(seq $N_START $N_STOP) 
do
    sim_dir="${sim_dir_prefix}${i}"
    echo -ne "Copying ${titan_output_file} from ${sim_dir}\n" 
    cp $sim_dir/$titan_output_file $parent_dir/"${field}_${i}"
done
