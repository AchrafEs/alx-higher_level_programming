#!/bin/bash
# Send GET request to a URL and display response body for HTTP 200 status code
[ $# -ne 1 ] && echo "Usage: $0 <URL>" || { redirections=0; url="$1"; while true; do response=$(curl -s -o /dev/null -w "%{http_code}" -L "$url"); echo "Status Code: $response"; if [ "$response" -eq 200 ]; then break; elif [ "$response" -ge 300 ] && [ "$response" -lt 400 ]; then url=$(curl -s -o /dev/null -w "%{redirect_url}" -L "$url"); echo "Redirecting to: $url"; ((redirections++)); else echo "Error: Unexpected status code $response"; break; fi; done; echo "Total Redirections: $redirections"; }
