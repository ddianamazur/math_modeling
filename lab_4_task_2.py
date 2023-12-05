import numpy as np

def my_func(massive):
    x = 1
    for i in massive:
        x = x * i
    return x 

mass1 = [2, 8, 40, 60]
mass2 = np.array(mass1)

print(my_func(mass2))