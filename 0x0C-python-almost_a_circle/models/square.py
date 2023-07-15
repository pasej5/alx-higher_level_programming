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

    @property
    def size(self):
        """Getter for size attribute.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for size attribute.

        Args:
            value (int): the size of the set.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Returns the string representation of a Square.
        """
        return f"[Square]({self.id}) {self.x}/{self.y} - {self.width}"
