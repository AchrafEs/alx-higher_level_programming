#!/bin/bash
# Display all HTTP methods accepted by the server for a given URL
curl -s -I -X OPTIONS "$1" | grep -i "Allow"
