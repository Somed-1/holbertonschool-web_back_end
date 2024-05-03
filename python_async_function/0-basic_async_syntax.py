#!/usr/bin/env python3
"""Some doc"""
import asyncio
import random
from typing import Union


async def wait_random(max_delay: Union[int, float]=10) -> Union[int, float]:
    rand_time = random.randrange(0, max_delay)
    await asyncio.sleep(rand_time)
    return rand_time
