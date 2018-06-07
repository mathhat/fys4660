import numpy as np 
from scipy.ndimage.measurements import label
from skimage.measure import regionprops
import matplotlib.pyplot as plt
import multiprocessing
import sys
import itertools

pc = 0.59275
p = np.linspace(pc-0.15,pc+0.05,40) 

k = 8
L = 2**k
pn = len(p)
N = 100

n_ = [0 for i in range(pn)]

def cluster(p):
    n = {}
    pc = 0.59275
    for i in range(0,N):    
        np.random.seed(i)
        r = np.random.rand(L,L)
        z = r<p; # This generates the binary array
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
    return n

pool = multiprocessing.Pool(pn)
n_ = pool.map(cluster, p)
pool.close() # no more tasks
pool.join()  # wrap up current tasks
S_ = [0 for i in range(pn)]

for i in range(pn):
    P = p[i]
    n = n_[i]
    S = 0
    for key,val in itertools.izip(n.keys(),n.values()):
        S += key**2 * float(val) #s * s * npc
    S_[i] = S

with open('data/S(L=%d)'%(L),'w') as File:
    for s in S_:
        File.write('%1.14f\n' %(s))