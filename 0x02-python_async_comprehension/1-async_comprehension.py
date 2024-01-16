#!/usr/bin/env python3
# File: 1-async_comprehension.py
# Author: Oluwatobiloba Light
"""Task 1 module"""


from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Creates a list of 10 numbers from a 10-number generator.
    """
    ret = [number async for number in async_generator()]
    return ret
