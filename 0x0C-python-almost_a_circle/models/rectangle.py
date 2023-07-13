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

    @property
    def width(self):
        """
        Getter for width attribute

        Returns:
        int: The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width attribute.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If value is an integer
            ValueError: If value is less than or equa to 0
        """

        if not is isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for height attribute

        Returns:
        int: The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height attribute.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If value is an integer
            ValueError: If value is less than or equa to 0
        """

        if not is isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def id(self):
        """
        Getter for id attribute

        Returns:
        int: The id of the rectangle
        """
        return self.__width

    @id.setter
    def id(self, value):
        """
        Setter for id attribute.

        Args:
            value (int): The id value to set.

        Raises:
            TypeError: If value is an integer
            ValueError: If value is less than or equa to 0
        """

        if not is isinstance(value, int):
            raise TypeError("id must be an integer")
        if value <= 0:
            raise ValueError("id must be > 0")
        self.__id = value

    @property
    def x(self):
        """
        Getter for x attribute

        Returns:
        int: The  x coodinate of the rectangle
        """
        return self.__x

    @width.setter
    def x(self, value):
        """
        Setter for x attribute.

        Args:
            value (int): The x value to set.

        Raises:
            TypeError: If value is an integer
            ValueError: If value is less than or equa to 0
        """

        if not is isinstance(value, int):
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter for y attribute

        Returns:
        int: The y of the rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for y attribute.

        Args:
            value (int): The y coodinate value to set.

        Raises:
            TypeError: If value is an integer
            ValueError: If value is less than or equa to 0
        """

        if not is isinstance(value, int):
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be > 0")
        self.__y = value
