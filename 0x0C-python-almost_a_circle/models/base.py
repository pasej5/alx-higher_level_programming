#!/usr/bin/python3
"""Module defining the Base class"""
import json


class Base:
    """Base class for managing id attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes Base instance with id

        Args:
            id (int): This is set to None

        Return:
            Nothing
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list dictionaries

        Args:
            list_dictionaries (list): A list of dictionaries

        Returns:
            str: The JSON string representation of list dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list represented by the JSON string json_string

        Args:
            json_string (str): A string representing a list of dictionaries

        Returns:
            list: The list represented by the JSON string
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objects):
        """Writes the JSON string representation of list_objects to a file

        Args:
            list_objects (list): A list of the instances

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        obj_list = []
        if list_objects is not None:
            obj_list = [obj.to_dictionary() for obj in list_objects]
        with open(filename, "w") as file:
            file.write(cls.to_json_string(obj_list))

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.

        Args:
            **dictionary: Double pointer to a dictionary.

        Returns:
            Instance: An instance with all attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy
    
    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a JSON file.

        Returns:
            list: List of instances.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                obj_list = cls.from_json_string(json_string)
                instances = [cls.create(**obj) for obj in obj_list]
                return instances
        except FileNotFoundError:
            return []
