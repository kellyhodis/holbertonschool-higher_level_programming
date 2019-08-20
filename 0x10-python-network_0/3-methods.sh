#!/bin/bash
# Takes in a URL and displays all HTTP methods server will accept
curl -si -X "OPTIONS" "$1" | grep Allow: | awk {'print $2, $3, $4}'
