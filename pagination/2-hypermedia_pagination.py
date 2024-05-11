#!/usr/bin/env python3
""" Something """
import csv
import math
from typing import Dict, Tuple
from typing import List


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get_page method """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        p, pz = index_range(page, page_size)
        try:
            return self.dataset()[p:pz]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ get_hyper method """
        dataset_len = len(self.dataset())
        pages_count = math.ceil(dataset_len / page_size)
        data = {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1 if page < pages_count else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": pages_count
        }
        return data


def index_range(page: int, page_size: int) -> Tuple:
    """ Something """
    return (page * page_size - page_size, page * page_size)
