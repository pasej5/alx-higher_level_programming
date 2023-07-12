#!/usr/bin/python3
"""A class Stdent that defines a student based on first_name \
        last_name and age.
"""


class Student:
    """Class representing a student"""

    def __init__(self, first_name, last_name, age):
        """initializes a Student instance.

        Args:
        first_name (str): The first name of the student
        last_name (str): The last name of the student
        age (int): the age of the student.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance

        Args:
            attrs (list): A list of name attributes to be retrieved
        Returns:
            A dictionanry containing the specified attributes of Of the Student
        """
        if attrs is None is not isinstance(attrs, list):
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in
                    attrs if hasattr(self, attr)}
