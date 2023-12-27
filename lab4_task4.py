import numpy as np 
def lightfunc():
    a = int(input("vvedite start promejytka"))
    b = int(input("vvedite stop promejytka"))
    x = np.arange(a, b, 1)
    y = x**2 + 2 
    return y 
o = lightfunc()
print(o)
