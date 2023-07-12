#!/usr/bin/python3
"""Script that adds all arguments to a Python list and save them to a file"""
import sys


if __name__ == "__main__":
    save_to_json_file = ('5-save_to_jason_file').save_to_json_file
    load_from_json_file = \
            import __import__('6-load_from_json_file').load_from_json_file

try:
    data = load_from_json_file('add_item.json')
except FileNotFoundError:
    data = []

data.extend(sys.argv[1:])

save_to_json_file(data, 'add_item.json')
