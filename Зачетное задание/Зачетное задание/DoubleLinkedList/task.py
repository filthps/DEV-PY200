from typing import Iterable
from collections.abc import MutableSequence
from node import Node, DoubleLinkedNode


class LinkedList(MutableSequence):
    NODE_TYPE = Node
    
    def __init__(self, items):
        self._head = None
        self._tail = None
        self._length = 0

        for i in items:
            self.append(i)

    def append(self, value) -> None:
        new_node = self.NODE_TYPE(value)
        if self._head is None:
            self._head = new_node  # fixme tail??? over test case
        else:
            last_node = self.move_from_head(self._length)
            self.add_link(last_node, new_node)
        self._length += 1

    def insert(self, index: int, value) -> None:
        node = self.NODE_TYPE(value)
        if index == 0:
            next_elem = self._head  # fixme лишнее
            self.add_link(node, next_elem)  # self.add_link(node, self._head)
            self._head = node
        elif index == self._length - 1:  # fixme test case insert(does_not_exist_index) index > len
            last_elem = self.move_from_head(self._length - 1)
            self.add_link(last_elem, node)
        else:
            elem = self.move_from_head(index - 1)
            self.add_link(elem, node) # fixme test case in middle
        self._length += 1

    @staticmethod
    def add_link(left_node: Node, right_node: Node):
        left_node.next = right_node

    @classmethod
    def is_valid(cls, node):  # todo зачем???
        """Зачем"""
        if not isinstance(node, cls):
            raise TypeError

    def move_from_head(self, index):  # todo negative index, index error???
        current_node = self._head
        for _ in range(index):
            next_node = current_node.next
            if next_node is not None:
                current_node = next_node
                return current_node

    def __getitem__(self, i):
        # fixme TypeError IndexError
        return self.move_from_head(i)

    def __setitem__(self, i, value):
        # fixme TypeError IndexError
        self.insert(i, value)

    def __delitem__(self, i):
        pass

    def __len__(self):
        return self._length

    def __str__(self):
        return str(self.to_list())

    def to_list(self):
        return [item for item in self]  # todo через магический метод

    def __repr__(self):
        return f"{self.__class__.__name__}({self.to_list()})"

    def iterator(self):
        current_node = self._head
        while True:
            yield current_node
            current_node = current_node.next  # test case ???

    def __iter__(self):
        return self.iterator()

    def __contains__(self, item):
        for node in self.to_list(): # in self
            if node == item:
                return True
        return False


class DoubleLinkedList(LinkedList):
    NODE_TYPE = DoubleLinkedNode


    @staticmethod
    def add_link(left_node: Node, right_node: Node):
        left_node.next = right_node
        right_node.prev = left_node


if __name__ == "__main__":
    node_collection = DoubleLinkedNode([1, 2, 3, 4])
    node_collection.append([5, 6, 7])
    print(repr(node_collection))
