#!/usr/bin/python3
"""Sends a request to a given URL and displays the value of the X-Request-Id header variable.

Usage: ./5-hbtn_header.py <URL>
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))
