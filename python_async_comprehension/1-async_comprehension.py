#!/usr/bin/env python3
"""Some doc"""
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Some doc"""
    return [i async for i in async_generator()]
