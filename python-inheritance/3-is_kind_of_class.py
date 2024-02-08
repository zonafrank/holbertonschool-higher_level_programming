#!/usr/bin/python3
"""Module for ``is_kind_of_class`` function"""


def is_kind_of_class(obj, a_class):
    """
    checks if obj is an instance of a_class, or if the obj is an
    instance of a class that inherited from, the a_class

    Args:
        obj (object): object to check
        a_class (type): type to check if ancestor of obj

    Return:
        bool: True if obj is a descendant of a_class else False
    """
    return isinstance(obj, a_class)
