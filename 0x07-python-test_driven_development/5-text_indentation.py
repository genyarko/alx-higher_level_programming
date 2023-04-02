#!/usr/bin/python3
"""
This is the "5-test_indentation" module.
The 5-text_indentation module supplies one function, text_indentation(text).
"""
def text_indentation(text):
"""splits a text into lines along "?", ":", "." followed by 2 new lines"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":  # iterate over the characters to replace
        text = text.replace(char, char + "\n\n")

    # remove any leading/trailing whitespaces and print the result
    print(text.strip())
