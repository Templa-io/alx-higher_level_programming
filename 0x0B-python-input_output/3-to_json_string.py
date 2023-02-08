#!/usr/bin/python3
"""This module holds a function that returns the JSON
representation of an object.
"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object(string)
    Args:
        my_obj: object to return as JSON representation.
    """
    
    return (json.dumps(my_obj))
