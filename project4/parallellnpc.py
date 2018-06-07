import numpy as np 
from scipy.ndimage.measurements import label
from skimage.measure import regionprops
import matplotlib.pyplot as plt
import multiprocessing
import sys
import itertools
#sample = np.logspace(0,np.log10(Lx*Ly),100,dtype = int)

k = np.arange(4,9)
L_ = 2**k
Ln = len(k)
n_ = [0 for i in range(Ln)]
N = 2000

def cluster(L):
    n = {}
    pc = 0.59275
    for i in range(0,N):    
        np.random.seed(i)
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
n_ = pool.map(cluster, L_)
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
#vals = n_[-1].values()
#keys = n_[-1].keys()
#npc , bins  = np.histogram(keys,np.logspace(0,np.log10(Lx*Ly),nbins),weights=vals)
for i in range(Ln):
    keys = n_[i].keys() 
    vals = n_[i].values()
    npb , bins  = np.histogram(keys,np.logspace(0,np.log10(L_[i]*L_[i]),nbins),weights=vals)#np.log10(Lx*Ly)
    plt.loglog(bins[:-1],npb,label="L = %1.4f"%L_[i])
    with open('npc%d'%L_[i],'w') as File:
        for key,val in itertools.izip(keys,vals):
            File.write('%d %f\n' %(key,val))
#plt.loglog(bins[:-1],npc)
#plt.title(r"F",fontsize=20)
plt.ylabel(r"log$_{10}$ n(s,p$_c$,L)",fontsize=17)
plt.xlabel(r"log$_{10}$ s",fontsize=17)
plt.legend(loc="best")
plt.show()
    