import numpy as np 
import matplotlib.pyplot as plt
pc = 0.59275
p = np.linspace(pc-0.15,pc+0.05,40)

k = np.arange(5,9,dtype=int)
L = 2**k 
for l in L:
    s=[]
    with open('data/S(L=%d)'%(l),'r') as File:
        for line in File:
            s.append(float(line)*l**(-3*43/18./4.)) 
    plt.plot((p-pc)**(4/3.)*l,s)
plt.show()