import matplotlib.pyplot as plt
import numpy as np 
import random 
from scipy import interpolate 
import shapely.geometry as geom 

fig, ax = plt.subplots()
N = 1000 
x, y = np.zeros(N), np.zeros(N)
for i in range(N):
    x[i] = random.uniforms(0, 1)
    y[i] = random.uniforms(0, 1)


scalar_field = 50 * np.sqrt(x**2 + y**2)

sc_plot






sc_plot = ax.scatter(x, y, c = scalar_field)
ax.set_xlabel("f,eufuf")
ax.set_ylabel("fgbnhus")
plt.savefig("dich.png")
