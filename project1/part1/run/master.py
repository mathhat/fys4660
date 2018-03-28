# -*- coding: utf-8 -*-
import tqdm, sys, os, parse 
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def OneDimReg(diff,model,time,N,d,slope0,t):
    best = sum((model-diff)**2)
    best_array=0
    for i in range(N):
        modeli = time*(slope0+i*delta)
        possible_best = sum((modeli-diff)**2)
        if possible_best < best:
            best = possible_best
            best_array = modeli
    if isinstance(best_array, np.ndarray):
        return best_array
    else:
        print "regression failed at t = ",t
        return model

N = 50
rho = 0.01  
T = 0.5
dt = 0.002
dump_interval = 50
run = 5000
system_size = 10
thermo = ["temp", "press", "pe", "ke", "etotal" ]
press=np.zeros((N+1,N+1))
#press2=np.zeros((N,N))
temp = np.linspace(0.5,3.5,N+1)
Rho = np.linspace(rho,100*rho,N+1)

for i in tqdm.trange(0,N+1):
    rho = Rho[i]
    for j in range(0,N+1):
        #t = T + i*0.01 #cmd line argument instead of T now
        t = temp[j]
        #os.system('mpirun -np 8 lmp_mpi -v rho %f -v T %f -v dt %f -v Dump %d -v Run %d -v size %d -in lj.in > /dev/null' % (rho,t,dt,dump_interval,run,system_size))
        foo="log.lammps%3.4ft%3.4fr"%(t,rho)
        #os.system("mv log.lammps %s"%foo)
        ave = parse.parse(run,dump_interval,dt,thermo,system_size,foo,t)
        press[i,j] =ave
        #press2[j,i] = ave

        #parse.parse(run,dump_interval,dt,thermo,system_size,foo,T)

    #delta = 0.02
    #n = 1000
    #diff = (diff-diff[0])
    #time = (time-time[0])
    #slope0 = diff[-1]/(time[-1])#-10
    #model = time*(slope0)
    #model = OneDimReg(diff,model,time,n,delta,slope0,t)
    
    #diffusion = model[-1]/time[-1]/6.
'''    
plt.plot(t*119.74,diffusion,'r-o')
plt.title("Diffusion as a Function of Temperature",size=17)
plt.xlabel("T [K]",size=16)
plt.ylabel(r"$D(T) [\sigma^2/\tau]$",size=21)
plt.show()

'''


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax = Axes3D(fig)
#ax = fig.gca(projection='3d')
#plt.plot(temp,press)

plt.title("Pressure as a function of both Temperature and Density")
plt.xlabel(r"$T_0$",size=21)
plt.ylabel(r"$\rho'$",size=22)
#plt.zlabel(r"$P [8.8994*10^(-6)eV/nm^2]$",size = 19)#name)
ax.set_zlabel("P'",size = 18)

X, Y = np.meshgrid(temp, Rho)



#n=np.asarray(atoms)
V=system_size**3
model_shit = Y*X/(1-Y*0.86) - 1.99*(Y)**2 #0.86 1.99

#model_shit_plot= ax.plot_surface(X,Y,model_shit)

shit = ax.plot_surface(X, Y, press,cmap=cm.hot,
                       linewidth=1, antialiased=0)
#ax.set_zlim(0.0, .11)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

#fig.colorbar(shit, shrink=0.5 , aspect=5)
plt.show()


#    print("write \"p\" or \"s\" or both after the script name in the cmd. \n p for plot, s for simulate")

