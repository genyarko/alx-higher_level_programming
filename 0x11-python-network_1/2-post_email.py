#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email and displays the response body.

Usage: ./3-post_request.py <URL> <email>
    - Displays the body of the response (decoded in utf-8).
"""

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    values = {"email": email}
    data = urllib.parse.urlencode(values).encode("utf-8")

    request = urllib.request.Request(url, data=data, method="POST")
    with urllib.request.urlopen(request) as response:
        body = response.read().decode("utf-8")
        print(body)
