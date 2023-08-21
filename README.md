# Titan2D Scripts
This repo contains all the important Pre & Post-Processing Scripts for Titan2D. This helps to setup runs and modify outputs as per requirements more efficiently. 

# Titan2D Output

- `vizout*.xmf` file. It contains the information about the time-step at which the simulation output is stored and path to corresponding `.h5` file. 
- `vizout` Dir. It contains all the simulation outputs in `.h5` format. 

## Scripts

### get_erosion_tecplot.py

- Reads the provided `.h5` file and returns the desried output field such as momemteum, pile_height, total_erosion in  TECPLOT format.