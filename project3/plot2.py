import matplotlib.pyplot as plt
import numpy as np
n = 5
L = np.zeros(5)
pi3 = np.zeros(5)
pi8 = np.zeros(5)
with open("pi2.txt") as File:
	k = File.readline()
	for i in range(n):
		pi3[i],L[i] = File.readline().split()
		pi3[i] = float (pi3[i])
                L[i] = float (L[i])

        File.readline()
        for i in range(n):
                pi8[i] = float(File.readline().split()[0])
print pi3
print pi8
y0 = np.log10(pi8[0]-pi3[0])
y1 = np.log10(pi8[-1]-pi3[-1])
x0 = np.log10(L[0])
x1 = np.log10(L[-1])
print "1/v = ", abs((y1-y0)/(x1-x0))

plt.plot(L**(-3/4),pi8)
plt.plot(L**(-3/4),pi3)
plt.show()
