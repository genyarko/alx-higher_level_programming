#!/usr/bin/python3
"""
Contains the lookup function
"""

def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a subclass of a_class; otherwise False.
    """
    return isinstance(obj, type) and issubclass(obj, a_class)
