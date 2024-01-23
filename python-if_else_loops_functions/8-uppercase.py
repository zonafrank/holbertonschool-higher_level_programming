#!/usr/bin/python3

def uppercase(str):
    res = ""
    for char in str:
        ascii_val = ord(char)
        if ascii_val >= 97 and ascii_val <= 122:
            res += chr(ascii_val - 32)
        else:
            res += char

    print("{}".format(res))
