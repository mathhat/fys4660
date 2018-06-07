import numpy as np 
from scipy.ndimage.measurements import label
from skimage.color import label2rgb
from skimage.measure import regionprops
import matplotlib.pyplot as plt
from skimage.viewer import ImageViewer
Lx = 100
Ly = 100
N = 1000 #number of porous systems generated
p_ = np.linspace(0.5,1,51)
with open("P.txt", "w") as File:
    File.write("    p        P \n")
    for p in p_:
        average = []
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
                if (bbox[3]-bbox[1] == Lx) or (bbox[2]-bbox[0] == Ly):
                    cunt += prop.area
                    

            prob = cunt/float(Lx*Ly)
            average.append(prob)
        P = np.mean(average)
        print P
        File.write("   %1.3f    %1.4f \n"% (p,P))
        

#view = ImageViewer(image)
#view.show()