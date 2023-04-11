#!/usr/bin/python3
"""
Contains the class BaseGeometry and subclass Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A representation of a square"""
    def __init__(self, size):
        """instantiation of the square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns a string representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
