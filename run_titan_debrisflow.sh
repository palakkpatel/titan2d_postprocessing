#! /bin/bash

# Run this script in your working Dir

# Six Parameters to Update
para1=2.925e-06
para2=0.428388
para3=0.16691
para4=8.92598e-04
para5=6.90772e-05
para6=1.2558

# Number of Processors to Run
NPROCS=8

# Path to Titan
export titan="/cluster/tufts/patralab/ppatel20/titan2d/titan_wsp/titan2d_bld/iccoptompmpi/bin/titan"

#Path to model_parameters.py
model_parameters="../model_parameters.py"

# Run model_parameters.py
python3 $model_parameters $para1 $para2 $para3 $para4 $para5 $para6

# Run Titan2d
NOW=`date`
echo "Simulation Starting Time: "$NOW
echo "====================================================="
$titan -nt $NPROCS input.py
echo "*****************************************************"
NOW=`date`
echo "Simulation Ending Time: "$NOW
echo "Done"


