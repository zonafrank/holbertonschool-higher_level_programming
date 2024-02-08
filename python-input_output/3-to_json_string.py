#!/usr/bin/python3
"""Module for function to_json_string"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)

    Args:
        my_obj (obj): object to stringify

    Return:
        str: JSON representation of my_obj
    """
    return json.dumps(my_obj)
