#!/usr/bin/python3
""" This is a script that takes Github credentials from the user and
uses the Github API to display the user id.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = "https://api.github.com/users/" + sys.argv[1]
    r = requests.get(url, auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    print(r.json()['id'])
