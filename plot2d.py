#!python3
import numpy as np
import random
import matplotlib.pyplot as plt
x=np.linspace(0,5,50)
y=np.linspace(0,5,50)[:,np.newaxis]
z=np.sin(x)**10+np.cos(3+y*x)*np.cos(x)
print(z)
plt.imshow(z,origin='lower',extent=[0,5,0,5],cmap='viridis')
plt.colorbar()
n=np.random.random((10,100))
n.sort()
print(n)
plt.show()
