import numpy as np
import matplotlib.pyplot as plt 
from scipy import interpolate
import shapely.geometry as geom 

phi = np.linspace(0, 2*np.pi, 40)
r = 0.5 + np.cos(phi)
x = r * np.cos(phi)
y = r * np.sin(phi)

spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords) 

curve_cords = []
for i in range(len(spline_curve[0])):
    curve_cords.append([spline_curve[0][i], spline_curve[1][i]])

polygon = geom.Polygon(curve_cords)
points_number_per_side = 100 
x_pictures_limits = [-0.5, 2]
y_pictures_limits = [-1, 1]

for x_point_cord in np.linspace(*x_pictures_limits, points_number_per_side):
    for y_point_cord in np.linspace(*y_pictures_limits, points_number_per_side):
        p = geom.Point(x_point_cord, y_point_cord,)
        if p.within(polygon):
            plt.plot(x_point_cord, y_point_cord, "go", ms = 0.5)



plt.plot(spline_curve[0], spline_curve[1]) 
plt.axis ("equal")
plt.savefig("point_in_polligon.png")