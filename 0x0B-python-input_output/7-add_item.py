#!/usr/bin/python3
"""
a script
"""

import sys
import json
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

# Try to load existing data from file
try:
    data = load_from_json_file("add_item.json")
except:
    data = []

# Add new arguments to the list
for arg in sys.argv[1:]:
    data.append(arg)

# Save the updated data to file
save_to_json_file(data, "add_item.json")
