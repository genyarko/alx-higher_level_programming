#!/usr/bin/python3
"""Sends a POST request to a given URL with an email as a parameter and displays the response body.

Usage: ./2-post_email.py <URL> <email>
    - Sends a POST request to the specified URL with the email as a parameter.
    - Displays the body of the response.
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {"email": email}
    response = requests.post(url, data=payload)

    print(response.text)
