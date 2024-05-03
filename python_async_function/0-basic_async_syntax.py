#!/usr/bin/env python3
"""Some doc"""
import asyncio
import random


async def wait_random(max_delay=10):
    await asyncio.sleep(random.randrange(0, max_delay))
