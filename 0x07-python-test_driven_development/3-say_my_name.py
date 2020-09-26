#!/usr/bin/python3

"""
This module contains - say_my_name function.
"""


def say_my_name(first_name, last_name=""):
    """
    Print "My name is <first name> <last name>".
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print("My name is " + first_name + " " + last_name)
