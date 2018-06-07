import numpy as np 
from scipy.ndimage.measurements import label
from skimage.measure import regionprops
import matplotlib.pyplot as plt
import sys
N = 10
k = 8

Lx = 2**k
Ly = 2**k
pc = 0.59275
pn = 6
p_ = np.linspace(pc-0.06,pc,pn)
n_ = [] #list of dictionaries
#sample = np.logspace(0,np.log10(Lx*Ly),100,dtype = int)

for p in p_:
    n = {}
    for i in range(0,N):    
        seed = i
        np.random.seed(seed)
        r = np.random.rand(Lx,Ly)
        z = r<p; # This generates the binary array
        z_labeled, num_clusters = label(z)
        regionp = regionprops(z_labeled)
        for prop in regionp:
            bbox = prop.bbox
            if (bbox[3]-bbox[1] == Lx) or (bbox[2]-bbox[0] == Ly):
                continue
            area = int(prop.area)
            try:
                n[area] += 1
            except:
                n[area] = 1
    n_.append(n)
'''
nbins=35
vals = n_[-1].values()
keys = n_[-1].keys()
npc , bins  = np.histogram(keys,np.logspace(0,np.log10(Lx*Ly/3.),nbins),weights=vals)
for i in range(pn-1):
    npb , bins  = np.histogram(n_[i].keys(),np.logspace(0,np.log10(Lx*Ly),nbins),weights=n_[i].values())
    plt.loglog(bins[:-1],1.0*npb/npc,label="p = %1.4f"%p_[i])
#plt.loglog(bins[:-1],npc)
plt.title(r"Cluster Number Densities Divided py n(s,p$_c$)",fontsize=20)
plt.ylabel(r"n(s,p)/n(s,p$_c$)",fontsize=17)
plt.xlabel(r"log$_{10}$ s",fontsize=17)
plt.legend(loc="best")
plt.show()
#for i in range(pn):

'''