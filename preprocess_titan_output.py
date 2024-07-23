import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker, cm, colors
import sys
import joblib

def read_output_file(filename, output_filename = None):
    """Creates Joblib file for Numpy array storage of size (Ny,Nx)"""
    f1 = open(filename)

    x_line = f1.readline()
    y_line=f1.readline()

    nx=int(x_line.split(':')[0].split('=')[1])
    x_min=float(x_line.split(':')[1].split(",        ")[0].split("         ")[1])
    x_max=float(x_line.split(':')[1].split(",         ")[1].split('}')[0])

    ny=int(y_line.split(':')[0].split('=')[1])
    y_min=float(y_line.split(':')[1].split(",        ")[0].split("        ")[1])
    y_max=float(y_line.split(':')[1].split(",        ")[1].split('}')[0])

    print(x_min, x_max, y_min, y_max)

    f1.readline()
    x=f1.readlines()

    field = np.zeros([ny,nx])
    for k,line in enumerate(x):
        line = line.split('\n')[0]
        field[k] = np.float_(line.split(' '))
    
    min_field = float("inf")
    max_field = float("-inf")

    for i in range(np.shape(field)[0]):
        for j in range(np.shape(field)[1]):
            if field[i,j] > max_field:
                max_field = field[i,j]
            elif field[i,j] < min_field:
                min_field = field[i,j]

    if output_filename is None:
        output_filename = f"{filename}_Nx_{nx}_Ny_{ny}.joblib"
    
    joblib.dump(field, output_filename)
    print(f"Array saved to {output_filename}")

if __name__ == "__main__":
    #Provide Filename in Argument"
    filename = sys.argv[1]
    read_output_file(filename=filename)
    print("Done")







    