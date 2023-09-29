#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response in utf-8

This script takes a URL as input, sends a request to that URL, and displays
the body of the response (decoded in utf-8). It handles HTTP errors and prints
the HTTP status code in case of an error. It uses the urllib and sys packages
for the HTTP request and command-line argument handling.
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    # Check if a URL is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            response_data = response.read()
            print(response_data.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
    except urllib.error.URLError as e:
        print("Error: {}".format(e.reason))
