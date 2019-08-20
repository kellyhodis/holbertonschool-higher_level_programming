#!/bin/bash
# Sends a request to URL passed and displays status code of response.
curl -LIs -o /dev/null -w "%{http_code}" "$1"
