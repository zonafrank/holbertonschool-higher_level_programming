#!/usr/bin/python3

def pow(a, b):
    res = 1
    sign = -1 if b < 0 else 1
    for i in range(abs(b)):
        if sign < 0:
            res /= a
        else:
             res *= a
    return res

print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))