#!/bin/bash
# Send a JSON POST request to a URL with the contents of a file in the request body
curl -s -X POST -d "@$2" -H "Content-Type: application/json" "$1"
