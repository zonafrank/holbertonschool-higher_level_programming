#!/usr/bin/python3

def safe_print_integer(value):
    returnVal = False
    try:
        print("{:d}".format(value))
        returnVal = True
    except Exception:
        pass
    return returnVal
