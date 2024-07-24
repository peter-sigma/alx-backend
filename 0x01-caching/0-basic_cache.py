#!/usr/bin/env python3
"""
   Basic caching file.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
       A class represention of an object that allows storing and
       retrieving items from a dictionary.
    """
    def put(self, key, item):
        """
           Add item to the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
           Retrieve item by key.
        """
        return self.cache_data.get(key, None)
