#!/usr/bin/python3
"""MyList that inherits from list"""


class MyList(list):
    """Class Mylist that inherits from list"""

    def print_sorted(self):
        """method that prints list, ascending order"""

        sorted_list = sorted(self)
        print(sorted_list)
