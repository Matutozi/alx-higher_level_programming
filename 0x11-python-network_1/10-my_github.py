#!/usr/bin/python3
"Use github api to display id, given username and password"

import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    user = sys.argv[1]
    pwd = sys.argv[2]

    r = requests.get(url, auth=(user, pwd))
    if r.json() == {}:
        print("None")
    else:
        print(r.json().get('id'))
