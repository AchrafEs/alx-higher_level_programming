#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user with
a letter parameter and processes the response.

This script takes a letter as input, sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter, and displays
the response according to the specified conditions. It uses the requests and
sys packages for making the HTTP request, handling command-line arguments, and
processing JSON responses from the server.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""

    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': letter}

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()

        try:
            json_response = response.json()
            if json_response:
                print("[{}] {}".format(
                    json_response['id'],
                    json_response['name']
                ))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
