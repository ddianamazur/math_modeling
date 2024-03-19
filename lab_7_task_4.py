from matplotlib.animation import FuncAnimation 
import matplotlib.pyplot as plt 
import numpy as np  

x0 = 0.1
y0 = 0.1
C = 0.3
D = 0.33

xdata1, ydata1 = [], []
xdata1.append(x0)
ydata1.append(y0)

def animate(i):
    xdata1.append(xdata1[i-1]**2 - ydata1[i-1]**2 + C)
    ydata1.append(2* xdata1[i-1] * ydata1[i-1] + D)
    lama.set_data(xdata1, ydata1)
    return lama, 

if __name__ == '__main__':
    plt.axis('equal')
    fig, ax = plt.subplots()
    lama, = plt.plot([], [], 'o', color = 'r', label = 'Lama')
    edge = 1
    ax.set_xlim(-edge, edge) 
    ax.set_ylim(-edge, edge)
    
ani = FuncAnimation(fig, animate, frames=range(1,100), interval=50)

ani.save ("animation_6.gif")
