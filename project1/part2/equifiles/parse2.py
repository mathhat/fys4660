import numpy as np
from matplotlib.pyplot import*
import string
import re
pattern = re.compile('[\W_]+')

def parse(run, dump,time,names,size,log,T):
    token = 0
    timestep = 0
    timesteps = np.linspace(0,time*int(run)+1,int(run/dump)+1)
    array = np.zeros((len(names),len(timesteps)))

    with open(log, "r") as my_file:
        while timestep < run/dump+1:
            line = my_file.readline()
            if token:
                for i in range(len(names)):
                    array[i,timestep] = float(line.split()[i])
                timestep += 1
            if str(names[0].title()) in line.split():# and len(line.split())<3:
                token += 1
            #if "atoms" in line.split():
            #    atoms = float(line.split()[1])
    
    msd = array[-1]#,int(len(array[-1,:])*0.5):]
    #timesteps = timesteps[int(len(array[-1,:])*0.5):]
    #h=timesteps[1]
    #for i in range(len(msd)-2):
    #    msd[i+1]= (msd[i+2]-msd[i+1])/h
    #print len(msd), len(timesteps)
    temp = array[-2]#,int(len(array[-1,:])*0.3):]
    temp = sum(temp)/len(temp)
    
    #average_temp = sum(temperature[int(len(temperature)*0.15):])/((float(run)/dump+1)*0.85)

    #average = sum(pressure[int(len(pressure)*0.15):])/((float(run)/dump+1)*0.85)
    

    return temp, msd,timesteps
'''
def parse_g():
    bins = np.zeros((2,100))
    for i in range(1,21):
        with open("%d.txt"%i,'r') as muhfile:
            muhfile.readline()
            muhfile.readline()
            muhfile.readline()
            for j in range(100):
                line = muhfile.readline().split()
                bins[0,j] = float(line[1])
                bins[1,j] += float(line[2])
    bins[1,:] /= 20.
    plot(bins[1])
    title("RDF of solid system with 4000 atoms and sides of 10 sigma")
    ylabel("g(r)",size=16)
    xlabel("r [?]",size=16)
    show()
    return 0 
'''