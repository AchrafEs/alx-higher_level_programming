#!/bin/bash
# a script that takes in a URL and displays all HTTP methods the server will accept.
curl -s -I 'http://0.0.0.0:5000' | awk -F': ' '/^Allow/{print $2}'
