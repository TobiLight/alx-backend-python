#!/usr/bin/env python3
# File: 100-safe_first_element.py
# Author: Oluwatobiloba Light
# Augments the following code with the correct duck-typed annotations
"""
Safe first element module
"""


from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Retrieves the first element of a sequence if it exists.
    """
    if lst:
        return lst[0]
    else:
        return None
