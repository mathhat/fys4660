import matplotlib.pyplot as plt 
import numpy as np 
P = []
p = []
with file("P.txt","r") as File:
    line = File.readline()
    line=File.readline().split()
    while line:
        p.append(float(line[0]))
        P.append(float(line[1]))
        line = File.readline().split()
plt.plot(p,P)
plt.ylabel(r"$\Pi$",size=20)
plt.xlabel("p",size=16)
plt.show()  