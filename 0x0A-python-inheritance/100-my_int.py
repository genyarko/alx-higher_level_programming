#!/usr/bin/python3
"""
a class MyInt that inherits from int
"""

class MyInt(int):
    """A rebel class of int with inverted == and != operators"""
    def __eq__(self, other):
        """Inverts the == operator"""
        return int(self) != int(other)
    
    def __ne__(self, other):
        """Inverts the != operator"""
        return int(self) == int(other)
