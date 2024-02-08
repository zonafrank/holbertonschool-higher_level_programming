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

    def area(self):
        """Calculates and returns the area of the rectangle instance
        Return:
            int: area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """Returns a string which describes the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
