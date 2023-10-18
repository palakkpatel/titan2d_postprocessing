from array import array
import sys

# ks = 1.389e-6
# manning = 0.05
# lambda_basal=0.6
# F = 0.008
# DS = 1e-5

ks = float(sys.argv[1])
manning = float(sys.argv[2])
lambda_basal = float(sys.argv[3])
F = float(sys.argv[4])
DS = float(sys.argv[5])
R_coef = float(sys.argv[6])

#print(type(ks))
para=[ks, manning, lambda_basal, F, DS, R_coef]
print(para)
para_array = array('d', para)
with open('parameters.bin','wb') as f:
    para_array.tofile(f)

