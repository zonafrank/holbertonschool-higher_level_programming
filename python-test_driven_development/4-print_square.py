#!/usr/bin/python3

def print_square(size):
    if any([isinstance(size, t) for t in [int, float]]):
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            size = int(size)
            for i in range(size):
                print("#" * size)
    else:
        raise TypeError("size must be an integer")
