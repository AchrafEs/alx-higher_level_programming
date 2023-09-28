#!/bin/bash
# Send GET request to a URL with the X-School-User-Id header and display the response body
curl -s -I -H "X-School-User-Id: 98" "$1" | awk -F': ' '/^X-School-User-Id/{print $2}' | tr -d '\r
