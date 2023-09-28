#!/bin/bash

# Check if a host:port is provided as an argument
if [ $# -ne 1 ]; then
  echo "Usage: $0 <host:port>"
  exit 1
fi

host_port="$1"

# Use curl with -s to fetch the response and store the size of the response body in bytes
body_size=$(curl -s "$host_port" | wc -c)
echo "$body_size"
