import math


def bhaskara(a, b, c):
    delta = b ** 2 - 4 * a * c
    
    
    if delta < 0:
        print('n há raízes')
    else:
        r1 = (-b + delta ** (1/2)) / (2 * a)
        r2 = (-b - delta ** (1/2)) / (2 * a)
        return r1, r2
print(bhaskara(3, 9, 27))
print(bhaskara(3, 9, -27))