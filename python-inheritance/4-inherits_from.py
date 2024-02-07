#!/usr/bin/python3

def inherits_from(obj, a_class):
    if (type(obj).__name__ == a_class.__name__):
        return False
    return issubclass(type(obj), a_class)
