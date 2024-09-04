#! /bin/bash  

# ==============================================================================
# Description: 
#   This script organizes simulation outputs from Titan2D  by  copying  specific
#   output files into a directory. It is designed to handle batch of simulations
#   and group their output files based on the simulation parameters.
#
# Usage: 
#   ./copy_titan_outputs.sh
#
# Author: 
#   Palak Patel
# ==============================================================================

# Define simulation parameters
dem_short="NOC_1m" # Short identifier for the Digital Elevation Model (DEM)
field="max_height" # Field of interest from the simulation output
titan_output_file="pileheightrecord.-00001" # Titan2D output file to be copied
sim_dir_prefix="sim_" # Prefix for simulation directories

N_START=1
N_STOP=64

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
    echo -ne "Copying ${titan_output_file} from ${sim_dir}\r" 
    cp $sim_dir/$titan_output_file $parent_dir/"${field}_${i}"
done
