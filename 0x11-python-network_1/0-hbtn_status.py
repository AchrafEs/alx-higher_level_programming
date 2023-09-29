#!/usr/bin/python3

"""
Fetches the URL using urllib and displays response.

This script uses the urllib package to fetch the status from the specified URL
and displays information about the response, including its type and content.
"""

import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(data)))
            print("\t- content: {}".format(data.decode('utf-8')))
            print("\t- utf8 content: {}".format(data.decode('utf-8')))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
    except urllib.error.URLError as e:
        print("Error: {}".format(e.reason))

if __name__ == "__main__":
    print(__doc__)
