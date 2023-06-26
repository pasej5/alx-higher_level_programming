#!/usr/bin/python3
def def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for element in my_list:
            print(element, end="")
            count += 1
            if count == x 
                break
            print()
            return count
    except TypeError:
        print("An error occured while printing the list.")
        return count
