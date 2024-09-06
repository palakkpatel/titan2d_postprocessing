from itertools import islice

def discharge_output_csv(num_planes : int, discharge_output_file : str, discharge_csv_file : str):
    """
    Converts Titan2D simulation discharge output into a CSV format.
    This function skips the header lines in the discharge output file, based on the number of planes.
    It then writes the discharge data into a CSV file with the first column as 'Time' and the subsequent 
    columns for each plane labeled 'Plane_1', 'Plane_2', etc.

    Args:
        num_planes (int): Number of planes in the simulation.
        discharge_output_file (str): Path to the discharge output file (usually '.out' format).
        discharge_csv_file (str): Path to save the resulting CSV file.
    """
    # Calculate the number of lines to skip (headers and metadata). The number of planes affects this.
    num_skip_lines = (num_planes + 2)*2

    # Open the output CSV file for writing  
    with open(discharge_csv_file, "w") as out_file:

        # Write the CSV header: 'Time,Plane_1,Plane_2,...'
        out_file.write('Time,' + ','.join([f"Plane_{i}" for i in range(1, num_planes+1)]) + '\n')

        # Open the discharge output file for reading and skip the necessary header lines
        with open(discharge_output_file) as f:
            for line in islice(f,num_skip_lines, None): # Skip lines and process the data
                out_file.write(','.join(line.split())+'\n')
    
def main():
    """
    Main function to convert discharge output file to CSV format.
    
    Defines the number of planes, input file, and output CSV file paths, 
    then calls the conversion function.
    """
    # Path to the example discharge output file and number of planes
    discharge_output_file = "example_data/discharge.out"
    num_planes = 3  # Specify the number of planes in the simulation
    
    # Generate the CSV filename by replacing the '.out' extension with '.csv'
    discharge_csv_file = discharge_output_file[:-3] + "csv"
    
    # Convert the discharge output to CSV format
    discharge_output_csv(num_planes, discharge_output_file, discharge_csv_file)
    print("Conversion Complete")

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()

