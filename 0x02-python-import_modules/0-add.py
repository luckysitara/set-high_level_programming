#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum of 1 and 2."""
#importing function from mudule
    from add_0 import add

    a = 1
    b = 2
#printing the result
    print("{} + {} = {}".format(a, b, add(a, b)))
