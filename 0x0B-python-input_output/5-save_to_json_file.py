#!/usr/bin/python3
"""This module holds a function that writes an Object to a text file,
using a JSON representation.
"""

import json

def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation.
    Args:
        my_obj: the object.
        filename: file to save my_obj to
    """

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
