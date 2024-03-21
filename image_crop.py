"""
This script is used to Crop PileHeightRecord (height) and terrain data to np.array of size(nx*ny). It works on Single File as well as ensemble. 

- Palak Patel
"""

import numpy as np
import sys
import os

# Enter DEM Info
dem_name = "NOC"
nx = 7170
ny = 2999
n_sims = 100
x_range = [1, nx-1]
y_range = [91, ny-92]

print(f"Cropping for DEM : {dem_name}")
print(f"DEM Dimension (Y,X): {(ny,nx)}")
print(f"Cropping in X to : {x_range} \tLenght={x_range[1]-x_range[0]}")
print(f"Cropping in Y to : {y_range} \tLenght={y_range[1]-y_range[0]}\n")


#for i in range(98, n_sims+1):
source_dir = "sim_height_NOC_1m"
#parent_dir = f"Cropped_Data_{dem_name}"
target_dir = "elevation_data"

print(f"Source Dir: {source_dir}")
print(f"Target Dir: {target_dir}\n")

if target_dir == "height_data":
    source_image = "pileheightrecord"
elif target_dir == "elevation_data":
    source_image = "elevation"



if not os.path.exists(target_dir):
    os.mkdir(target_dir)
else:
    print(f"Target Dir: {target_dir} Exists\n Aborting")
    exit()

for i in range(1,65):
    #f1_name = 'elevation_grid_NOC/elevation_' + str(i)
    f1_name = f'{source_dir}/{source_image}_{i}'
    f1 = open(f1_name)
    x_line = f1.readline()
    y_line=f1.readline()
    tmp=f1.readline()
    x=f1.readlines()
    height = np.zeros([ny,nx])
    
    for k,line in enumerate(x):
        line = line.split('\n')[0]
        height[k] = np.float_(line.split(' '))
    
    #f1_save = 'cropped_ele_data_NOC/elevation_' +str(i)
    f1_save = f'{target_dir}/{source_image}_{i}'
    height[y_range[0]:y_range[1],x_range[0]:x_range[1]].astype(np.float32).tofile(f1_save)
    print(f"File saved to {f1_save}", end="\r")

    if len(sys.argv)==2 and sys.argv[1]=="one":
        break

print("\nDone")