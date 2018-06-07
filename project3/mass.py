import numpy as np 
from scipy.ndimage.measurements import label
from skimage.measure import regionprops
import matplotlib.pyplot as plt
import multiprocessing
import sys

#sample = np.logspace(0,np.log10(Lx*Ly),100,dtype = int)

k = np.arange(4,11)
kn = len(k)
print kn
L = 2**k
pc = 0.59275
m_ = [0 for i in range(kn)]
N = 1000

def mass(L):
    p = 0.59275    
    M = 0
    cunt=0
    for i in range(0,N):    
        np.random.seed(i)
        r = np.random.rand(L,L)
        z = r<p; # This generates the binary array
        z_labeled, num_clusters = label(z)
        for prop in regionprops(z_labeled):
            bbox = prop.bbox
            if ((bbox[3]-bbox[1] == L) + (bbox[2]-bbox[0] == L)):
                M += int(prop.area)
                cunt += 1
    M = float(M)/(cunt)
    print L
    return M



#pool_size = multiprocessing.cpu_count() /2
pool = multiprocessing.Pool(kn)
m_ = pool.map(mass, L)
pool.close() # no more tasks
pool.join()  # wrap up current tasks

plt.loglog(L,np.log10(m_))
plt.show()
print m_