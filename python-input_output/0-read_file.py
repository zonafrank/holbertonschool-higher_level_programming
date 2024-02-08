#!/usr/bin/python3
"""Module for function read_file"""


def read_file(filename=""):
    """reads from a file

    Args:
        filename (string): name of the file to read
    """
    if filename:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                print(line, end="")
