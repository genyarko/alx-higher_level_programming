#!/usr/bin/python3
"""
Contains a function that appends a string
"""
def append_write(filename="", text=""):
    """
    Appends a string to a text file (UTF8) and returns the number of characters added.
    If the file doesn't exist, it is created.
    """
    with open(filename, "a", encoding="utf-8") as f:
        num_chars_added = f.write(text)
    return num_chars_added
