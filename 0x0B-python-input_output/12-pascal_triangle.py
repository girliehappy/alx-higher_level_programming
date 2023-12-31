#!/usr/bin/python3
"""Defines a function Pascal's Triangle."""


def pascal_triangle(n):
    """
    Represent Pascal's Triangle.

    Returns a list of lists of integers representing the Pascal's triangle of n.
    """
    
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for h in range(len(tri) - 1):
            tmp.append(tri[h] + tri[h + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
