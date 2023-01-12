#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    keys_to_delete = [k for k, v in a_dictionary.items() if v == value]
    for k in keys_to_delete:
        del a_dictionary[k]
