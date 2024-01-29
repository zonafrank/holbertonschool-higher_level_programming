#!/usr/bin/python3

def roman_to_int(roman_string):
    symbol_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    res = 0
    strlen = len(roman_string)

    for i in range(0, strlen):
        s1 = symbol_map.get(roman_string[i], 0)
        if i + 1 < strlen:
            s2 = symbol_map.get(roman_string[i + 1])
            if s1 >= s2:
                res += s1
            else:
                res -= s1
        else:
            res += s1
    return res
