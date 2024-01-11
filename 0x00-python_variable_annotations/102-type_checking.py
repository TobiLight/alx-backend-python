#!/usr/bin/env python3
# File: 102-type_checking.py
# Author: Oluwatobiloba Light
# Validates the following piece of code and apply any necessary changes.
"""
Zoom Array module
"""


from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Returns a list.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x: List = zoom_array(array, 3)
