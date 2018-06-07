import numpy as np 
from scipy.ndimage.measurements import label
from skimage.color import label2rgb
from skimage.measure import regionprops
import matplotlib.pyplot as plt
from skimage.viewer import ImageViewer
import multiprocessing

def pi08(L):
    N = 200 #number of porous systems generated
    pup = np.linspace(0.65 ,0.55,100) #p up
    tol = 0.05
    for p in pup:
        cunt = 0
        for i in range(0,N):
            seed = i
            np.random.seed(seed)
            r = np.random.rand(L,L)
            z = r<p; # This generates the binary array
            z_labeled, num_clusters = label(z)
            regionp = regionprops(z_labeled)
            for prop in regionp:
                bbox = prop.bbox
                if ((bbox[3]-bbox[1] == L) + (bbox[2]-bbox[0] == L)):
                    cunt += 1.0

        prob = cunt/float(N)
        print prob
        if abs(prob - 0.8)<tol:
            print "success ", L
            return p

l = [25, 50, 100, 200, 400]#, 800]


pool = multiprocessing.Pool(len(l))
p_ = pool.map(pi08, l)
pool.close() # no more tasks
pool.join()  # wrap up current tasks
print True==None
print p_
with open("pi2.txt",'a') as fil:
    for i in range(len(l)):
        fil.write('%1.4f   %d \n'%(p_[i],l[i]))
#view = ImageViewer(image)
#view.show()