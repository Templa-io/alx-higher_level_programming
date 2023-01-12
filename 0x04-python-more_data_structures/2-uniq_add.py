#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_list = list(set(my_list))
    total = 0
    for i in unique_list:
        if isinstance(i, int):
            total += i
    return total
