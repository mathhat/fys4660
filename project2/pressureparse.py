import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
iterations=0
with open("master.py", "r") as my_file:
    while iterations < 20:
        iterations += 1
        line = my_file.readline().split()
        if 'dump_interval' in line:
            dump = int(line[-1])
        if 'run' in line:
            runs = int(line[-1])
timesteps = runs%dump +1
atoms = 13954
itermax = (atoms+9)*timesteps
t = 0
i = 0
press = np.zeros(atoms)
pos = np.zeros((3,atoms))
with open("dump.xyz", "r") as my_file:
    while i < itermax:
        if t:
            for atom in range(atoms):
                line = my_file.readline().split()
                pos[:,atom] =  float(line[-3]),float(line[-2]),float(line[-1])
                i += 1
        for skip in range(9):
            my_file.readline()
            i+=1
        t += 1
t = 0
i = 0
with open("press.xyz", "r") as my_file:
    while i < itermax:
        if t:
            for atom in range(atoms):
                line = my_file.readline().split()
                press[atom] = -(float(line[-3])+float(line[-2])+float(line[-1]))/3488.5
                i += 1
        for skip in range(9):
            my_file.readline()
            i+=1

        t += 1
press = np.abs(press)

for i in range(500):
    press[np.argmax(press)] /= 1.1 

for i in range(15000):

    press[np.argmin(press)] *=4


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
every=20
size = 10
scat = ax.scatter(pos[0,::every], pos[1,::every], pos[2,::every], s=size,c = press[::every], cmap=cm.coolwarm)
scatt = ax.scatter([0],[0],[0], s=1000)

plt.colorbar(scat,shrink=0.5, aspect=5)
ax.set_xlabel('X [MD]')
ax.set_ylabel('Y [MD]')
ax.set_zlabel('Z [MD]')
plt.title("Pressure Visualization at Original Density",size=25)
plt.show()