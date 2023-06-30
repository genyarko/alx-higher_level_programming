#!/usr/bin/python3
"""Displays the user ID using GitHub API and Basic Authentication.
Usage: ./github_id.py <username> <personal_access_token>
"""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    access_token = sys.argv[2]

    url = "https://api.github.com/user"
    headers = {
        "Accept": "application/vnd.github.v3+json",
    }
    auth = (username, access_token)

    response = requests.get(url, headers=headers, auth=auth)
    if response.status_code == 200:
        data = response.json()
        user_id = data["id"]
        print(f"User ID: {user_id}")
    else:
        print(f"Error: {response.status_code} - {response.text}")
