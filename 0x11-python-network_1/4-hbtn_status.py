#!/usr/bin/python3
"""Fetches the status from https://alx-intranet.hbtn.io/status.

Usage: ./4-hbtn_status.py
"""

import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
