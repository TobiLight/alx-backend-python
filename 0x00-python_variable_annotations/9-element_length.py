#!/usr/bin/env python3
# File: 9-element_length.py
# Author: Oluwatobiloba Light
# Annotate the below function’s parameters and return values with the
# appropriate types
"""
Element length module
"""


from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a tuple of unknown type and an integer.
    """
    return [(i, len(i)) for i in lst]
