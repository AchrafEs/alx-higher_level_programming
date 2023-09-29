#!/usr/bin/python3
"""
Lists the 10 most recent commits of a GitHub repository.

This script takes two arguments: the repository name and the owner name.
It uses the GitHub API to fetch and print the 10 most recent commits of
the specified repository by the specified owner.
"""

import requests
import sys


def list_recent_commits(repo, owner):
    # GitHub API URL for fetching commits
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    try:
        # Send a GET request to the GitHub API
        response = requests.get(url)

        # Check for a successful response (status code 200)
        if response.status_code == 200:
            commits = response.json()[:10]  # Get the most recent 10 commits

            # Print each commit in the specified format
            for commit in commits:
                sha = commit['sha']
                author_name = commit['commit']['author']['name']
                print(f"{sha}: {author_name}")
        else:
            print("Error: HTTP Status Code", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    # Check if two arguments (repo and owner) are provided
    if len(sys.argv) != 3:
        print("Usage: {} <repository_name> <owner_name>".format(sys.argv[0]))
        sys.exit(1)

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Call the function to list recent commits
    list_recent_commits(repo_name, owner_name)
