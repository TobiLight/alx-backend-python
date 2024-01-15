#!/usr/bin/env python3
# File: 2-measure_runtime.py
# Author: Oluwatobiloba Light
"""
Total time execution measurement module
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures and returns the total execution time of wait_n.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_exec_time = (end - start) / n

    return total_exec_time
