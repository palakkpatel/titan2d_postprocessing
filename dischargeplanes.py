import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

discharge_file = "example_data/discharge.csv"

discharge_df = pd.read_csv(discharge_file)

fig, ax = plt.subplots(1, 3, fig_size = (4, 12))

plane = [0,0,0]
plane[0] = (260067.4,3815819.6,260147.4,3815819.6)
plane[1] = (260240.6,3815819.6,260320.6,3815819.6)
plane[2] = (260028.0,3815559.0,260108.0,3815559.0)

for i in range(3):
    ax[i].plot(discharge_df.iloc[:,0],discharge_df.iloc[:,i+1], label = f'Plane {i+1} : {plane[i]}')

plt.tight_layout()
plt.show()



