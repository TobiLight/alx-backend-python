#!/usr/bin/env python3
# File: 0-basic_async_syntax.py
# Author: Oluwatobiloba Light
"""Asynchronous coroutine module"""


import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay and returns it
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
