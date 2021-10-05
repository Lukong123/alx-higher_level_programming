#!/usr/bin/python3
""" a module contains add_integer function
    it takes two values a and b,b has been set to 98 by default.
"""


def add_integer(a, b=98):
    """
    add_integer function adds two numbers
    :param a: should be of type int or float
    :param b: should be of type int or float
    :return: should return a type int or float
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
