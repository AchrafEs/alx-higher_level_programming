#!/bin/bash
# Send GET request to a URL and display response body for HTTP 200 status code
[ $# -ne 1 ] && echo "Usage: $0 <URL>" || { http_code=$(curl -s -o /dev/null -w "%{http_code}" "$1"); [ "$http_code" -eq 200 ] && curl -s "$1"; }
