#!/usr/bin/python3

"""
display x-request-id
"""

import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    print(response.headers.get('x-request-id'))
