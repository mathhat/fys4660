# -*- coding: utf-8 -*-
import tqdm, sys, os, parse2
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter

N = 3
rho = 0.01
T = 2.5
dt = 0.001
dump_interval = 200
run = 200000
system_size = 10
thermo = ["step", "temp"]
therm = ["without","Hoover","Berendsen"]


for i in tqdm.trange(0,N):
    #os.system('mpirun -np 8 lmp_mpi -v rho %f -v T %f -v dt %f -v Dump %d -v Run %d -v size %d -in diff.in > /dev/null' % (rho,t,dt,dump_interval,run,system_size))
    #os.system('mpirun -np 8 lmp_mpi -v rho %f -v T %f -v dt %f -v Dump %d -v Run %d -v size %d -in diff.in' % (rho,T,dt,dump_interval,run,system_size))
    foo = "temp_%s.log"%therm[i]
    #os.system("mv log.lammps %s"%foo)

    temp,time=parse2.parse(run, dump_interval,dt,thermo,system_size,foo,T)

    plt.plot(time,119.74*temp,label= "Thermostat: %s" %therm[i])
    #msd = msd/6.
    #plt.plot(time[0:len(time)-1],msd[0:len(time)-1],label="Temp = %3.1fK"% (T*119.74) )
    #T += 1./119.74
plt.title("System initiated with different thermostats at 299Kelvin",size=16)
plt.legend(loc="best")
plt.ylabel("T[K]",size=15)
plt.xlabel(r"$t [\tau]$",size=19)    
plt.show()

#parse2.parse_g()
