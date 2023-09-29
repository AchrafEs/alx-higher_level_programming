#!/usr/bin/python3
"""
Sends a POST request to a URL with an email parameter and
displays the response body.

This script takes a URL and an email as input arguments, sends a POST request
to the URL with the email as a parameter, and displays the body of the response
(decoded in utf-8).It uses the urllib and sys packages for the HTTP request,
command-line argument handling, and data encoding.
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    # Check if both a URL and an email are provided as arguments
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary containing the email parameter
    data = {'email': email}
    data = urllib.parse.urlencode(data)
    data = data.encode('utf-8')  # Encode the data as bytes

    try:
        # Send a POST request with the email parameter
        with urllib.request.urlopen(url, data=data) as response:
            response_data = response.read()
            print(response_data.decode('utf-8'))
    except urllib.error.URLError as e:
        print("Error: {}".format(e.reason))
