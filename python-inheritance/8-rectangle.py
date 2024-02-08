#!/usr/bin/python3
"""Module for the Rectangle class"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class which inherits from the BaseGeometry class"""

    def __init__(self, width, height):
        """instance initialization method"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
