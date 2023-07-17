#!/usr/bin/python3
"""Tests for base.py"""


import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_to_json_string(self):
        """Test when list_dictionaries is empty or has elements"""

        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

        list_dictionaries = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
        result = Base.to_json_string(list_dictionaries)
        self.assertEqual(result, '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]')

    def test_from_json_string(self):
        """Test when json_string is empty or has elements"""
        result = Base.from_json_string('')
        self.assertEqual(result, [])

        json_string = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        result = Base.from_json_string(json_string)
        expected = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
        self.assertEqual(result, expected)

    def test_save_to_file(self):
        """Test saving an empty list of objects"""
        Base.save_to_file([])

    def test_create(self):
        # Test creating an instance of the Rectangle class
        rectangle_dict = {'id': 1, 'width': 10, 'height': 20}
        rectangle = Base.create(**rectangle_dict)
        # Check if the attributes of the rectangle match the dictionary values

        # Test creating an instance of the Square class
        square_dict = {'id': 2, 'size': 5}
        square = Base.create(**square_dict)
        # Check if the attributes of the square match the dictionary values

    def test_load_from_file(self):
        # Test loading from a file that doesn't exist
        result = Base.load_from_file()
        self.assertEqual(result, [])

        # Test loading from a file that exists
        # Create a file with some objects in JSON format

        # Load the objects from the file

        # Check if the loaded objects match the expected values

if __name__ == '__main__':
    unittest.main()

