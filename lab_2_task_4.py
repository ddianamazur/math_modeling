a = 1
b = 1
stop = int(input('введи'))
for _ in range(0,stop, 1): 
    c = a + b
    a = b
    b = c
    print(c)
