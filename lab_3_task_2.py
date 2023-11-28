import numpy as np
h = 100
a= 3.14159/3
b=30
g = 10
v = np.sqrt(g*h*np.tan(b)**2/2*np.cos(a)**2*(1-np.tan(b))*np.tan(a))
print(v)