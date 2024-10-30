#!/usr/bin/env python3
"""implementing Server class for working with pagination"""
import csv
import math
import typing


class Server:
    """
        Server class to paginate a database f popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """object initializer"""
        self.__dataset = None

    @property
    def dataset(self) -> typing.List[typing.List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10)\
            -> typing.List[typing.List]:
        """returns a paginated list of baby names based
        on the page and page_size parameter"""
        assert type(page) is int, "expected integer greater than 0"
        assert type(page_size) is int, "expected integer greater than 0"
        assert page > 0, "expected integer greater than 0"
        assert page_size > 0, "expected integer greater than 0"

        start, end = self.index_range(page, page_size)

        return self.dataset[start:end]

    def index_range(self, page: int, page_size: int) -> typing.Tuple[int, int]:
        """
        returns a tuple of size two containing a
        start index and an end index corresponding to the range
        of indexes to return in a list for those particular
        pagination parameters.
        """

        last_index = (page - 1) * page_size
        return (last_index, last_index + page_size)

    def get_hyper(self, page: int = 1, page_size: int = 10)\
            -> typing.Mapping:

        total_pages = math.ceil(len(self.dataset) / page_size)
        data = self.get_page(page, page_size)
        paginated_data = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": (page + 1) if (page + 1) <= total_pages else None,
            "prev_page": (page - 1) if (page - 1) > 0 else None,
            "total_pages": total_pages
        }

        return paginated_data