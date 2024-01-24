#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_val = 0
    for val in my_list:
        if val > max_val:
            max_val = val
    return max_val
