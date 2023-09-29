#!/usr/bin/python3
"""
Sends a request to a URL and displays the value of the
X-Request-Id header variable.

This script takes a URL as input, sends a request to that URL, and displays the
value of the X-Request-Id header found in the response. It uses the urllib and
sys packages for the HTTP request and command-line argument handling.
"""

import urllib.request
import sys

if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.getheader('X-Request-Id')
            if x_request_id:
                print(x_request_id)
            else:
                print("X-Request-Id header not found in the response.")
    except urllib.error.URLError as e:
        print("Error: {}".format(e.reason))
