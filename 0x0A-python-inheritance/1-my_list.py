#!/usr/bin/python3

"""
This is a module for MyList.
"""


class MyList(list):
    """A MyList class."""

    def print_sorted(self):
        """print the list, but sorted (ascending sort)."""
        print(sorted(self))
