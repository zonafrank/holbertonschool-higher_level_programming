#!/usr/bin/python3
"""Task 0. Integers addition
"""


def add_integer(a, b=98):
    """Function that adds two integers

    Args:
        a (int): The first integer
        b (int): The second integer

    Returns:
        int: the sum of a and b

    Raises:
        TypeError: Either of a and b is not an integer
    """
    try:
        a = int(a)
    except Exception as e:
        raise TypeError("a must be an integer")
    
    try:
        b = int(b)
    except Exception as e:
        raise TypeError("b must be an integer")
 
    return a + b
