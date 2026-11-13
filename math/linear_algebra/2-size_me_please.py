#!/usr/bin/env python3
def matrix_shape(matrix):
    shape = [len(matrix)]
    while type(matrix[0]) == list:
        matrix = matrix[0]
        shape.append(len(matrix))
    return shape
