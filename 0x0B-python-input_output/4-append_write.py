#!/usr/bin/python3
"""
append_write
"""


def append_write(filename="", text=""):
    """str filename to write, str text to append to file
    """

    with open(filename, mode="a", encoding="utf-8") as appendFile:
        appendFile.write(text)
        return len(text)
