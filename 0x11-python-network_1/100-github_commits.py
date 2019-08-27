#!/usr/bin/python3
""" This is a script that takes input from the user:
- repository name
- owner name
and prints all commits by <sha>: <author name>
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2],
                                                              sys.argv[1])
    r = requests.get(url)
    for i in r.json()[:10]:
        print("{}: {}".format(i.get('sha'),
                              i.get('commit').get('author').get('name')))
