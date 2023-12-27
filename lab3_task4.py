import numpy as np
A = 5
F = 4
a = np.zeros((A, F))
for i in np.arange(0, A, 1):
    for j in np.arange(0, F, 1):
        arg = np.sin(A * i + F * j + 1)
        if arg < 0:
            a[i,j] = 0
        else:
            a[i,j] = arg
        

print(a)