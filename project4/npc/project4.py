import numpy as np 
import matplotlib.pyplot as plt

k = np.arange(4,9)
L_ = 2**k 
Ln = len(k)
n_ = [0 for i in range(Ln)]
for it in range(Ln):
    i = L_[it]
    S = []
    with open('npc%d'%i,'r') as File:
        for line in File:
            line = line.split(" ")
            S.append([int(line[0],float(line[1])]) #s * npc
    S_[it] = S

Slog = np.log10(S_)
Llog = np.log10(L_)
mod0 = (Slog[-1]-Slog[0]) / float(Llog[-1]-Llog[0]) * np.linspace(0,3,11) #+ Llog[0]
#mod0 -= mod0[0]
mod0 -= Slog[0]*1.4
print 10**mod0[0]
plt.plot(np.linspace(0,3,11),mod0)
for i in range(Ln):
    plt.plot(Llog[i],Slog[i],'o',label="L = %d" %L_[i])
plt.title("S = S0*L^D = 0.05*L^1.8")
plt.ylabel("log10 S(pc,L)",size=15)
plt.xlabel("log10 L",size=15)
plt.legend(numpoints=1,loc='best')
plt.show()
'''
import numpy as np 
import matplotlib.pyplot as plt

k = np.arange(4,9)
L_ = 2**k 
Ln = len(k)
n_ = [0 for i in range(Ln)]
for it in range(Ln):
    i = L_[it]
    n = []
    with open('npc%d'%i,'r') as File:
        for line in File:
            line = line.split(" ")
            n.append([int(line[0]),float(line[1])]) #s * npc
    n_[it] = np.asarray(n)

for i in range(Ln):
    plt.plot(n_[i],label="L = %d" %L_[i])
plt.title("npc for various L")
plt.ylabel("npc",size=15)
plt.xlabel("s",size=15)
plt.legend(numpoints=1,loc='best')
plt.show()
'''