#!/usr/bin/python3
"""Module for the function write_file"""


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8)
    and returns the number of characters written:

    Args:
        filename (str): name of file to write to

    Return:
        int: number of characters written to filname
    """
    if not filename:
        return

    with open(filename, "w") as f:
        chars_written = f.write(text)
        return chars_written
