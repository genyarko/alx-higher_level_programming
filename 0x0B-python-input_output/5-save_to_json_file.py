#!/usr/bin/python3
"""
object to text
"""
import json

def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file using a JSON representation.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
