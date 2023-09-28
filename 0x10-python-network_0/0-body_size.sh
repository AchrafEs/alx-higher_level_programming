#!/bin/bash
# a script that takes in a URL and displays all HTTP methods the server will accept.

host_port="$1"

body_size=$(curl -s "$host_port" | wc -c)
echo "$body_size"
