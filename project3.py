import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import h5py




width, height = 500, 500


x = np.linspace(0, width, width)
y = np.linspace(0, height, height)
x, y = np.meshgrid(x, y)
z = np.sin(0.1 * x) * np.cos(0.1 * y)


z += 0.1 * np.random.randn(*z.shape)


grid_x, grid_y = np.mgrid[0:width:500j, 0:height:500j]


points = np.vstack((x.ravel(), y.ravel())).T
values = z.ravel()
grid_z = griddata(points, values, (grid_x, grid_y), method='cubic')


data_points = np.vstack((grid_x.ravel(), grid_y.ravel(), grid_z.ravel())).T


filename = 'nebula_data.h5'
with h5py.File(filename, 'w') as f:
    # Создание группы для данных
    grp = f.create_group('nebula')
    # Сохранение данных
    grp.create_dataset('points', data=data_points)


plt.imshow(grid_z, extent=(0, width, 0, height), origin='lower')
plt.colorbar(label='Intensity')
plt.title('Simulated Nebula Image')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

print(f"Data saved in {"NGC7293_(2004).jpg"}")