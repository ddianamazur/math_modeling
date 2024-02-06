import matplotlib.pyplot as plt
import numpy as np
b=1

def spiral(b):

    phi = np.arange(.01, 10, 0.01)
    e = 2.7
    r = e**(b*phi)

    x = r*np.cos(phi)
    y = r*np.sin(phi)


    plt.plot(x,y,label = 'gang bang')
    plt.savefig('fig_8.png')

if  __name__ == '__main__':
    spiral(.3)