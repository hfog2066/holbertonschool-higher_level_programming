#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    j = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                j += 1
                print("")
                return j
    except (TypeError, ValueError):
        if isinstance(my_list, list):
            print("")
            return j
