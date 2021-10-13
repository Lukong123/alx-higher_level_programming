#!/usr/bin/python3
"""
a function that reads file and prints data to stdout
"""


def read_file(filename=""):
    """ a function to read file as UT8 text file"""
    with open(filename, 'r') as f:
        read_data = f.read()
        print(read_data, end="")
