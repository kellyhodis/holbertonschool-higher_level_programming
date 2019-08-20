#!/usr/bin/env bash
# Takes in a URL, sends request to URL, and displays size of body of response.
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
