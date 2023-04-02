#!/usr/bin/python3
"""
Module: calculator
Function: add_integer(a, b=98)
"""
def test_add_integer():
  """Returns the addition of two numbers."""
    assert add_integer(2, 3) == 5
    assert add_integer(2.5, 3.5) == 5
    try:
        add_integer(2, '3')
    except TypeError as e:
        assert str(e) == "b must be an integer"
    try:
        add_integer([2], 3)
    except TypeError as e:
        assert str(e) == "a must be an integer"
