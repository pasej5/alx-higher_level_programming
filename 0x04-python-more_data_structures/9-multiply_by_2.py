#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_diction = a_dictionary.copy()
    list_keys = list(new_diction.keys())

    for key in list_keys:
        new_diction[key] *= 2

    return (new_diction)
