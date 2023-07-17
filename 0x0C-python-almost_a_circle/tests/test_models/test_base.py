#!/usr/bin/python3
"""Tests for base.py"""


import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_to_json_string(self):
        """Test when dictionary is empty or has elements"""

        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

        list_dictionaries = [{'id': 1, 'name': 'Matsika'}, {'id': 2, 'name': 'Jealous'}]
        result = Base.to_json_string(list_dictionaries)
        self.assertEqual(result, '[{"id": 1, "name": "Matsika"}, {"id": 2, "name": "Jealous"}]')

    def test_from_json_string(self):
        """Test when JSON string is empty or has elements"""
        result = Base.from_json_string('')
        self.assertEqual(result, [])

        json_string = '[{"id": 1, "name": "Nopah"}, {"id": 2, "name": "Matsika"}]'
        result = Base.from_json_string(json_string)
        expected = [{'id': 1, 'name': 'Nopah'}, {'id': 2, 'name': 'Matsika'}]
        self.assertEqual(result, expected)

    def test_save_to_file(self)


if __name__ == '__main__':
    unittest.main
