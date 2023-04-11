#!/usr/bin/python3
"""
Contains the class BaseGeometry and subclass Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initializes a new Rectangle instance with given width and height"""
        self.__width = self.integer_validator('width', width)
        self.__height = self.integer_validator('height', height)

    def __str__(self):
        """Returns a string representation of the Rectangle instance"""
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)

    def area(self):
        """Computes the area of the Rectangle instance"""
        return self.__width * self.__height

