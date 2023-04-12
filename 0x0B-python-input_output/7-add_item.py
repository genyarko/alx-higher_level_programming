#!/usr/bin/python3
"""
a script
"""

import json

def load_from_json_file(filename):
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)
