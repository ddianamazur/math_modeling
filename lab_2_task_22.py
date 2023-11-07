a = int(input('first side'))
b = int(input('secod side'))
c = int(input('third side'))
if a < c + b and b < c + a and c < a + b:
    print('yes')
    if a == b == c:
        print('equal')
    elif (a == b and c!= a) or ( b == c and a!= b) or ( a == c and a != b):
        print('isosceles')
    else:
        print('usual')
else:
    print('no')