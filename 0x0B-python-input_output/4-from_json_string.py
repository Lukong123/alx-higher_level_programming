#!/usr/bin/python3
"""
A module that returns an object (Python data structure) represented by a JSON string
"""
import json


def from_json_string(my_str):
    """ A function that returns an object represented by json string"""
    return json.loads(my_str)
