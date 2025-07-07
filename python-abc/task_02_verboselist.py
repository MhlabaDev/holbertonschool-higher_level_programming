#!/usr/bin/env python3
"""
Module containing VerboseList class that extends list with notifications
"""


class VerboseList(list):
    """
    A list subclass that prints notifications for modifications
    """

    def append(self, item):
        """
        Add an item to the end of the list with notification
        Args:
            item: The item to append
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list with items from iterable with notification
        Args:
            iterable: Items to add to the list
        """
        length_before = len(self)
        super().extend(iterable)
        added_items = len(self) - length_before
        print(f"Extended the list with [{added_items}] items.")

    def remove(self, item):
        """
        Remove first occurrence of item with notification
        Args:
            item: The item to remove
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Remove and return item at index with notification
        Args:
            index: Position of item to remove (default last)
        Returns:
            The popped item
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
