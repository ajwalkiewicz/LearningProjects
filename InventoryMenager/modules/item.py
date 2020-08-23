#!/usr/bin/python3
from dataclasses import dataclass


# @dataclass
# class Item:
#     """Example:
#     >>> item = Item("The Godfather", "book", "living_room", 1)
#     >>> item
#     Item(name='The Godfather', category='book', localization='living_room', quantity=1)
#     """
#     name: str
#     category: str
#     localization: str
#     quantity: int = 1

#     def __contains__(self, text: str):
#         """Example:
#         >>> "the" in Item("The Godfather", "book", "living_room", 1)
#         True
#         """
#         scope = self.name.split() + self.category.split() + self.localization.split()
#         scope = [t.lower() for t in scope]
#         return True if text.lower() in scope else False


class Item():
    """Example:
    >>> item = Item("The Godfather", "book", "living_room", 1)
    >>> print(item.name, item.category, item.place, item.quantity)
    The Godfather book living_room 1
    """

    id_ = 0

    def __init__(self, name: str, category: str, place: str, quantity: int = 1):
        Item.id_ += 1
        self.id_ = Item.id_
        self.name = name
        self.category = category
        self.place = place
        self.quantity = quantity

    def __contains__(self, text: str):
        """Example:
        >>> "the" in Item("The Godfather", "book", "living_room", 1)
        True
        """
        scope = self.name.split() + self.category.split() + self.place.split()
        scope = [t.lower() for t in scope]
        return True if text.lower() in scope else False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
