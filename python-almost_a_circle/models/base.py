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

    @staticmethod
    def from_json_string(json_string):
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates a class instance with everything already set

        Args:
            key-value pairs (dictionary)

        Returns:
            the class instance

        """
        new_obj = None
        if cls.__name__ == "Rectangle":
            new_obj = cls(1, 1)
        elif cls.__name__ == "Square":
            new_obj = cls(1)
        new_obj.update(**dictionary)
        return new_obj

    @classmethod
    def load_from_file(cls):
        """Reads a file and creates mulitple class instances

        Args:
            nothing

        Returns:
            list of instances

        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r", encoding="utf-8") as f:
                list_of_dicts = json.load(f)
                return [cls.create(**obj) for obj in list_of_dicts]
        except FileNotFoundError:
            return []
