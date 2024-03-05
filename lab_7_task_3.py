import matplotlib.pyplot as plt
import numpy as np 
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots() #создание пространства и подпространства

anim_object, = plt.plot([], [], '-', lw = 2) # объект анимации

xdata, ydata = [], []

ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
 

def update(t):
    xdata.append(np.sin(t) * (e**np.cos(t) - np.e*np.cos(4*t))+np.sin(t/12)**5)
    ydata. append(np.cos(t) *(e**np.cos(t) - np.e**np.cos(4*t) + np.sin (t/12)** 5 ))
    anim_object.set_data(xdata,ydata)
    return anim_object,

ani = FuncAnimation (fig, update, frames = np.arange(0.12*3.14), interval = 100)

ani.save('animation_5.gif')
