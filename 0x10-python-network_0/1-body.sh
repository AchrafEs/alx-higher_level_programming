#!/bin/bash
# Send GET request to a URL and display response body for HTTP 200 status code
[ $# -ne 1 ] && echo "Usage: $0 <URL>" || { url="$1"; while [ $(curl -s -o /dev/null -w "%{http_code}" -L -I "$url") -ge 300 ]; do url=$(curl -s -o /dev/null -w "%{redirect_url}" -L -I "$url"); done; curl -s "$url"; }
