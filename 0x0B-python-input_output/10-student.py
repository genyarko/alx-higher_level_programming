#!/usr/bin/python3
"""a class Student."""

class Student:
    """
    A class that defines a student by their first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with the given first name, last name, and age.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of attribute names to retrieve. If not provided, retrieves all attributes.

        Returns:
            A dictionary containing the requested attributes and their values.
        """
        if attrs is None:
            # if no attributes are specified, return all attributes as a dictionary
            return self.__dict__
        else:
            # filter the dictionary to only include the requested attributes
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
