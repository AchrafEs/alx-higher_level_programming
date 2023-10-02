#!/bin/bash
# Send a request to a URL and display only the status code
[ $# -ne 1 ] && echo "Usage: $0 <URL>" || response=$(curl -s -o /dev/null -w "%{http_code}" "$1") && echo "Status Code: $response"
