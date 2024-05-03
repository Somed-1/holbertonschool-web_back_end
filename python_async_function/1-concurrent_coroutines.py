#!/usr/bin/env python3
"""Some doc"""
import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax.py").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = []
    for i in range(n):
        delays.append(await wait_random(max_delay))
    return delays
