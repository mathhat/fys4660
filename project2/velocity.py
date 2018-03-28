from matplotlib.pyplot import *
import numpy as np
atoms = 0
with open("dump.xyz", "r") as my_file:
    for line in my_file:
        if 'ATOMS' in line.split():
            atoms = int(my_file.readline().split()[0])
            break
iterations = 0 #only have to read first 10 lines of the script to know the timesteps

with open("lj.in", "r") as my_file:
    while iterations < 14:
        iterations += 1
        line = my_file.readline().split()
        if 'dump' in line:
            dump = int(line[-1])
        if 'run' in line:
            runs = int(line[-1])
        if 'time' in line and len(line)>3:
            timestep = float(line[-1])
timesteps = int(runs/dump)+1

itermax = (atoms+9)*timesteps
t = 0
i = 0
velocities = np.zeros((timesteps,atoms))
with open("dump.xyz", "r") as my_file:
    while i < itermax:
        for skip in range(9):
            my_file.readline()
            i+=1
        for atom in range(atoms):
            line = my_file.readline().split()
            velocities[t,atom] = float(line[-3])#*float(line[-1]) +  #np.sqrt(
                                #float(line[-2])*float(line[-2]) + 
                                #float(line[-3])*float(line[-3]))
            i += 1
        t += 1

for i in range(0,timesteps,int(timesteps/5)):
    hist(velocities[i,:], bins= atoms/40,weights=np.ones_like(velocities[i,:])/len(velocities[i,:]))#int(timesteps/10))  # arguments are passed to np.histogram
    ylabel("P(V)",size=16)
    xlabel(r"V(x) [$\sigma/\tau$]",size=16)
    title(r"P(V(x)) distribution at time $\tau$ = %s"% str(i*dump*timestep),size = 18)  # arguments are passed to np.histogram
    show()
