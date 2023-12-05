import numpy as np

g = 10


def my_func(m, h, v):
    pot = m*g*h
    kin = m*v**2/2
    E = pot + kin
    print(E)
    

my_func(20, 60, 85)