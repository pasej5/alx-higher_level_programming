#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    """Class representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of attribute names to be retrieved (optional).

        Returns:
            dict: A dictionary containing attributes of the student.
                  all attributes are retrieved.
        """
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr
                    in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """Replace all Student instance based on a dictionary representation.

        Args:
            json (dict): representing the attributes of the student.
        """
        for key, value in json.items():
            setattr(self, key, value)
