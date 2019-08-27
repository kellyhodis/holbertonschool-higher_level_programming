#!/usr/bin/python3
""" This is a script that takes in a URL and email address, sends a POST
request to the passed URL with email as parameter, and displays the body
of the response.
"""
import sys
import requests


if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
