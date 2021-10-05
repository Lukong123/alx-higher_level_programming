#!/usr/bin/python3
""" a module contains say_my_name function
    it takes two values first_name and last_name.
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name function adds two numbers
    :param first_name: should be of type string
    :param last_name: should be of type string
    :return: should return a type string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/3-say_my_name.txt")
