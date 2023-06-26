#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """function that prints x elements of a list."""
    real_number_of_elements = 0
    for variable in range(x):
        try:
            print("{}".format(my_list[variable]), end="")
            real_number_of_elements += 1
        except IndexError:
            break
    print("")
    return (real_number_of_elements)
