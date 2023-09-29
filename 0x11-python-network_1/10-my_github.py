#!/usr/bin/python3
"""
Uses the GitHub API to display your GitHub user ID.

This script takes your GitHub username as the first argument and your personal
access token (used as a password) as the second argument. It uses Basic
Authentication to access your GitHub information and displays your user ID.
"""

import requests
import sys

try:
    letter = sys.argv[1]
except IndexError:
    letter = ""

headers = {"Content-Type": "application/json"}
data = {"q": letter}
response = requests.post(
        "http://0.0.0.0:5000/search_user", headers=headers, json=data)

# Check if the response body is properly JSON formatted and not empty.
if response.ok and response.headers["Content-Type"] == "application/json":
    try:
        json_data = response.json()

        # If the JSON is empty, display No result.
        if len(json_data) == 0:
            print("No result")
        else:
            # Display the id and name of the user like this: [<id>] <name>
            for user in json_data:
                print("[{}] {}".format(user["id"], user["name"]))
    except json.JSONDecodeError as e:
        print("Not a valid JSON: {}".format(e))
else:
    print("Error: {}".format(response.status_code))
