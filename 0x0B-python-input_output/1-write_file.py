#!/usr/bin/python3
"""
A module that writes a string to  a text file and
returns the number of characters written
"""


def write_file(filename="", text=""):
    """a function which takes as filename and text to be written in the file"""
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
