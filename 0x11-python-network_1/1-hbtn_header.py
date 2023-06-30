#!/usr/bin/python3
"""Sends a request to the given URL and displays the value of the X-Request-Id variable.

Usage: ./2-hbtn_status.py <URL>

This script takes a URL as input, sends a request to the URL using urllib, and displays
the value of the X-Request-Id variable found in the header of the response.

Note:
    The value of the X-Request-Id variable is different for each request.

Arguments:
    <URL>: The URL to send the request to.

Example:
    ./2-hbtn_status.py https://example.com
"""

import sys
import urllib.request

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-hbtn_status.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        x_request_id = response.getheader("X-Request-Id")
        print(x_request_id)
