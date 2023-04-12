#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then saves them to a file
"""

import sys
from load_from_json_file import load_from_json_file
from save_to_json_file import save_to_json_file

filename = "add_item.json"

try:
    json_list = load_from_json_file(filename)
except FileNotFoundError:
    json_list = []

for arg in sys.argv[1:]:
    json_list.append(arg)

save_to_json_file(json_list, filename)
