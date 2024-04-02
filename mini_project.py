import matplotlib.pyplot as plt
import numpy as np 
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots() 

anim_object1, = plt.plot([], [], '-', lw = 2) 

xdata1, ydata1 = [], []

ax.set_xlim(0, 5 * np.pi)
ax.set_ylim(-2,2) 

def update(frame):
    xdata.append(frame)
    ydata. append(np.sin(frame))
    anim_object1.set_data(xdata,ydata)

    return anim_object,

ani = FuncAnimation (fig, update, frames = np.arange(0,5*np.pi,0.3), interval = 100)

ani.save('animation_7.gif')