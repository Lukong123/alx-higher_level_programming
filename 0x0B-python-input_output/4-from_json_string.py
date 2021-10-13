#!/usr/bin/python3
"""
A module that returns an object (Python data structure) represented by a JSON string
"""
import json


def from_json_string(my_str):
    """ returns an obj for JSON string repr
    """
    return json.loads(my_str)
