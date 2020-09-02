#!/usr/bin/python3

def uppercase(str):
    for c in str:
        c = ord(c)

        if ord('a') <= c <= ord('z'):
            c = c - 32

            print("{:c}".format(c), end='')
