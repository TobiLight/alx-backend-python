#!/usr/bin/env python3
# File: 3-tasks.py
# Author: Oluwatobiloba Light
""""
Task wait random module
"""


from asyncio import Task
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Creates and returns an asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
