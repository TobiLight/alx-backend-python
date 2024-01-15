#!/usr/bin/env python3
# File: 1-concurrent_coroutines.py
# Author: Oluwatobiloba Light
"""
Multiple coroutines module
"""


import asyncio
from random import uniform
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes wait_random n times
    """
    delay = uniform(0, max_delay)
    wait_random_list = [wait_random(delay) for _ in range(n)]
    ret = await asyncio.gather(*wait_random_list)

    return sorted(ret)
