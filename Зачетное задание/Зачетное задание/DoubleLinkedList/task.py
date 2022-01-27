from typing import Iterable
from collections.abc import MutableSequence
from weakref import ref
from node import Node


class LinkedList(MutableSequence):
    def __init(self, items):
        self._value = self.append(items)


    def append(self, value) -> None:
        pass

    def insert(self, index: int, value) -> None:
        pass

    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

    def __len__(self):
        pass

    def __str__(self):
        return str(self.to_list())

    def to_list(self):
        return [item for item in self]

    def __repr__(self):
        return f"{self.__class__.__name__}({self.to_list()})"


class DoubleLinkedList(LinkedList):
    def __init__(self, items: Iterable = []):
        self.__value = self.append(items)
        self.__head = None
        self.__length = 0

    def is_valid(self, val):
        if not isinstance(val, int):
            raise TypeError
        if not 0 < self.__length < val:
            raise IndexError


    def append(self, items):
        last_node = self.__head or Node()
        if self.__head is None:
            self.
        for v in range(len(items)):
            self.set_next(v)

    @staticmethod
    def add_link(left_node: Node, right_node: Node):
        left_node.next = right_node

    def move_to_index(self, index):
        current_node = self.__head
        for _ in range(index):
            next_node = current_node.next
            if next_node is not None:
                current_node = next_node
                return current_node


if __name__ == "__main__":
    ...
