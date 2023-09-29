#!/usr/bin/python3
"""Script that takes url and display value of X-Request-Id found in response"""

import sys
from urllib import request


if __name__ == "__main__":
    url = sys.argv[1]
    with request.urlopen(url) as resp:
        html = resp.info().get('X-Request-Id')
        print(html)
