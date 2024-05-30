import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import shapely.geometry as geom

img = plt.imread('ss.jpg')
fig, ax = plt.subplots()
ax.imshow(img)

x = [140,150,160,165,180,190,200,210,220,225,223,230,226,225,230,234,234,230,238,230,225,215,205,200,195,180,175,170,160,150,130,140]
y = [70,65,50,45,33,40,45,40,45,45,55,60,65,70,77,77,78,85,95,100,95,93,92,85,80,105,105,107,100,105,75,70]

plt.plot(x,y,lw = 2, color = 'w')
plt.ylim()
plt.savefig('чиназес2.png')