#!/bin/bash
# Sends a request to URL passed and displays status code of response.
curl -Ls -o /dev/null -w "%{http_code}" -X GET "$1"
