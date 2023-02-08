#!/usr/bin/python3
"""This module holds a function that returns an object represented
by a JSON string.
"""
import json


def from_json_string(my_str):
    """returns an object (Python data structure)
    represented by a JSON string.
    Args:
        my_str: the object.
    """

    return (json.loads(my_str))
