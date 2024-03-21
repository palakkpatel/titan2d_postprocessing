#! /bin/bash

dem_short="NOC_1m"
parent_dir="sim_height_${dem_short}"
if ! [ -d $parent_dir ]; then
    mkdir $parent_dir
fi

# runs=("98")
# for i in ${runs[@]}
for i in {63..64} 
do
foldername="sim_${dem_short}_${i}"
echo -ne "$foldername\r" 
cp $foldername/pileheightrecord.-00001 $parent_dir/pileheightrecord_$i
done
