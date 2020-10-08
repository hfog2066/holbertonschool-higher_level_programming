#!/usr/bin/python3
"""
write_file
"""


def write_file(filename="", text=""):
    """str filename to read, and str next to write
    """

    with open(filename, mode="w", encoding="utf-8") as writeFile:
        writeFile.write(text)
        return len(text)
