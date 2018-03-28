# -*- coding: utf-8 -*-
import tqdm, sys, os, parse2
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter

N = 11
T0 = 2000
T1 = 3000
dt = 0.001
system_size=8
T = np.linspace(T0,T1,N)
dump_interval = 500
run = 100000
thermo = ["step", "temp", "density" , "c_msd[4]"]
#therm = ["without","Hoover","Berendsen"]
filename = "DiffSi.in"
rainbow = ['r','c','m','g','b']
for i in tqdm.trange(0,N):
    #
    dumpname = "equil.temp_%f"%T[i]
    foo = "diff_temp%f.log"%T[i] #must be activated when producing msd logs!
    

    #os.system('mpirun -np 8 lmp_mpi -v T %f -v dt %f -v Dump %d -v Run %d -v dumpname %s -in %s' % (T[i],dt,dump_interval,run,dumpname,filename))
    #os.system("mv log.lammps %s"%foo) #must be activated when producing msd logs!

    temp,msd ,time=parse2.parse(run, dump_interval,dt,thermo,system_size,foo,T[i])
    msd = (msd[-1]-msd[0]) / (time[-1]-time[0])

    msd = msd/6. #m**2 per sec
    color = i%5
    plt.plot(temp,msd, '%so'%rainbow[color])#,label="Temp = %3.1fK"% temp )

plt.title("Diffusion of Si for varius temperatures",size=16)
#plt.legend(loc="best")
plt.ylabel(r"D[m$^2$/s]",size=19)
plt.xlabel("$T[K]$",size=15)    
plt.show()

#parse2.parse_g()
