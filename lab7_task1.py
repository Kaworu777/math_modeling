import numpy as np
import matplotlib.pyplot as plt
R = 1 
t = np.arange(0, 10, 0.01)
x = R*t - R*np.np.sin(t)
y = R - R*np.cos(t)
plt.axis("equal")
plt.plot(x, y)
plt.svafig("fig_1.png")
