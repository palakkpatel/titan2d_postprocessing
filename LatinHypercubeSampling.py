import lhsmdu
import numpy as np

num_parameters = 6 #number of Parameters
num_sims = 64 # Number of DesignPoints

#LHS output : Scaled from 0 - 1
lhs = lhsmdu.sample(num_parameters,num_sims) 

# List of Minimum and Maximum of all parameters
min_para = [1.39e-6, 0, 0.03,0.005,5e-5,0.4]
max_para = [5.56e-6,0.3,0.1,0.05,5e-4,1.5]

# Unscaling the LHS output
lhs = np.array(lhs)
lhs_unscaled = lhs

for i in range(6):
    diff = max_para[i] - min_para[i]
    for j in range(num_sims):
        lhs_unscaled[i,j] = lhs[i,j]*diff + min_para[i]


#Saving Latin Hypercube File
lhs_unscaled = np.transpose(lhs_unscaled)
np.savetxt('Latin_model_parameters_mask.txt',lhs_unscaled,delimiter=',')