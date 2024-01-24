#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    list_copy = [val for val in my_list]
    if idx < 0 or idx >= len(list_copy):
        return list_copy
    
    list_copy[idx] = element
    return list_copy
