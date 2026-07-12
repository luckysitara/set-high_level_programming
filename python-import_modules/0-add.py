#!/usr/bin/python3
"""Print the sum of 1 and 2."""


if __name__ == "__main__":
    # Importing function from module
    from add_0 import add

    a = 1
    b = 2

    # Printing the result
    print("{} + {} = {}".format(a, b, add(a, b)))
