#!/usr/bin/python3
"""

class Square:
    """
    A class used to represent a square

    Attributes
    ----------
    size : int
        The side length of the square

    Methods
    -------
    area()
        Returns the area of the square
    perimeter()
        Returns the perimeter of the square
    """

    def __init__(self, size=0):
        """
        Parameters
        ----------
        size : int, optional
            The side length of the square (default is 0)

        Raises
        ------
        TypeError
            If size is not an integer
        ValueError
            If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """
        Returns the side length of the square

        Returns
        -------
        int
            The side length of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the side length of the square

        Parameters
        ----------
        value : int
            The side length of the square

        Raises
        ------
        TypeError
            If size is not an integer
        ValueError
            If size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the area of the square

        Returns
        -------
        int
            The area of the square
        """
        return self.__size ** 2

    def perimeter(self):
        """
        Returns the perimeter of the square

        Returns
        -------
        int
            The perimeter of the square
        """
        return self.__size * 4
