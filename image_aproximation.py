import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('horsehead_aldohubble_960.jpg')
fig, ax = plt.subplots()
ax.imshow(img)
x = [0, 100]
y = [250,230]
plt.plot(x,y,lw = 2, color = 'w')
plt.ylim()
plt.savefig('KILL3.png')