# Titan2D Scripts

This repository houses a collection of essential pre and post-processing scripts designed to streamline your experience with Titan2D simulations. Whether you're setting up runs or fine-tuning output modifications, these scripts are here to help you achieve your goals more efficiently.

These scripts are intended to assist you in two key aspects:

**Pre-Processing:**

- Generating input files with required parameters for Titan2D simulations.
- Automating the setup of simulation scenarios and initial conditions.

**Post-Processing:**

- Analyzing simulation results and generating meaningful visualizations.
- Modifying and formatting output data to match specific requirements.

## Titan2D Output

- `vizout*.xmf` file. It contains the information about the time-step at which the simulation output is stored and path to corresponding `.h5` file.
- `vizout` Dir. It contains all the simulation outputs in `.h5` format.

## Scripts

### get_field_tecplot.py

- Reads the provided `.h5` file and returns the desried output field such as momemteum, pile_height, total_erosion in  TECPLOT format.

### pileheightimage.py

- Script is a Python utility for visualizing MAX FLOW HEIGHT data. It reads data from a TITAN2D output file. It automatically extracts information about the dataset's dimensions and boundaries, and then generates a contour plot using `NumPy` and `Matplotlib`.
