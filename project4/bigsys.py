import numpy as np 
from scipy.ndimage.measurements import label
from skimage.measure import regionprops
import matplotlib.pyplot as plt
import multiprocessing
import sys
import itertools
#sample = np.logspace(0,np.log10(Lx*Ly),100,dtype = int)
threads = 8
size = int(raw_input("size of sys in 2**x"))
k = np.ones(threads,dtype=int)*size #system size expo
L = 2**k #system size
Ln = len(k)
n_ = [0 for i in range(Ln)]
N = 1000

def cluster(L):
    n = {}
    pc = 0.59275
    for i in range(0,N):    
        #np.random.seed(i)
        r = np.random.rand(L,L)
        z = r<pc; # This generates the binary array
        z_labeled, num_clusters = label(z)
        for prop in regionprops(z_labeled):
            bbox = prop.bbox
            bol = np.bool((bbox[3]-bbox[1] == L) + (bbox[2]-bbox[0] == L))
            if bol:
                continue
            area = int(prop.area)
            try:
                n[area] += 1
            except:
                n[area] = 1
    scale = float(L*L*N)
    for key in n:
        n[key] /= scale
    print ('done with', L)
    return n


pool = multiprocessing.Pool(Ln)
n_ = pool.map(cluster, L)
pool.close() # no more tasks
pool.join()  # wrap up current tasks

def merge(n_):
    N = n_[0] #cheating
    for n in n_[1:]:
        for key,val in itertools.izip(n.keys(),n.values()):
            try:
                N[key] += val 
            except:
                N[key] = val
    for keys in N.keys():
        N[keys]/=float(threads)
    return N

N = merge(n_)

nbins=30
#vals = n_[-1].values()
#keys = n_[-1].keys()
#npc , bins  = np.histogram(keys,np.logspace(0,np.log10(Lx*Ly),nbins),weights=vals)
#for i in range(Ln):
keys = N.keys() 
vals = N.values()
npb , bins  = np.histogram(keys,np.logspace(0,np.log10(L[0]*L[0]),nbins),weights=vals)#np.log10(Lx*Ly)
plt.loglog(bins[:-1],npb,label="L = %d"%L[0])
with open('npc%d'%L[0],'w') as File:
    for key,val in itertools.izip(keys,vals):
        File.write('%d %1.14f\n' %(key,val))
#plt.loglog(bins[:-1],npc)
#plt.title(r"F",fontsize=20)
plt.ylabel(r"log$_{10}$ n(s,p$_c$,L)",fontsize=17)
plt.xlabel(r"log$_{10}$ s",fontsize=17)
plt.legend(loc="best")
plt.show()
    