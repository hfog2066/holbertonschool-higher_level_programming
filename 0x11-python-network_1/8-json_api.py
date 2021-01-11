#!/usr/bin/python3

"""
json api
"""

import requests
from sys import argv

if __name__ == "__main__":
    data = {'q': ""}
    if len(argv) > 1:
        data['q'] = argv[1]
    r = requests.post("http://0.0.0.0:5000/search_user", data)
    if "json" not in r.headers.get('content-type'):
        print("Not a valid JSON")
    else:
        if r.json():
            print("[{}] {}".format(r.json().get('id'), r.json().get('name')))
        else:
            print("No result")
