#!/usr/bin/python3
""" This is a script that fetches https://intranet.htbn.io/status.
"""
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as x:
    content = x.read()
    decoded_content = content.decode('utf-8')
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
    print("\t- utf8 content: {}".format(decoded_content))
