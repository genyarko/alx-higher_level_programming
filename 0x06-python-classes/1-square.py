#!/usr/bin/python3


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

    def __init__(self, size):
        """
        Parameters
        ----------
        size : int
            The side length of the square
        """
        self.__size = size

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
