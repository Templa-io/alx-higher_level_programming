#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    return list(map(lambda sub_list: list(map(lambda x: x*x, sub_list)), matrix))
