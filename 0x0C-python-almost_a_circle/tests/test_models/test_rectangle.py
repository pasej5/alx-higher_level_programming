#!/usr/bin/python3
"""Tests for rectangle.py"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_area(self):
        """Test the area() method of Rectangle"""
        rectangle = Rectangle(2, 4)
        result = rectangle.area()
        expected = 8
        self.assertEqual(result, expected)

    def test_display(self):
        """Test the display() method of Rectangle"""
        # Test code for the display() method

    def test_update(self):
        """Test the update() method of Rectangle"""
        # Test code for the update() method

    # Add more test methods for other methods/attributes of Rectangle


if __name__ == '__main__':
    unittest.main()
