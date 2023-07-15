#!/usr/bin/python3
"""Module defining the Base class"""
import json


class Base:
    """Base class for managing id tribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes Base instnce with id

        Args:
            id (int): THis is set to None

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
        """returns the JSON string representation of list dictionaries

        Args:
            list_dictionaries (list): A list of dictionaries

        Returns:
            str: The JSON string representation of list dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objects):
        """
        Writes the JSON string represantation of list_objects to a file.

        Args:
            lis_objects (list): A list of the instances

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        obj_list = []
        if list_objects is not None:
            obj_list = [obj.to_dictionary() for obj in list_objects]
        with open(filename,"w") as file:
            file.write(cls.to_json_string(obj_list))
