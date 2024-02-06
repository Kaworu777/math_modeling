import matplotlib.pyplot as plt 
import numpy as np
def elps(a=9, b=4):
    x = np.arange(-2*a, 2*a, 0.1)
    y = np.arange(-2*a, 2*a, 0.1)
    X, Y = np.meshgrid(x, y)
    fxy = X**2/a**2 + Y**2/b**2 - 1 
    plt.contour(X ,Y, fxy, levels=[0])
    plt.axis('equal')
    plt.savefig('fig_lab6_task3.png')

if __name__ == '__main__': 
    elps()
