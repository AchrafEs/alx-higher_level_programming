#!/bin/bash
# Display all HTTP methods accepted by the server for a given URL
curl -s -X OPTIONS -i "$1" | awk -F': ' '/^Allow/{print $2}' | tr -d '\r'
