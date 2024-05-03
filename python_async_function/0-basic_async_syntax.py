#!/usr/bin/env python3
"""Some doc"""
import asyncio
import random


async def wait_random(max_delay=10):
    rand_time = random.randrange(0, max_delay)
    await asyncio.sleep(rand_time)
    return rand_time
