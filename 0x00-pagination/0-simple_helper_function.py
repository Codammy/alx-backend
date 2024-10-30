#!/usr/bin/env python3
"""
function named index_range that takes two integer arguments page and page_size
"""
import typing


def index_range(page: int, page_size:int)-> typing.Tuple[int, int]:
    """
    returns a tuple of size two containing a
    start index and an end index corresponding to the range
    of indexes to return in a list for those particular
    pagination parameters.
    """

    last_index = (page - 1) * page_size
    return (last_index, last_index + page_size)