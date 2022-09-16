#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for i in matrix:
        x = (list(map(lambda y: y ** 2, i)))
    return (x)
