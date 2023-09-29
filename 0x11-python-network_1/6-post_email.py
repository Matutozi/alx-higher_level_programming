#!/usr/bin/python3
"""Send POST request to passed url"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    param = {'email': sys.argv[2]}

    r = requests.post(url, data=param)
    print(r.text)
