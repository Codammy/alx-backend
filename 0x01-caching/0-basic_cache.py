#!/usr/bin/env python3
"""basic caching"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """basic caching class"""

    def put(self, key, item):
        """assign to the dictionary self.cache_data
        the item value for the key key."""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key:
            return self.cache_data.get(key, None)
