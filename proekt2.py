import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y = np.linspace(-2*np.pi, 2*np.pi, 1000)
X, Y = np.meshgrid(x, y)
Z = np.arctan2(Y, X)


plt.figure(figsize=(8, 8))
plt.imshow(Z, cmap='viridis', extent=(-2*np.pi, 2*np.pi, -2*np.pi, 2*np.pi))
plt.colorbar()
plt.axis('equal')
plt.axis('off')
plt.show()