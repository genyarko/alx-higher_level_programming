#!/usr/bin/python3
"""
writes a string to a text file (UTF8) and returns the number of characters written
"""

def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        num_chars_written = f.write(text)
    return num_chars_written
