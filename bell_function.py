import matplotlib as plt
import numpy as np
from scipy import interpolate
import shapely.geometry as geom

x_p = np.array(points_coords[0::2])
y_p = np.array(points_coords[1::2])

def bell_function (x,y, intensity = 1, dec_rate = [0.5,0.5]):
    scalar_field = intensity * np.exp(-dec_rate[0]*x**2-dec_rate[1]*y**2)
    return scalar_field
fig,ax = plt.subplots()
sc_plot = ax.scatter(x_p, y_p, c = bell function)
ax.set_xlabel('координатата х,м')
ax.set_xlabel('координатата y,м')
cbar = fig.colorbar(sc_plot)
cbar.set_label('интенсивность скалярного поля')

plt.savefig('field.png')
                  