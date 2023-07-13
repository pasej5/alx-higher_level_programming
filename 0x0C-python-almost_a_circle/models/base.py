#!/usr/bin/python3
"""Module defining the Base class"""


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
