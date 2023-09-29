#!/usr/bin/python3
"""
Uses the GitHub API to display your GitHub user ID.

This script takes your GitHub username as the first argument and your personal
access token (used as a password) as the second argument. It uses Basic
Authentication to access your GitHub information and displays your user ID.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    username = sys.argv[1]
    access_token = sys.argv[2]

    # Construct the URL for the authenticated user's GitHub information
    url = 'https://api.github.com/user'

    auth = (username, access_token)

    try:
        # Send a GET request to the GitHub API
        response = requests.get(url, auth=auth)

        # Check for a successful response (status code 200)
        if response.status_code == 200:
            user_info = response.json()
            user_id = user_info.get('id')
            if user_id:
                print("Your GitHub user ID is: {}".format(user_id))
            else:
                print("User ID not found in the response.")
        else:
            print("Error: HTTP Status Code {}".format(response.status_code))
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
