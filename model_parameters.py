"""
Description:
    This script takes six numerical input parameters from the command line and writes them to a binary file. 
    The script converts the input parameters into a list, then into an array of double precision floats, 
    and finally writes the array to a binary file named 'parameters.bin'.

Author:
    Palak Patel

Usage:
    `python model_parameters.py value1 value2 value3 value4 value5 value6`
"""

#Importing Libraries
import sys
from array import array

# Parse input arguments and convert them to float
ks = float(sys.argv[1])
manning = float(sys.argv[2])
lambda_basal = float(sys.argv[3])
F = float(sys.argv[4])
DS = float(sys.argv[5])
R_coef = float(sys.argv[6])

# Store parameters in a list
parameters = [ks, manning, lambda_basal, F, DS, R_coef]
print(parameters)

# Convert list to array of type 'double'
parameters_array = array('d', parameters)

# Write the array to a binary file
output_file = 'parameters.bin'
with open(output_file, 'wb') as file:
    parameters_array.tofile(file)

print(f"Parameters successfully written to {output_file}")
