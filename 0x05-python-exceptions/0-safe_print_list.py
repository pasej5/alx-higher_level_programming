#!/usr/bin/python3
def safe_print_list(my_list=[], x = 0):
    """function that prints x elements of a list"""
   count = 0
   for variable in range(x):
       try :
            print(my_list[variable], end=' ')
            count += 1
        except IndexError:
            break
    finally:
        print()
        return (count)