#!/usr/bin/python3
"""module for Base class"""
import json


class Base:
    """Base class"""
    __nb_objects = 0
    id = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        that returns the JSON string representation of list_dictionaries

        Args:
            list_iof_dictionaries (list): list of dictionary objects

        Returns:
            str: stringified version of list_of_dictionaries
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file

        Args:
            list_objs (any): the data to convert to JSON

        Returns:
            Nothing
        """
        res = "[]"
        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as f:
            if not list_objs:
                f.write(res)
            else:
                list_of_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_of_dicts))
