#!/usr/bin/python3
"""
A module that appends a string to  a text file and
returns the number of characters written
"""


def append_write(filename="", text=""):
    """appending text to file"""
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
