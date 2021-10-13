#!/usr/bin/python3
"""
A module that shows how to write object to a text file the json way
"""
import json


def save_to_json_file(my_obj, filename):
    """ a function that writes an Object to a text file"""
    with open(filename, mode="w", encoding='utf-8') as file:
        json.dump(my_obj, file)
