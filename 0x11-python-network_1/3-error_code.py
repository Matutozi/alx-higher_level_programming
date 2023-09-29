#!/usr/bin/python3
"""Script that takes url and displays body of the response"""

import sys
from urllib import request, error


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as resp:
            html = resp.read().decode('utf-8')
            print(html)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
