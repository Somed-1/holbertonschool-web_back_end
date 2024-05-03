#!/usr/bin/env python3
"""Some doc"""
import asyncio
import time
wait_n = __import__("1-concurrent_coroutines").wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Some doc"""
    start = time.time()
    delays = await wait_n(n, max_delay)
    end = time.time()
    return (end - start) / n
