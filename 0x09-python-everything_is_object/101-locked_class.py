#!/usr/bin/python3
"""

This module contains a class avoids
dynamically attributes

"""


class LockedClass:
    def __setattr__(self, attribute, value):
        if attribute == "first_name":
            self.__dict__[attribute] = value
        else:
            raise AttributeError("'LockedClass' object has no attribute '" + attribute + "'")
