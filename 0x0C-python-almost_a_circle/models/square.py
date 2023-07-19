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
        return f"[Square]({self.id}){self.x}/{self.y} - {self.width}"

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
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        if value <= 0:
            raise ValueError("Size must be greater than 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the attribute of the Square instance.

        Args:
            *args: Variable length argument list
            **kwargs: key word arguments
        """
        if args and len(args) > 0:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                if i < len(attrs):
                    setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary represantation of the square

        Returns:
            dict: The dictionary represantation of the square
        """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
