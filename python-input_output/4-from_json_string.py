#!/usr/bin/python3
"""Module for function from_json_strint"""
import json


def from_json_string(my_str):
    """Converts a JSON string to a python object

    Args:
        my_str (str): the string to convert to JSON

    Return:
        obj: a python object
    """
    return json.loads(my_str)
