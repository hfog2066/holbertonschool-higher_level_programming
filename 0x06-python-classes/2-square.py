#!/usr/bin/python3
"""
Square Module - for all your needs, as long as they include printing squares!
"""


class Square:
    """
    Square class: now setting your size to 0 if you don't provide it, and doing
    basic error checking!
    """
    def __init__(self, size=0):
        """
        Init for Square class. Basic error checking for int size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
