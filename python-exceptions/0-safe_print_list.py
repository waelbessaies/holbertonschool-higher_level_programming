#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for count in range(x):
            print(my_list[count], end="")
            count += 1
    except IndexError:
        None
    print()
    return count
