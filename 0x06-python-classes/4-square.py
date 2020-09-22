#!/usr/bin/python3
"""
Square Module - for all your needs, as long as they include printing squares!
"""


class Square:
    """
    Square class now has cool setters and getters for the size!
    """
    def __init__(self, size=0):
        """
        Square class init! Takes in a size.
        """
        self.size = size

    @property
    def size(self):
        """
        Size getter, returns the private size.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Size setter, sets the size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the area of the square.
        """
        return (self.__size ** 2)
