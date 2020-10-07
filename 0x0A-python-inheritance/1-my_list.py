#!/usr/bin/python3

"""
This is module for MyList.
"""


class MyList(list):
    """MyList class."""

    def print_sorted(self):
        """print list, sorted ascending sort."""
        print(sorted(self))
