#!/usr/bin/python3
"""
This module contains the class LockecClass
LockedClass will only allow the attribute `first_name` to be set on it
"""


class LockedClass:
    """A class that prevents dynamic attribute creation, except for 'first_name'."""
    __slots__ = ["first_name"]

    def __setattr__(self, name, value):
        """Restrict attribute creation to 'first_name'."""
        if name == "first_name":
            super().__setattr__(name, value)
        else:
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{name}'")
