#!/usr/bin/python3
"""Define a function that converts a Roman numeral to an integer."""


def roman_to_int(roman_string):
    """Convert a Roman numeral string to an integer.

    Args:
        roman_string (str): The Roman numeral to convert.

    Returns:
        int: The integer value of the Roman numeral, or 0 if
            roman_string is not a string.
    """
    if type(roman_string) is not str or len(roman_string) == 0:
        return 0

    roman_dictionary = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    result = 0

    for i in range(len(roman_string)):
        value = roman_dictionary[roman_string[i]]
        if i < len(roman_string) - 1 and \
                value < roman_dictionary[roman_string[i + 1]]:
            result -= value
        else:
            result += value

    return result
