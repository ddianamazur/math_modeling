a = int(input('1koef'))
b = int(input('2koef'))
c = int(input('3koef'))
d = b**2 - 4*a*c
x = (-b + d**0.5) / 2**a or (-b - d**0.5) / 2**a
a*x**2 + b*x + c  == 0



print (x)
