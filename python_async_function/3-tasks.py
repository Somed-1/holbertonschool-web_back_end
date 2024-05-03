#!/usr/bin/env python3
"""Some doc"""
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Some doc"""
    return wait_random(max_delay)
