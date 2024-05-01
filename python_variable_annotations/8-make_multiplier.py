#!/usr/bin/env python3
"""Some doc"""



from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Some doc"""
    def f(n: float) -> float:
        """Some doc"""
        return n * multiplier

    return f
