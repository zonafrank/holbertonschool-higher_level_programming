#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col, val in enumerate(row):
            print("{}{:d}".format(" " if col > 0 else "", val), end="")
        print()
