#!/usr/bin/python3

import requests
import sys

repository = sys.argv[1]
owner = sys.argv[2]

url = f'https://api.github.com/repos/{owner}/{repository}/issues'

response = requests.get(url)

if response.status_code == 200:
    issues = response.json()
    for issue in issues:
        print("Issue:", issue['title'])
else:
    print("Failed to retrieve issues. Status code:", response.status_code)
