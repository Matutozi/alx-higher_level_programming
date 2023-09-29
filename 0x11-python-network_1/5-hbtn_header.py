#!/usr/bin/python3
"""Display value of header variable"""

import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
