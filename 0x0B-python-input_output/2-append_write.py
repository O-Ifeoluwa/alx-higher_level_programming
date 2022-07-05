#!/usr/bin/python3
"""append to a file function"""


def append_write(filename="", text=""):
    """appends strings to the end of a text file"""

    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return (len(text))
