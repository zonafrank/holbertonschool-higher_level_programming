#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    key_highest_val = ""
    highest_val = 0
    for key in a_dictionary:
        if a_dictionary.get(key) > highest_val:
            key_highest_val = key
            highest_val = a_dictionary.get(key)
    return key_highest_val
