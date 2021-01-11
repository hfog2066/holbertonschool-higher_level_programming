#!/usr/bin/python3

"""
sends a request
"""

import urllib.request
from sys import argv

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as f:
        print(f.headers.get('X-Request-Id'))
