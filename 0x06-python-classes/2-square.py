#!/usr/bin/python3
""" A class used to represent a square """


class Square:
    """ square with private instance attribute size """

    def __init__(self, size=0):
        """
        Args:
            The side length of the square
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
