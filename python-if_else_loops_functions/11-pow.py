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
