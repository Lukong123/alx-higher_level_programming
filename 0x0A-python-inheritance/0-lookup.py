#!/usr/bin/python3
"""
a function that returns a list of available attributes and methods of objects
"""


def lookup(obj):
    """ returns list of available attributes and methods"""
    return dir(obj)
