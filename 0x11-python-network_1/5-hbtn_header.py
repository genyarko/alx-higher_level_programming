#!/usr/bin/python3
"""Sends a request to a given URL and displays the value of the X-Request-Id header.

Usage: ./1-hbtn_header.py <URL>
    - Displays the value of the X-Request-Id header in the response.
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    x_request_id = response.headers.get("X-Request-Id")

    print(x_request_id)
