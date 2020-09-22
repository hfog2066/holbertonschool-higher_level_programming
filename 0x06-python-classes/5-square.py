#!/usr/bin/python3
"""
Square Module - for all your needs, as long as they include printing squares!
"""


class Square:
    """
    Square class, now with a function to print the square!
    """
    def __init__(self, size=0):
        """
        Init for square! Takes in a size, defaults to 0.
        """
        self.__check_size__(size)
        self.__size = size

    @property
    def size(self):
        """
        Size getter, returns the private size.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Size setter, sets the private size.
        """
        self.__check_size__(value)
        self.__size = value

    def area(self):
        """
        Returns the area of the square.
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        Prints the square! Should only print a newline if size is 0.
        """
        print("\n".join("#" * self.__size for i in range(self.__size)))

    def __check_size__(self, size):
        """
        Size error checking!
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
