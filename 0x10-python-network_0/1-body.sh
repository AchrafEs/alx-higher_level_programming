#!/bin/bash
# a cript that takes in a URL, sends a GET request to the URL, and displays the body of the response
(curl -s -I "$1" | grep -q "HTTP/1.1 200" && curl -s "$1") ; echo ""
