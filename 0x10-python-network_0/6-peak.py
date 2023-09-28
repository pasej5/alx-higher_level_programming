#!/usr/bin/python3
"""Peak of unsorted numbers"""


def find_peak(list_of_integers):
    """Finding the peak of unsorted intergers"""
    prev = 0
    for idx, num in enumerate(list_of_integers):
        if idx:
            prev = list_of_integers[idx - 1]
        if idx < len(list_of_integers) - 1:
            next = list_of_integers[idx + 1]
        else:
            next = 0
        if num >= prev and num >= next:
            return num
