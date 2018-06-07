import numpy as np 
import matplotlib.pyplot as plt 

schi = []
pc = 0.59275
pn = 8
p = np.linspace(pc-0.04,pc,pn)
with open("data.txt","r") as fil:
    schi = fil.readline().split()
    for i in range(pn-2): #lacking pc and pc-1 
        schi[i] = float(schi[i])

plt.loglog(np.abs(p[0:pn-2]-pc),np.log10(schi))

plt.show() 
print (np.log10(np.abs(p[pn-2]-pc))-np.log10(np.abs(p[0]-pc)))/(np.log10(schi[-1])-np.log10(schi[0]))