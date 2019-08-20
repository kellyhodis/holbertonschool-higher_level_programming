#!/bin/bash
# Sends a request to URL passed and displays status code of response.
curl -s -o /dev/null -w "%{http_code}" -X POST "$1"
