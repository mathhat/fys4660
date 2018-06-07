import numpy as np 
import matplotlib.pyplot as plt
import multiprocessing
import sys
import itertools
k = np.arange(4,9)
L_ = 2**k 
Ln = len(k)
n_ = [0 for i in range(Ln)]
nbins = 50
for it in range(Ln):
    i = L_[it]
    n = {}
    with open('npc%d'%i,'r') as File:
        for line in File:
            key,val= int(line.split(" ")[0]),float(line.split(" ")[1])
            n[key] = val 
    n_[it] = n
    keys = n_[it].keys() 
    vals = n_[it].values()
    npb , bins  = np.histogram(keys,np.logspace(0,np.log10(L_[it]*L_[it]),nbins),weights=vals)#np.log10(Lx*Ly)
    plt.loglog(bins[:-1],npb,label="L = %d"%L_[it])
    #plt.loglog(bins[:-1][23:24],npb[23:24],'r-o')
#plt.loglog(bins[:-1],npc)
plt.title(r"n(s,p$_c$,L)",fontsize=20)
plt.ylabel(r"log$_{10}$ n(s,p$_c$,L)",fontsize=17)
plt.xlabel(r"log$_{10}$ s",fontsize=17)
plt.legend(loc="best")
plt.show()
    