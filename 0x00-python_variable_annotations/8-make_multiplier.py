#!/usr/bin/env python3
# File: 8-make_multiplier.py
# Author: Oluwatobiloba Light
# A type-annotated function make_multiplier that takes a float
# multiplier as argument and returns a function that multiplies a float
# by multiplier.
"""
Multiplier module
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float.
    """
    def wrapper(multiplier: float) -> float:
        return multiplier * multiplier

    return wrapper
