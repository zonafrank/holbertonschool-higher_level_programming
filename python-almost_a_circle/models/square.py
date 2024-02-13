#!/usr/bin/python3
"""Module for Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, which inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization method for instances"""
        super().__init__(size, size, x, y, id)
        # self.size = size

    def __str__(self):
        """overides the __str__ method of Rectangle"""
        class_name = type(self).__name__
        id = self.id
        x = self.x
        y = self.y
        width = self.width
        return f"[{class_name}] ({id}) {x}/{y} - {width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, val):
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute:"""
        if args:
            for idx, val in enumerate(args):
                if idx == 0:
                    self.id = val
                elif idx == 1:
                    self.width = val
                    self.height = val
                elif idx == 2:
                    self.x = val
                elif idx == 3:
                    self.y = val
        else:
            if kwargs:
                for key in kwargs:
                    if key == "size":
                        self.__setattr__("width", kwargs[key])
                        self.__setattr__("height", kwargs[key])
                    else:
                        self.__setattr__(key, kwargs[key])
