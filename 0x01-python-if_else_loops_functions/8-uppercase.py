#!/usr/bin/python3
def uppercase(str):
    for c in str:
        char = ord(c)
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            char = ord(c) - ord('a') + ord('A')
            print("{:c}".format(char), end="")
            print("".format())
