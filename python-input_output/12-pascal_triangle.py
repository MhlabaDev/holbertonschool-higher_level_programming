#!/usr/bin/python3
"""create and return a list of lists of int represent Pascal triangle of n"""


def pascal_triangle(n):
    """create a pascal_triangle in list"""

    if n <= 0:
        return []
    left_side = [1]
    right_side = [1]
    new_item = []
    pascal_list = [[1]]
    for i in range(1, n):
        left_side.insert(0, 0)
        right_side.append(0)
        new_item = [ll + rr for ll, rr in zip(left_side, right_side)]
        pascal_list.append(new_item)
        left_side = new_item.copy()
        right_side = new_item.copy()
    return pascal_list
