#!/usr/bin/env python3
# File: 2-measure_runtime.py
# Author: Oluwatobiloba Light
"""Task 2 module"""


import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension 4 times and measures the total execution time.
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()
    total_exec_time = end - start

    return total_exec_time
