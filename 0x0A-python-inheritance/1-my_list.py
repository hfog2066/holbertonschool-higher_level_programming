#!/usr/bin/python3
"""
Module for MyList
"""


class MyList(list):
     """
        Prints self in sorted format
     """

    def print_sorted(self):
        print(sorted(self))
