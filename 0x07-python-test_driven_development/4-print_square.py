#!/usr/bin/python3
"""
a function that prints a square with the character #
"""


def print_square(size):
    """
    print_square a function
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for ligne in range(0, size):
        for column in range(0, size):
            print("#", end="")
        print()
