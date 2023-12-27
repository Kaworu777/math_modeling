import numpy as np 

from lab3_task1 import eiler_num as en
from lab3_task1 import plank_num as pn
from lab3_task1 import bolcman_num as bn
a = 9,8 * 100 * np.tan(30)**2
b = 2 * np.cos(np.pi/3)**2 * (1 - np.tan(30) * np.tan(np.pi/3))
v = np.sqrt(a / b)
print(v)