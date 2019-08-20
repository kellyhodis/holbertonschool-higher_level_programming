#!/bin/bash
# Sends a JSON POST request to a URL and displays response body.
curl -s -H "Content-Type: application/json" -d @"$2" -X POST "$1"
