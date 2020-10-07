#!/usr/bin/python3
"""MyList
"""


class MyList(list):
    """Contains list
    """

    def print_sorted(self):
        """Print the list, but
           sorted (ascending sort)
        """

        print(sorted(self))
