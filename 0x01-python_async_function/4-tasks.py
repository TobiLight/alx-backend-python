#!/usr/bin/env python3
# File: 4-tasks.py
# Author: Oluwatobiloba Light
"""
Task 4 module
"""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes task_wait_random n times.
    """
    task_wait_random_list = [task_wait_random(max_delay) for _ in range(n)]
    ret = await asyncio.gather(*task_wait_random_list)

    return sorted(ret)
