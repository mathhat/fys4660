# -*- coding: utf-8 -*-
import tqdm, sys, os, parse2
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter

N = 11
Nruns = 100
rho = 0.01
T0 = 2000
T1 = 3000
T = np.linspace(T0,T1,N)
dt = 0.001
dump_interval = 1000
run = 1000
system_size =8
thermo = ["step", "temp"]
#therm = ["without","Hoover","Berendsen"]
filename = "sw.in"

print T

for i in tqdm.trange(0,N):
        #> /dev/null
        dumpname = "equil.temp_%f"%T[i]
        os.system('mpirun -np 8 lmp_mpi -v T %f -v dt %f -v Dump %d -v Run %d -v Nruns %d -v size %d -v filename %s -v dumpname %s -in sw.in ' % (T[i],dt,dump_interval,run,Nruns,system_size,filename,dumpname))
        #foo = "diff_temp%s.log"%T
        os.system("mv %s equifiles2"%dumpname)

        #temp,msd ,time=parse2.parse(run, dump_interval,dt,thermo,system_size,foo,T)

        #plt.plot(time,119.74*temp,label= "Thermostat: %s" %therm[i])
        #msd = msd/6.
        #plt.plot(time[0:len(time)-1],msd[0:len(time)-1],label="Temp = %3.1fK"% (T*119.74) )
'''
plt.title("System initiated with different thermostats at 299Kelvin",size=16)
plt.legend(loc="best")
plt.ylabel("T[K]",size=15)
plt.xlabel(r"$t [\tau]$",size=19)    
plt.show()
'''
#parse2.parse_g()
