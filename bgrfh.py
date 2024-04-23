import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('ss.jpg')
fig, ax = plt.subplots()
ax.imshow(img)

x = [100,300]
y = [60,100]
plt.plot(x,y,lw = 2, color = 'w')
plt.ylim()
plt.savefig('KILL9.png')