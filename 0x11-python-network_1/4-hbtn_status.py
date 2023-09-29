#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using the requests package.

This script uses the requests package to fetch the status from the
specified URL and displays information about the response, including
its type and content.
"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.text
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
