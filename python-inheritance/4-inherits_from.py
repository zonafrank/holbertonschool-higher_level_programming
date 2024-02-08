#!/usr/bin/python3
"""Module for function `inherits_from`"""


def inherits_from(obj, a_class):
    """returns true / false if obj inherits from a_class or not."""
    if (type(obj).__name__ == a_class.__name__):
        return False
    return issubclass(type(obj), a_class)
