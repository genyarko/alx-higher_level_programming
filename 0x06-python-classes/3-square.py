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

    def __init__(self, size=0):
        """
        initializes square
        Args:
             The side length of the square (default is 0)
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """
        Returns the area of the square
        Returns
        -------
        int
            The area of the square
        """

        return self.__size ** 2
