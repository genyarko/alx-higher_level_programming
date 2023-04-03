#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    """Class that represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new instance of the Rectangle class"""
        self.width = width
        self.height = height

    def __del__(self):
        """Destructor for the Rectangle class"""
        print("Bye rectangle...")

    @property
    def width(self):
        """Get the value of the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the value of the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        for i in range(self.__height):
            rectangle += "#" * self.__width + "\n"
        return rectangle[:-1]

    def __repr__(self):
        """Return a string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
