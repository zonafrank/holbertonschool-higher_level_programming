#!/usr/bin/python3
"""Module for function append_write"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)
    and returns the number of characters added

    Args:
        filename (str): name of the file to append text to
        text (str): text to append to the file

    Return:
        int: number of characters added to filename
    """
    if not filename:
        return
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
