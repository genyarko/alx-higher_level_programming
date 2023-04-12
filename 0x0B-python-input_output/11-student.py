#!/usr/bin/python3
"""
Contains the clas "Student"
"""
class Student:
    """
    A class representing a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        """
        Initializes a new instance of the Student class.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None) -> dict:
        """
        Returns a dictionary representation of the student instance.

        Args:
            attrs (Optional[List[str]]): A list of attribute names to include in the dictionary.
                If None, all attributes will be included. Defaults to None.

        Returns:
            dict: A dictionary representation of the student instance.
        """
        if attrs is not None:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        else:
            return self.__dict__

    def reload_from_json(self, json: dict) -> None:
        """
        Replaces all attributes of the student instance with those from a dictionary.

        Args:
            json (dict): A dictionary containing attribute names and values.
                Each key corresponds to an attribute name and each value to its value.
        """
        for key, value in json.items():
            setattr(self, key, value)
