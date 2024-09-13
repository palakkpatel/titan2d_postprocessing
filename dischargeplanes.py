import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

discharge_file = "example_data/discharge.csv"
multi = False

discharge_df = pd.read_csv(discharge_file)

number_of_planes = discharge_df.shape[1] - 1

plane = [0,0,0,0,0]
plane[0] = (260067.4,3815819.6,260147.4,3815819.6)
plane[1] = (260240.6,3815819.6,260320.6,3815819.6)
plane[3] = (260028.0,3815559.0,260108.0,3815559.0)
plane[2] = (260065.0,3815700.0,260145.0,3815700.0)
plane[4] = (260028.0,3815523.0,260108.0,3815523.0)
# legend = lambda x: f' \tMin\t\tMax\n' + f'X\tx[0]\tx[2]' + f'Y\tx[1]\tx[3]' 

if multi:
    fig, ax = plt.subplots(int(np.ceil(number_of_planes/3)), 3, figsize = (15, 10)) 
    for i in range(number_of_planes):
        i_row = int(i//3)
        i_col = i - i_row*3
        ax[i_row, i_col].plot(discharge_df.iloc[:,0], discharge_df.iloc[:,i+1], linewidth=3)
        ax[i_row, i_col].set_title(f'Plane {i+1}')
        # ax[i_row, i_col].legend([f'Endpoints: {legend(plane[i])}'])
        ax[i_row, i_col].set_xlabel('Time (seconds)')
        ax[i_row, i_col].set_ylabel('Discharge Volume (m3)')      

else:
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot()

    for i in range(number_of_planes):
        ax.plot(discharge_df.iloc[:,0], discharge_df.iloc[:,i+1], linewidth=3, color = (0 + 0.15*i,0.9 - 0.15*i,0.1 + 0.2*i) if i != 2 else (1,0,1), label = f'Plane {i+1}')
        # ax[i_row, i_col].legend([f'Endpoints: {legend(plane[i])}'])
    ax.set_xlabel('Time (seconds)', fontsize = 20)
    ax.set_ylabel('Discharge Volume (m3)', fontsize = 20)   
    plt.legend()
plt.tight_layout()
fig.savefig('Discharge_Plane_Vol_Plot.png', dpi = 600)



