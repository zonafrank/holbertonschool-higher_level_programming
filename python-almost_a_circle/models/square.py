#!/usr/bin/python3
"""Module for Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, which inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization method for instances"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overides the __str__ method of Rectangle"""
        class_name = type(self).__name__
        id = self.id
        x = self.x
        y = self.y
        width = self.width
        return f"[{class_name}] ({id}) {x}/{y} - {width}"
