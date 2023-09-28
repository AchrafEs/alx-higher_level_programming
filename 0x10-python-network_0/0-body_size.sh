#!/bin/bash
# a script that takes in a URL and displays all HTTP methods the server will accept.
curl -s "$1" | wc -c
