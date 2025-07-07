#!/usr/bin/env python3
"""
Module containing CountedIterator class that tracks iteration count
"""


class CountedIterator:
    """
    Iterator wrapper that counts how many items have been fetched
    """

    def __init__(self, iterable):
        """
        Initialize with an iterable and set counter to 0
        Args:
            iterable: Any iterable object
        """
        self.iterator = iter(iterable)
        self.counter = 0

    def __next__(self):
        """
        Get next item from iterator and increment counter
        Returns:
            Next item from iterator
        Raises:
            StopIteration: When no more items available
        """
        item = next(self.iterator)  # May raise StopIteration
        self.counter += 1
        return item

    def get_count(self):
        """
        Get current count of items fetched
        Returns:
            int: Number of items fetched so far
        """
        return self.counter

    def __iter__(self):
        """
        Make CountedIterator iterable by returning self
        Returns:
            The iterator object itself
        """
        return self
