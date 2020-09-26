#!/usr/bin/python3

"""
This module contains - print_square functions.
"""


def print_square(size):
    """
    Print a square with the character #.
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if size == 0:
        return
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
