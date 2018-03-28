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
                #for i in range(len(names)-1):
                array[1,timestep] = float(line.split()[1])
                timestep += 1
            if names[0].title() in line.split():# and len(line.split())<3:
                token += 1
            if "atoms" in line.split() and timestep < 1:
                atoms = float(line.split()[1])

    pressure = array[1,20:]
    #timesteps = timesteps[int(len(timesteps)*0.3):]

    #print len(msd), len(timesteps)
    
    
    #average_temp = sum(temperature[int(len(temperature)*0.15):])/((float(run)/dump+1)*0.85)

    average = sum(pressure)/len(pressure)

    return average #timesteps #,average_temp