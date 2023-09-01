import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker, cm, colors
import sys

filename = sys.argv[1]

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

height = np.zeros([ny,nx])
for k,line in enumerate(x):
    line = line.split('\n')[0]
    height[k] = np.float_(line.split(' '))
min_height = 10
max_height = 10e-5
for i in range(np.shape(height)[0]):
    for j in range(np.shape(height)[1]):
        if height[i,j] > max_height:
            max_height = height[i,j]
        elif height[i,j] < 10e-5:
            height[i,j] = 10e-5

print('Max Height', max_height)
print('Min Height', min_height)


x = np.linspace(x_min,x_max,nx)
y = np.linspace(y_min,y_max,ny)

[X,Y]=np.meshgrid(x,y)


locator=None
ticks = np.linspace(0, 4, 10)

fig, ax = plt.subplots()
img = ax.contourf(X, Y, height, 
                locator=locator, 
                levels = 100,
                cmap='coolwarm')

ax.set_xticks(np.linspace(x_min + 0.1*(x_max - x_min), x_max - 0.1*(x_max - x_min),3))
#ax.set_xticklabels(rotation = 45)
plt.xticks(rotation = 0, fontsize= 8)
plt.yticks(rotation = 0, fontsize= 8)
#plt.title(filename.split('_')[0].upper() + "_" + filename.split('_')[1].capitalize())
ax.set_ylabel('UTM North (m)')
ax.set_xlabel('UTM East (m)')
plt.xlim(x[0], x[-1])
plt.gca().set_aspect('equal', adjustable='box')
plt.margins(x=0)
cbar = fig.colorbar(img, ticks = ticks)
cbar.set_label('Max Flow Depth (m)')

plt.savefig(filename + '.png',format='png',dpi=720, bbox_inches='tight')
