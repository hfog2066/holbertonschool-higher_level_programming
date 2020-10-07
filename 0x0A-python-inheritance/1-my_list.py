#!/usr/bin/python3

"""
Mylist module.
"""


class Mylist(list):
    """Mylist class."""

    def print_sorted(self):
        """print list, sorted ascending sort."""
        print(sorted(self))
