#!/usr/bin/python3

import requests
import sys

username = sys.argv[1]
token = sys.argv[2]

url = 'https://api.github.com/user'

response = requests.get(url, auth=(username, token))

if response.status_code == 200:
    user_info = response.json()
    print("Your user id is:", user_info['id'])
else:
    print("Failed to retrieve user information. Status code:", response.status_code)
