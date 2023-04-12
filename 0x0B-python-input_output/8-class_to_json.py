#!/usr/bin/python3
"""
a function that returns the dictionary description
"""
def class_to_json(obj):
    """Returns a dictionary description of a class object with simple data structures for JSON serialization"""
    json_dict = {}
    for attr, value in obj.__dict__.items():
        if isinstance(value, (int, str, bool, list, dict)):
            json_dict[attr] = value
    return json_dict
