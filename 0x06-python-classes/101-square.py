#!/usr/bin/python3
class Square:
    """
    A class used to represent a square

    Attributes
    ----------
    size : int
        The side length of the square
    position : tuple
        The position of the top-left corner of the square

    Methods
    -------
    area()
        Returns the area of the square
    my_print()
        Prints the square in stdout
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Parameters
        ----------
        size : int, optional
            The side length of the square (default is 0)
        position : tuple, optional
            The position of the top-left corner of the square (default is (0, 0))

        Raises
        ------
        TypeError
            If size is not an integer
            If position is not a tuple of 2 positive integers
        ValueError
            If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple) or len(position) != 2 or \
           not all(isinstance(num, int) and num >= 0 for num in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Returns the position of the top-left corner of the square

        Returns
        -------
        tuple
            The position of the top-left corner of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the top-left corner of the square

        Parameters
        ----------
        value : tuple
            The position of the top-left corner of the square

        Raises
        ------
        TypeError
            If position is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns the area of the square

        Returns
        -------
        int
            The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square in stdout

        If size is 0, prints an empty line
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
