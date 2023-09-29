#!/usr/bin/python3
"""Script sends POST request to a passed URL with an email parameter
   Displays the body of the response
"""
import sys
from urllib import request, parse


if __name__ == "__main__":
    url = sys.argv[1]
    param = parse.urlencode({'email': sys.argv[2]}).encode('utf-8')

    req = request.Request(url, param)
    with request.urlopen(req) as response:
        html = response.read()
        print("{}".format(html.decode('utf-8')))
