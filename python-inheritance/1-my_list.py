#!/usr/bin/python3
"""
Contains a class MyList that inherits from list
"""


class MyList(list):
    """MyList class that inherits from list type"""

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
        return self
