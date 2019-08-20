#!/bin/bash
# Takes in URL, sends GET request to URL, and displays body response.
curl -X GET -H 'X-HolbertonSchool-User-Id:98' "$1"
