#!/usr/bin/python3
import json
"""Module for function class_to_json"""


def class_to_json(obj):
    """eturns the dictionary description with simple data structure"""
    return json.dumps(obj.__dict__)
