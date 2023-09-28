#!/bin/bash
# a script that takes in a URL and displays all HTTP methods the server will accept.

if [ $# -ne 1 ]; then
  echo "Usage: $0 <host:port>"
  exit 1
fi

host_port="$1"

body_size=$(curl -s "$host_port" | wc -c)
echo "$body_size"
