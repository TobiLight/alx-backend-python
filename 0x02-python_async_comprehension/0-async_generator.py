#!/usr/bin/env python3
# File: 0-async_generator.py
# Author: Oluwatobiloba Light
"""Task 0 module"""

import asyncio
from random import uniform
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    An asynchronous generator coroutine that yields random numbers.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
