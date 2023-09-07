# Convert Last step erosion data into TECPLOT data file

import sys
import h5py
import numpy as np

sim = int(sys.argv[1])
field = sys.argv[2]
#erosion_file = 'total_erosion/vizout_' + str(sim) +'.h5'
erosion_file = 'vizout_' + str(sim) +'.h5'
f = h5py.File(erosion_file,'r')

erosion = f['Properties'][field][()]
mesh = f['Mesh']['Points'][()]
face = f['Mesh']['Connections']
face_centroid=mesh[face].mean(axis=1)
face_centroid=face_centroid[:,:2]

face_min = face_centroid.min(axis=0)
y_number = len(face_centroid[abs(face_centroid[:,0] - face_min[0]) < 1e-5])
x_number = len(face_centroid[abs(face_centroid[:,1] - face_min[1]) < 1e-5])
f.close()

filename = field + '_' + str(sim) + '.dat'
f = open(filename, "w")
f.write(f'VARIABLES = "X" "Y" "{field}"\n')
f.write(f'ZONE T = "{field}"\n')
f.write('\tI=%d, J=%d\n'%(x_number,y_number))
for i in range(len(face_centroid)):
    f.write('\t%.4f\t%.4f\t%.6f\n'%(face_centroid[i,0],face_centroid[i,1],erosion[i]))


exit()

'''
erosion_arr = np.zeros((y_number, x_number))
X = erosion_arr
Y = erosion_arr
for i in range(x_number):
    for j in range(y_number):
        X[j,i] = 
'''





#/home/palak/thomaswildfire_titan/sim_16/vizout/xdmf_p0000_i00049000.h5
