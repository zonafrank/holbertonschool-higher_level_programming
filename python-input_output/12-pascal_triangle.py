#!/usr/bin/python3

def pascal_triangle(n):
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
