#!/usr/bin/python3
"""Tests for square.py"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_area(self):
        """Test the area() method of Square"""
        # Create a Square instance
        square = Square(5)
        # Calculate the expected area
        expected_area = 5 * 5
        # Compare the expected area with the actual area
        self.assertEqual(square.area(), expected_area)

    def test_display(self):
        """Test the display() method of Square"""
        # Create a Square instance
        square = Square(3)
        # Capture the output of the display() method
        expected_output = "###\n" \
                          "###\n" \
                          "###\n"
        # Create a stream to capture the print output
        captured_output = io.StringIO()
        # Redirect stdout to the stream
        sys.stdout = captured_output
        # Call the display() method
        square.display()
        # Reset stdout
        sys.stdout = sys.__stdout__
        # Get the printed output
        actual_output = captured_output.getvalue()
        # Compare the expected output with the actual output
        self.assertEqual(actual_output, expected_output)

    def test_update(self):
        """Test the update() method of Square"""
        # Create a Square instance
        square = Square(4)
        # Update the Square attributes
        square.update(1, 5, 2, 1)
        # Check if the attributes are updated correctly
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 1)

    # Add more test methods for other methods/attributes of Square


if __name__ == '__main__':
    unittest.main()

