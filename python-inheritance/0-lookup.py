#!/usr/bin/python3
"""
Module for function that returns the list of available
attributes and methods of an object
"""


def lookup(obj):
    """
    function that returns the list of available attributes
    and methods of an object

    Args:
        obj (object): object to get the attributes of

    Returns:
        list: attributes of the object passed in as argument
    """
    return dir(obj)
