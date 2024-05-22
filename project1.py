import numpy as np
import matplotlib.pyplot as plt
import h5py


x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y = np.linspace(-2*np.pi, 2*np.pi, 1000)
X, Y = np.meshgrid(x, y)
Z = np.arctan2(Y, X)


x_new = np.linspace(-2*np.pi, 2*np.pi, 100)
y_new = np.linspace(-2*np.pi, 2*np.pi, 100)
X_new, Y_new = np.meshgrid(x_new, y_new)
Z_interp = np.interp(X_new, x, Z)


plt.figure(figsize=(10, 10))
plt.imshow(Z_interp, cmap='viridis', extent=(-2*np.pi, 2*np.pi, -2*np.pi, 2*np.pi))
plt.colorbar()
plt.axis('equal')
plt.axis('off')
plt.show()

