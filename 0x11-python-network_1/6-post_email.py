#!/usr/bin/python3

"""
display body response post
"""

import requests
from sys import argv

if __name__ == "__main__":
    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)
