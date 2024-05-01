#!/usr/bin/env python3
"""Some doc"""


from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Some doc"""
    return [(i, len(i)) for i in lst]
