import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

img = plt.imread('horsehead_aldohubble_960.jpg')
fig, ax = plt.subplots()
ax.imshow(img)

x = [100, 120,130,140,150,150,200,225,250,250,265,270,280,290,295,310,320,340,350,400,400,600,650,660,680,700,720,750,770,800,800,790,810,805,815,820,790,800,780,765,800,300,400,430,440,400,350,250,190,180,160,100,70,100]
y = [400,380,370,360,350,340,335,300,200,140,125,120,110,100,95,95,95,110,120,130,125,135,150,160,170,180,200,230,250,300,310,310,320,330,400,510,550,600,650,800,1000,1000,800,600,500,420,500,570,600,610,600,600,500,400]

spline_coords, figure_spline_part = interpolate.splprep([x,y], s = 0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)
plt.plot(spline_curve[0], spline_curve[1], color  = 'g', lw = 4)

plt.plot(x,y,lw = 2, color = 'w')
plt.ylim()
plt.savefig('KILL8.png')