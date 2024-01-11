#!/usr/bin/env python3
# File: 100-safe_first_element.py
# Author: Oluwatobiloba Light
# Augments the following code with the correct duck-typed annotations


from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
