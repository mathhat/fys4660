import numpy as np 
from scipy.ndimage.measurements import label
from skimage.measure import regionprops
import matplotlib.pyplot as plt
import multiprocessing
import sys

#sample = np.logspace(0,np.log10(Lx*Ly),100,dtype = int)
k = 6
Lx = 2**k
Ly = 2**k
pc = 0.59275
pn = 8
p_ = np.linspace(pc-0.04,pc,pn)
n_ = [0 for i in range(pn)]
N = 1000

def cluster(p):
    n = {}
    for i in range(0,N):    
        np.random.seed(i)
        r = np.random.rand(Lx,Ly)
        z = r<p; # This generates the binary array
        z_labeled, num_clusters = label(z)
        for prop in regionprops(z_labeled):
            bbox = prop.bbox
            if (bbox[3]-bbox[1] == Lx) or (bbox[2]-bbox[0] == Ly):
                continue
            area = int(prop.area)
            try:
                n[area] += 1
            except:
                n[area] = 1
    scale = float(Lx*Ly*N)
    for key in n:
        n[key] /= scale
    return n


#builtin_outputs = map(cluster, inputs)

#pool_size = multiprocessing.cpu_count() /2
pool = multiprocessing.Pool(len(p_))
n_ = pool.map(cluster, p_)
pool.close() # no more tasks
pool.join()  # wrap up current tasks

'''
ts =[]
for i in range(pn):
    p = multiprocessing.Process(target=cluster,args=())
    p.start()
    ts.append(p)
for i in range(pn):
    ts[i].join()
'''
nbins=30
vals = n_[-1].values()
keys = n_[-1].keys()
npc , bins  = np.histogram(keys,np.logspace(0,np.log10(Lx*Ly),nbins),weights=vals)
for i in range(pn-1):
    npb , bins  = np.histogram(n_[i].keys(),np.logspace(0,np.log10(Lx*Ly),nbins),weights=n_[i].values())#np.log10(Lx*Ly)
    plt.loglog(bins[:-1],1.0*npb/npc,label="p = %1.4f"%p_[i])
#plt.loglog(bins[:-1],npc)
#plt.title(r"F",fontsize=20)
plt.ylabel(r"n(s,p)/n(s,p$_c$)",fontsize=17)
plt.xlabel(r"log$_{10}$ s",fontsize=17)
plt.legend(loc="best")
plt.show()
