#!/usr/bin/python3

""" function that returns True if the object is exactly an instance of the specified class ; otherwise False """

def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class; otherwise False.
    """
    return type(obj) is a_class
