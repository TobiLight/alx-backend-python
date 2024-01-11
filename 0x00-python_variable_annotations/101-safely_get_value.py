#!/usr/bin/env python3
# File: 101-safely_get_value.py
# Author: Oluwatobiloba Light
# Adds type annotations to the function
"""
Task 101 Module
"""


from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None)\
        -> Union[Any, T]:
    """
	Retrieves a value from a dict using a given key
    """
    if key in dct:
        return dct[key]
    else:
        return default
