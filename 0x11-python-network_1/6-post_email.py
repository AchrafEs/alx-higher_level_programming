#!/usr/bin/python3
"""
Sends a POST request to a URL with an email parameter and
displays the response body.

This script takes a URL and an email address as input arguments, sends
a POST request to the specified URL with the email as a parameter, and
displays the body of the response. It uses the requests and sys packages
for making the HTTP request and handling command-line arguments.
"""

import requests
import sys

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()

        response_data = response.text
        print(response_data)
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
