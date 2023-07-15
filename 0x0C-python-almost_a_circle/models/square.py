#!/usr/bin/python3
"""Class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialization of the Square.

        Args:
            size (int): The size of the Square
            x (int): The x coordinate of the square
            y (int): The y coordinate of the square
            id (int): The id of the Square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the string representation of a Square.
        """
        return f"[Square]({self.id}) {self.x}/{self.y} - {self.width}"
