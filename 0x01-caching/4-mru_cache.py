#!/usr/bin/env python3
"""MRUCache that inherits from BaseCaching and is a caching system
"""

import base_caching


class MRUCache(base_caching.BaseCaching):
    """Most Recently Used(MRU) Cache that inherits from BaseCaching"""

    def __init__(self):
        """class initializer"""
        super().__init__()
        self.most_accessed_key = None

    def put(self, key, item):
        """assign to the dictionary self.cache_data"""
        if key and item:
            if not self.get(key) and len(self.cache_data) >= self.MAX_ITEMS:
                most_accessed = self.most_accessed_key
                self.cache_data.pop(most_accessed)
                print(f'DISCARD: {most_accessed}')

            self.cache_data[key] = item
            self.most_accessed_key = key

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key:
            item = self.cache_data.get(key, None)
            if item:
                self.most_accessed_key = key
            return item
