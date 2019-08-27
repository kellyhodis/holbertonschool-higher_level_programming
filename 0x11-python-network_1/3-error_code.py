#!/usr/bin/python3
""" This is a script that takes in a URL, sends a request to the URL
and displays the body of the response decoded in utf-8.
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as x:
            print(x.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
