#!/bin/bash
# aa Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -s -I -H "X-School-User-Id: 98" "$1" | awk -F': ' '/^X-School-User-Id/{print $2}' | tr -d '\r'
