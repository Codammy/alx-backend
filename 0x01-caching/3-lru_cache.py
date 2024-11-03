#!/usr/bin/env python3
"""LRUCache that inherits from BaseCaching and is a caching system
"""

import base_caching


class LRUCache(base_caching.BaseCaching):
    """Least Recently Used(LRU) Cache that inherits from BaseCaching"""

    def __init__(self):
        """class initializer"""
        super().__init__()
        self.__rank = {}
        self.access_times = 0

    def put(self, key, item):
        """assign to the dictionary self.cache_data"""
        if key and item:
            if not self.get(key) and len(self.cache_data) >= self.MAX_ITEMS:
                least_accessed = self.__least_accessed()[0]
                self.cache_data.pop(least_accessed)
                print(f'DISCARD: {least_accessed}')

            if len(self.cache_data) == 0:
                self.__rank[key] = 0
            else:
                self.__rank[key] = self.access_times

            self.cache_data[key] = item
            self.access_times += 1

    def __least_accessed(self):
        """returns the key with the least accessed times."""
        least_accessed = (None, self.access_times)
        for k, t in self.__rank.items():
            if t < least_accessed[1]:
                least_accessed = (k, t)
        self.__rank.pop(least_accessed[0])
        return least_accessed

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key:
            item = self.cache_data.get(key, None)
            if item:
                self.access_times += 1
                self.__rank[key] = self.access_times
            return item
