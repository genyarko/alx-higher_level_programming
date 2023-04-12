#!/usr/bin/python3
"""
Creates a python object
"""
import json

def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.
    """
    with open(filename, "r") as f:
        return json.load(f)
