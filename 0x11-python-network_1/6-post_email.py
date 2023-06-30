#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email and displays the response body.

Usage: ./2-post_email.py <URL> <email>
    - Displays the body of the response.
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {"email": email}
    response = requests.post(url, data=data)

    print(response.text)
