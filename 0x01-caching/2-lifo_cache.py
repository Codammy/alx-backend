#!/usr/bin/env python3
"""LIFOCache that inherits from BaseCaching and is a caching system
"""

import base_caching


class LIFOCache(base_caching.BaseCaching):
    """FIFOCache that inherits from BaseCaching"""

    def __init__(self):
        """class initializer"""
        super().__init__()
        self.last_mod = None

    def put(self, key, item):
        """assign to the dictionary self.cache_data"""
        if key and item:
            if not self.get(key) and len(self.cache_data) >= self.MAX_ITEMS:
                self.cache_data.pop(self.last_mod)
                print(f'DISCARD {self.last_mod}')
            self.cache_data[key] = item
            self.last_mod = key

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key:
            return self.cache_data.get(key, None)
