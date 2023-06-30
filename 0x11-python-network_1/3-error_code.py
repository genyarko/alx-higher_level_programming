#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.

Usage: ./4-hbtn_status.py <URL>
    - Displays the body of the response (decoded in utf-8).
    - Handles HTTP errors and prints the error code.
"""

import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))

