#!/usr/bin/python3
"""
Module for BaseGeometry
"""


class BaseGeometry:
    """Contains function area(), integer_validator()
    """

    def area(self):
        """Funtion not implemented yet
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function that validates `value`
        """

        if type(value) != int:
            raise TypeError(name + " must be an integer")

        if value <= 0:
            raise ValueError(name + " must be greater than 0")
