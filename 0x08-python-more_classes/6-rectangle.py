#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
            number_of_instances: the count incement count/decrement
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Return a string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = []
        for i in range(self.__height):
            rectangle_str.append("#" * self.__width)
        return "\n".join(rectangle_str)

    def __repr__(self):
        """Return a string representation of the rectangle for eval()"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Destructor method"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
