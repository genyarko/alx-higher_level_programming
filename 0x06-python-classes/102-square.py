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
        Parameters
        ----------
        size : int, optional
            The side length of the square (default is 0)

        Raises
        ------
        TypeError
            If size is not a number
        ValueError
            If size is less than 0
        """
        if not isinstance(size, (int, float)):
            raise TypeError("size must be a number")
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
            If size is not a number
        ValueError
            If size is less than 0
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
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

    def __eq__(self, other):
        """
        Compares to squares based on their area

        Parameters
        ----------
        other : object
            The object to compare

        Returns
        -------
        bool
            True if the area of self is equal to the area of other, otherwise False
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compares to squares based on their area

        Parameters
        ----------
        other : object
            The object to compare

        Returns
        -------
        bool
            True if the area of self is not equal to the area of other, otherwise False
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Compares to squares based on their area

        Parameters
        ----------
        other : object
            The object to compare

        Returns
        -------
        bool
            True if the area of self is greater than the area of other, otherwise False
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compares to squares based on their area

        Parameters
        ----------
        other : object
            The object to compare

        Returns
        -------
        bool
            True if the area of self is greater than or equal to the area of other, otherwise False
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Compares to squares based on their area

        Parameters
        ----------
        other : object
            The object to compare

        Returns
        -------
        bool
            True if the area of self is less than the area of other, otherwise False
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compares to squares based on their area

        Parameters
        ----------
        other : object
            The object to compare

        Returns
        -------
        bool
            True if the area of self is less than or equal to the area of other, otherwise False
        """
        return self.area() <= other.area()
