"""
Description:
    This script generates a Latin Hypercube Sample (LHS) of design points, scales 
    them according to specified minimum and maximum parameter values, and saves 
    the resulting unscaled samples to a CSV file.

Author:
    Palak Patel

Usage:
    Modify the USER DEFINED PARAMETERS section 
    to customize the number of parameters, number of simulations, and parameter 
    ranges.

    `python lhs_parameters_samples.py`
"""
#importing Libraries
import lhsmdu
import numpy as np

def generate_LHS(num_parameters, num_sims, min_parameters, max_parameters, output_file):
    """
    Generate a Latin Hypercube Sample (LHS) and save it to a file.

    This function creates a Latin Hypercube Sample (LHS) of design points, 
    scales them according to provided minimum and maximum parameter values,
    and saves the resulting unscaled samples to a specified output file.
    """
    #LHS output : Scaled from 0 - 1
    lhs = lhsmdu.sample(num_parameters,num_sims) 

    # Unscaling the LHS output
    lhs = np.array(lhs)
    lhs_unscaled = np.zeros_like(lhs)

    for i in range(num_parameters):
        diff = max_parameters[i] - min_parameters[i]
        lhs_unscaled[i] = lhs[i]*diff + min_parameters[i]
    
    np.savetxt(output_file, np.transpose(lhs_unscaled), delimiter=',')
    print(f"Output saved to {output_file}")

def main():
    """
    Main function to set up parameters and call the generate_LHS function.

    Defines user parameters, including the number of parameters, number of 
    design points, minimum and maximum values for each parameter, and the 
    output file name.
    """
    # User Defined PARAMETERS
    NUM_PARAMETERS = 6 #Number of Parameters for designed study
    NUM_SIMS = 64 #Number of Design Points
    MIN_PARA = [1.39e-6, 0, 0.03,0.005,5e-5,0.4] #List of Minimum of all parameters
    MAX_PARA = [5.56e-6,0.3,0.1,0.05,5e-4,1.5] #List of Maximum of all parameters
    OUTPUT_FILE = "LHS_model_parameters.txt"

    # Generate LHS samples and save to file
    generate_LHS(NUM_PARAMETERS, NUM_SIMS, MIN_PARA, MAX_PARA, OUTPUT_FILE)

if __name__ == "__main__":
    main()
    print("Done")


 