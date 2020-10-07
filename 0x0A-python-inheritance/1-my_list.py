#!/usr/bin/python3
"""Module for MyList"""


class MyList(list):
     """
        Prints self in sorted format
     """

    def print_sorted(self):
         """print_sorted method prints lists in a sorted."""
        print(sorted(self)
