# -*- coding: utf-8 -*-
import parse
import tqdm, sys, os
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter

b = 5.72 #angstroms
sigma = 3.405 #angstroms
b_scaled = b/sigma
N = 1
rho = 4./(b_scaled)**3/2.
print rho
T = 1.5
dt = 0.001
dump_interval = 10
run = 10000
system_size = 20.
filename = "lj.in"
thermo = ["Step","temp"]
r1 = 20*0.174825175  #20angstrom/sigma[angstrom]
r2 = 30*0.174825175  #20angstrom/sigma[angstrom]


for i in tqdm.trange(0,N):
    #os.system('mpirun -np 8 lmp_mpi -v rho %f -v T %f -v dt %f -v Dump %d -v Run %d -v size %d -in diff.in > /dev/null' % (rho,t,dt,dump_interval,run,system_size))
    #os.system('mpirun -np 8 lmp_mpi -v r1 %f -v r2 %f -v rho %f -v T %f -v dt %f -v Dump %d -v Run %d -v size %d -v filename %s -in lj.in' % 
    #            (r1,r2,rho,T,dt,dump_interval,run,system_size,filename))
    #foo = "nameofwhateverfileyouwant"
    #os.system("mv log.lammps %s"%foo)
    foo ="log.lammps"
    temp,time=parse.parse(run, dump_interval,dt,thermo,system_size,foo,T)

plt.plot(time,temp)
plt.show()