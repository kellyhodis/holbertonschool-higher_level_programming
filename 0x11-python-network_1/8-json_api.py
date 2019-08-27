#!/usr/bin/python3
""" This is a script that takes in a letter and sends a POST request to
https://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    try:
        qy = sys.argv[1]
    except IndexError:
        qy = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': qy})
    if r.headers['content-type'] == 'application/json':
        if "id" in r.json():
            print("[{}] {}".format(r.json()['id'], r.json()['name']))
        else:
            print("No result")
    else:
        print("Not a valid JSON")
