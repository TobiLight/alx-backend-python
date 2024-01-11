#!/usr/bin/env python3
# File: 7-to_kv.py
# Author: Oluwatobiloba Light
# A type-annotated function to_kv that takes a string k and an int OR
# float v as arguments and returns a tuple.
"""
Task 7 module
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple
    """
    return k, v ** 2
