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
atoms = 6980
itermax = (atoms+9)*timesteps
t = 0
i = 0
press = np.zeros(atoms)
pos = np.zeros((3,atoms))
vel = np.zeros((3,atoms))
with open("flow_station.xyz", "r") as my_file:
    while i < itermax:
        if t:
            for atom in range(atoms):
                line = my_file.readline().split()
                pos[:,atom] =  float(line[-6]),float(line[-5]),float(line[-4])
                vel[:,atom] =  float(line[-3]),float(line[-2]),float(line[-1])
                i += 1
        for skip in range(9):
            my_file.readline()
            i+=1
        t += 1

size = 42.3304
dist_to_axis = size/2

for i in range(1,3):
    pos[i] = pos[i] - dist_to_axis
for i in range(1,3):
    pos[i] = (pos[i]*pos[i])    #calculate r from x axis
pos[0] = np.sqrt(pos[1]+pos[2]) #replace x pos with distance from x axis

definition = 1000+1 #how many layers
t = 2 #threshold + - this distance
rrange = np.linspace(min(pos[0])+t,max(pos[0])-t,definition)
u = []
for dist in rrange:
    count = 0
    mean = 0
    for i in range(len(pos[0])):
        if (dist - t) < pos[0,i] < (dist +t):
            count += 1
            mean += vel[0,i]
    u.append( mean/float(count))
du = []
dr = 1#rrange[1]-rrange[0]
for i in range(len(u)-1):
    du.append((u[i+1]-u[i])/dr)
plt.plot(rrange,u)
plt.plot(rrange[:-(1+len(du)/3)],du[:-(len(du)/3)])
plt.show()
