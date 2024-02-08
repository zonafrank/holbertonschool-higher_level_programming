#!/usr/bin/python3
"""Module for function to generate pascal's triangle"""


def pascal_triangle(n):
    """Generate a Pascal's Triangle

    Args:
        n (int): number of layers

    Returns:
        Representation of the triangle using lists
    """
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                prev_row = triangle[-1]
                row.append(prev_row[j - 1] + prev_row[j])
        triangle.append(row)
    return triangle
