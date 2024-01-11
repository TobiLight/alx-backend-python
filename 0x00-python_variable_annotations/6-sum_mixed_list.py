#!/usr/bin/env python3
# File: 6-sum_mixed_list.py
# Author: Oluwatobiloba Light
# A type-annotated function sum_mixed_list which takes a list mxd_lst of
# integers and floats and returns their sum as a float.
"""
Sum of list module
"""


from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns their sum as a float.
    """
    return sum(mxd_lst)
