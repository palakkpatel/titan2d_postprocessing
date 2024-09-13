import numpy as np
from itertools import islice
import matplotlib.pyplot as plt
import json

def make_binary(maskfile_txt : str, binary_filename : str):
    """
    Reads a mask file in text format, converts it to a binary file, and saves it. 
    A PNG visualization of the mask and a JSON file with metadata are also saved.

    Parameters:
    - maskfile_txt (str): Path to the text file containing mask data.
    - binary_filename (str): Path where the binary file will be saved.

    Returns:
    - mask_array (numpy.ndarray): 2D array representing the mask data.
    """

    with open(maskfile_txt) as f:

        # Read the metadata from the first six lines of the text file
        meta_data = {}
        for line in islice(f, 6):
            line = line.split()
            meta_data[line[0]] = int(line[1])

        print(meta_data)

        # Initialize an array for the mask data
        mask_array = np.zeros((meta_data['nrows'],meta_data['ncols']))

        # Populate the mask array with values from the file
        for k,line in enumerate(f):
            mask_array[k,:] = np.array(line.split(), dtype="int")

    # Save the mask array as a binary file
    mask_array.astype(dtype = np.int32).tofile(binary_filename)

    # Save metadata to a JSON file
    with open(binary_filename[:-4]+'_meta.json',"w") as f:
        json.dump(meta_data, f, indent=4)

    # Plot the mask array using contour and save the image
    fig, ax = plt.subplots(1,1)
    ax.contourf(mask_array[::-1], cmap = "Grays")
    ax.set_aspect("equal")
    fig.savefig(binary_filename[:-3]+'png')

    print(f"Binary File saved to {binary_filename}")

    return mask_array

def main():
    mask_file = 'example_data/wshed_mask_oaksy.txt'
    binary_mask_file = mask_file[:-3] + "bin"
    _ = make_binary(mask_file, binary_mask_file)

if __name__ == "__main__":
    main()