#!/usr/bin/python3
"""Defining class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes Rectangle with width, height, x, y and id.

        
        Args:
        width (int): The width of the Rectangle.
        height (int): The height of the Rectangle.
        x (int): The x coodinator of the rectangle's position default 0
        y (int): The y coodinator of the rectangle's position default 0
        id (int): The id of the rectangle default = 0
    """

    super().__init__(id)
    self.width = width
    self.height = height
    self.x = x
    self.y = y
