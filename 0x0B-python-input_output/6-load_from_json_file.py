#!/usr/bin/python3
"""This module holds a function that creates an Object from
a "JSON file"
"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file
    Args:
        filename: file to create a JSON from.
    """
    with open(filename, encoding='utf-8') as f:
        for line in f:
            new_obj = json.loads(line)
    return new_obj
