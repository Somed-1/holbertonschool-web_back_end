#!/usr/bin/env python3
"""Some doc"""
import asyncio
import random
from typing import Union


async def wait_random(max_delay: int=10) -> float:
    """Some doc"""
    rand_time = random.uniform(0, max_delay)
    await asyncio.sleep(rand_time)
    return rand_time
