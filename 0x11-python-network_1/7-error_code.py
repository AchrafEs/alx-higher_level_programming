#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response.
Handles HTTP errors.

This script takes a URL as input, sends a request to that URL using
the requests package, displays the body of the response, and prints the
error code if the HTTP status code is greater than or equal to 400.
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

        if response.status_code >= 400:
            print("Error code: {}".format(response.status_code))
        else:
            print(response.text)
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
