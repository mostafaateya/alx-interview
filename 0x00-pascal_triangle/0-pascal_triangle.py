#!/usr/bin/python3
""" Module for calculating Pascal Triangle """


def pascal_triangle(n):
    """ Function for creating a pascal triangle as a list of lists
    n: number of rows
    returns empty list if n <= 0
    """
    if n <= 0:
        return ([])

    pascal_output = [[1]]
    for i in range(1, n):
        row = [1]
        prev = pascal_output[i - 1]
        for j in range(len(prev)):
            new = prev[j] + prev[j + 1] if j != len(prev) - 1 else 1
            row.append(new)

        pascal_output.append(row)

    return pascal_output
