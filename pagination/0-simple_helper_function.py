#!/usr/bin/env python3
""" Something """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """ Something """
    return (page * page_size - page_size, page * page_size)
