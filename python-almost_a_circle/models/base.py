#!/usr/bin/python3
"""module for Base class"""
import json
import turtle


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
        """Convert string to json

        Args:
            json_string (str) : string representation of list of dicts

        Returns:
            list

        """
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
                list_of_dicts = cls.from_json_string(f.read())
                return [cls.create(**obj) for obj in list_of_dicts]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw_square(ttl, square):
        """draws a square instance

        Args:
            ttl (Turtle): turtle instance
            square (Square): Square instance

        Returns:
            Nothing
        """
        ttl.up()
        ttl.goto(square.x, square.y)
        ttl.down()
        for _ in range(4):
            ttl.forward(square.size)
            ttl.left(90)

    @staticmethod
    def draw_rectangle(ttl, rectangle):
        """draws a rectangle instance

        Args:
            ttl (Turtle): turtle instance
            rectangle (Rectangle): Rectangle instance

        Returns:
            Nothing
        """
        ttl.up()
        ttl.goto(rectangle.x, rectangle.y)
        ttl.down()
        for _ in range(2):
            ttl.forward(rectangle.width)
            ttl.left(90)
            ttl.forward(rectangle.height)
            ttl.left(90)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draws rectangles and squares using turtle package

        Args:
            list_rectangle (list): list of Rectangle instances
            list_squares (list): list of Square instances

        Returns:
            Nothing
        """
        win = turtle.Screen()
        win.bgcolor("yellow")
        win.title("turtle")
        ttl = turtle.Turtle()

        for rect in list_rectangles:
            Base.draw_rectangle(ttl, rect)

        for square in list_squares:
            Base.draw_square(ttl, square)
