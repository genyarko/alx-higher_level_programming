#!/usr/bin/python3
"""
contain the JSON string
"""

import json

def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON string.
    """
    return json.loads(my_str)
