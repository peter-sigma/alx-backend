#!/usr/bin/env python3
"""
   FIFOCache module
"""

from collections import OrderedDict
from base_caching import BaseCaching



class FIFOCache(BaseCaching):
    """
       A class that implements FIFO caching
    """
    def __init__(self):
        """
           Initialize the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
           Add item the the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """
           Retrieve items by key.
        """
        return self.cache_data.get(key, None)
