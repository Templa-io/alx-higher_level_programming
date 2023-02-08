#!/usr/bin/python3
"""This module holds a function that writes a string to
a text file.
"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the
    number of characters written.
    Args:
        filename: the file to write.
        text: the string to be written
    """

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
        return len(text)

