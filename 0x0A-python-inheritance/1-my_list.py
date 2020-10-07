#!/usr/bin/python3

"""
MyList module

"""


class MyList(list):
    """Contains list. """

    def print_sorted(self):
        """Print the list, but sorted ascending sort."""

        print(sorted(self))
