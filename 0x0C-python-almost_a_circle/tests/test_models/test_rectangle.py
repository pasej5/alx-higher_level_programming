#!/usr/bin/python3
"""Tests for rectangle.py"""
import unittest
from models.rectangle import Rectangle
import io
import contextlib


class TestRectangle(unittest.TestCase):
    def test_area(self):
        """Test the area() method of Rectangle"""
        rectangle = Rectangle(2, 4)
        result = rectangle.area()
        expected = 8
        self.assertEqual(result, expected)

    def test_display(self):
        """Test the display() method of Rectangle"""
        rectangle = Rectangle(3, 4)
        with io.StringIO() as captured_output:
            with contextlib.redirect_stdout(captured_output):
                rectangle.display()

            output = captured_output.getvalue()

        expected = "###\n###\n###\n###\n"
        self.assertEqual(output, expected)

    def test_update(self):
        """Test the update() method of Rectangle"""
        rectangle = Rectangle(2, 4)
        rectangle.update(5, 6, 7, 8, 9)
        self.assertEqual(rectangle.id, 5)
        self.assertEqual(rectangle.width, 6)
        self.assertEqual(rectangle.height, 7)
        self.assertEqual(rectangle.x, 8)
        self.assertEqual(rectangle.y, 9)

    def test_invalid_width(self):
        """Test raising an exception for invalid width"""
        with self.assertRaises(ValueError):
            Rectangle(-2, 4)

    def test_invalid_height(self):
        """Test raising an exception for invalid height"""
        with self.assertRaises(ValueError):
            Rectangle(2, -4)

    def test_invalid_x(self):
        """Test raising an exception for invalid x-coordinate"""
        with self.assertRaises(ValueError):
            Rectangle(2, 4, -1, 0)

    def test_invalid_y(self):
        """Test raising an exception for invalid y-coordinate"""
        with self.assertRaises(ValueError):
            Rectangle(2, 4, 0, -1)


if __name__ == '__main__':
    unittest.main()
