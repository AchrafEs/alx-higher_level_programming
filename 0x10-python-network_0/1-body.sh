#!/bin/bash
# Send GET request to a URL and display response body for HTTP 200 status code
curl -s -I "$1" | grep -q "HTTP" && curl -s "$1"
