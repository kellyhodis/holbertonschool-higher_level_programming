#!/usr/bin/env bash
# Takes in a URL, sends a POST request to URL, and displays response body.

curl -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
