#!/usr/bin/python3
"""Send POST request with letter as parameter"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        param = {'q': sys.argv[1]}
    else:
        param = {'q': ''}

    r = requests.post('http://0.0.0.0:5000/search_user', data=param)
    try:
        if not r.json():
            print("No result")
        else:
            uid = r.json().get('id')
            name = r.json().get('name')
            print("[{}] {}".format(uid, name))
    except ValueError:
        print("Not a valid JSON")
