import numpy as np 
from scipy.ndimage.measurements import label
from skimage.measure import regionprops
import matplotlib.pyplot as plt
k = np.arange(4,8)
Lx_ = 2**k
Ly_ = 2**k
N = 1000 #number of porous systems generated
pc = 0.59275
p_ = np.linspace(pc-0.05,pc,4)
estimate = np.zeros(4)
for Lx,Ly in zip(Lx_,Ly_):
    p=pc-0.02
    n = {}
    for i in range(0,N):    
        cunt = 0
        seed = i
        np.random.seed(seed)
        r = np.random.rand(Lx,Ly)
        z = r<p; # This generates the binary array
        z_labeled, num_clusters = label(z)
        regionp = regionprops(z_labeled)
        for prop in regionp:
            bbox = prop.bbox
            area = prop.area
            if (bbox[3]-bbox[1] == Lx) or (bbox[2]-bbox[0] == Ly):
                continue
            else:
                try :
                    n[area] += 1
                except:
                    n[area] = 1
    pees = np.zeros(len(n.keys()),dtype=float)
    keys = np.asarray(np.sort(n.keys()),dtype=float)
    i=0
    for key in keys:
        pees[i] = n[key]
        i+=1
    pees /= (Lx*Ly*N)
    plt.plot(np.log10(keys[0:len(keys)/1.5]),np.log10(pees[0:len(keys)/1.5]),label="L %d" % Lx)

#plt.hist(keys,bins=np.logspace(0,3,50),weights=pees)#,label="p = %1.3f" % p)

plt.title("loglog of n(s,Pc;L) for various L",size=16)
plt.xlabel("log10 s",size=16)
plt.ylabel(r"log10 n(s,$p_c$;L)",size=16)
plt.legend(loc="best")
plt.show()
               
    #File.write("   %1.3f    %1.4f \n"% (p,P))
