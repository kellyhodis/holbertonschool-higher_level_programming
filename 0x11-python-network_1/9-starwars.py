#!/usr/bin/python3
""" This is a script that takes in a string and sends a search to the
Star Wars API.
"""
import sys
import requests


if __name__ == "__main__":
    r = requests.get('https://swapi.co/api/people/',
                     params={'search': sys.argv[1]})
    print("Number of results: {}".format(r.json()['count']))
    for item in range(len(r.json()['results'])):
        print("{}".format(r.json()['results'][item]['name']))
