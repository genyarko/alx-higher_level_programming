#!/usr/bin/python3

import sys
import urllib.request

def fetch_x_request_id(url):
    """
    Fetches the value of the X-Request-Id variable from the header of a response to the given URL.
    
    Args:
        url (str): The URL to send the request to.
    
    Returns:
        str: The value of the X-Request-Id variable.
    """
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        x_request_id = response.getheader("X-Request-Id")
        return x_request_id

if __name__ == "__main__":
    url = sys.argv[1]

    x_request_id = fetch_x_request_id(url)
    print(x_request_id)
