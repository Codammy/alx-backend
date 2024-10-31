#!/usr/bin/env python3
"""FIFOCache that inherits from BaseCaching and is a caching system
"""

import base_caching


class FIFOCache(base_caching.BaseCaching):
    """FIFOCache that inherits from BaseCaching"""

    def __init__(self):
        """class initializer"""
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                to_pop = list(self.cache_data.keys())
                print(f'DISCARD {to_pop[0]}')
                self.cache_data.popitem()

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key:
            return self.cache_data.get(key, None)
        