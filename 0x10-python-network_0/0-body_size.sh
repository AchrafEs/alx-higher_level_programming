#!/bin/bash

# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

url="$1"

# Use curl to fetch the URL and store the response in a temporary file
response_file=$(mktemp)
curl -s -o "$response_file" "$url"

# Check if the request was successful (HTTP status 200 OK)
http_status=$(curl -s -o /dev/null -w "%{http_code}" "$url")

if [ "$http_status" -eq 200 ]; then
  # Get the size of the response body in bytes
  body_size=$(wc -c < "$response_file")
  echo "Size of the response body: $body_size bytes"
else
  echo "Error: HTTP request failed with status code $http_status"
fi

# Clean up by removing the temporary response file
rm "$response_file"
