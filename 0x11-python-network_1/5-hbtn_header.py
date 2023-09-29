#!/usr/bin/python3
"""
Sends a request to a URL and displays the value of the X-Request-Id
variable in the response header.

This script takes a URL as input, sends a request to that URL using the
requests package, and displays the value of the X-Request-Id variable
found in the response header.
"""

import requests
import sys

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()

        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(x_request_id)
        else:
            print("X-Request-Id header not found in the response.")
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
