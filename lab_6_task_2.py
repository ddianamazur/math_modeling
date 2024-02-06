import matplotlib.pyplot as plt
import numpy as np

def hyperbola(k):

    x = np.arange(.01, 10, 0.01)
    y = k/x

    plt.plot(x,y,label = 'gang bang')
    plt.savefig('fig_6.png')

if  __name__ == '__main__':
    hyperbola(.7)