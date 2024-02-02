#!/usr/bin/python3
""" Module for ``text_indentation`` function"""


def text_indentation(text):
    """
    prints out text passed in as argument.
    It inserts two newline characters after each '.' or '?'

    Args:
        text (string): a text string to print out

    Returns:
        Nothing
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()
    if not text:
        print()

    for idx, char in enumerate(text):
        if idx > 0 and char == " " and text[idx - 1] in ".?:":
            continue
        print(char, end="")
        if (char in ".?:"):
            print("\n")
