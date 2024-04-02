import matplotlib.pyplot as plt
import numpy as np 
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots() 

anim_object1, = plt.plot([], [], '-', lw = 2, color = 'r') 
anim_object2, = plt.plot([], [], '-', lw = 2, color = 'b') 
anim_object3, = plt.plot([], [], '-', lw = 2, color = 'g') 

xdata1, ydata1 = [], []
xdata2, ydata2 = [], []
xdata3, ydata3 = [], []

def update(frame):
    xdata1.append(frame)
    ydata1.append(np.sin(frame+np.pi))
    anim_object1.set_data(xdata1,ydata1)

    xdata2.append(frame)
    ydata2.append(np.sin(frame)+3)
    anim_object2.set_data(xdata2,ydata2)

    xdata3.append(frame)
    ydata3 = -5 + np.array(ydata1) + np.array(ydata2)
    anim_object3.set_data(xdata3,ydata3)



ax.set_xlim(0, 5 * np.pi)
ax.set_ylim(-8, 8) 

ani = FuncAnimation (fig, update, frames = np.arange(0, 8*np.pi, 0.1), interval = 100)

ani.save('animation_8.gif')