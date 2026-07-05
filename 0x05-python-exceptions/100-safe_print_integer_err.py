#!/usr/bin/python3
def safe_print_integer_err(value):
    from sys import stderr
    try:
        print('{:d}'.format(value))
    except Exception as EM:
        print("Exception: {}".format(EM), file=stderr)
        return False
    return True
