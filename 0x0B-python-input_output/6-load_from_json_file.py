#!/usr/bin/python3
"""
A module creates an object from a json file
"""
import json


def load_from_json_file(filename):
    """ a function that creates an object from a json file"""
    with open(filename, mode="r", encoding='utf-8') as file:
        json.load(file)
