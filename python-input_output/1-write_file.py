#!/usr/bin/python3

def write_file(filename="", text=""):
    if not filename:
        return

    with open(filename, "w") as f:
        chars_written = f.write(text)
        return chars_written
