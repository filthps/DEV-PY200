from typing import Iterable, Any
from copy import deepcopy
from collections.abc import MutableSequence
from node import Node, DoubleLinkedNode


class LinkedList(MutableSequence):
    NODE = Node

    def __init__(self, items: Iterable = ()):
        self._head = None
        self._tail = None
        self._length = 0

        for i in items:
            self.append(i)

    @property
    def head(self):
        """
        Свойства понадобились для методов extend, __add__ и __iadd__!
        """
        return self._head

    @head.setter
    def head(self, element):
        self.is_valid_node(element)
        self._head = element

    @property
    def tail(self):
        """
        Свойства понадобились для методов extend, __add__ и __iadd__!
        """
        return self._tail

    @tail.setter
    def tail(self, element):
        self.is_valid_node(element)
        self._tail = element

    def is_valid_index(self, index) -> bool:
        if type(index) is not int:
            raise TypeError
        if 0 > index or index > self._length:
            raise IndexError
        return True

    def is_valid_node(self, node) -> bool:
        if not isinstance(node, (self.__class__.NODE, type(None))):
            raise TypeError
        return True

    def is_valid_nodes_collection(self, collection):
        if not isinstance(collection, self.__class__):
            raise ValueError

    def append(self, value) -> None:
        new_node = self.NODE(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.add_link(self.tail, new_node)
            self.tail = new_node
        self._length += 1

    def insert(self, index: int, value) -> None:
        self.is_valid_index(index)
        node = self.NODE(value)
        if index == 0:
            if self._length == 0:
                self.head = self.tail = node
            else:
                self.add_link(node, self.head)
                self.head = node
        elif index == self._length:
            self.add_link(self.tail, node)
            self.tail = node
        else:
            elem_prev = self.find_node(index - 1)
            elem_next = elem_prev.next
            self.add_link(elem_prev, node)
            self.add_link(node, elem_next)
        self._length += 1

    @staticmethod
    def add_link(left_node: Node, right_node: Node):
        left_node.next = right_node

    def find_node(self, index: int):
        return self.move_from_head(index)

    def find_value(self, value: Any) -> tuple[int, Any]:
        index_counter = 0
        for v in self:
            if type(v) is type(value) and v == value:
                return index_counter, v
            index_counter += 1

    def move_from_head(self, index):
        current_node = self.head
        for _ in range(index):
            next_node = current_node.next
            if next_node is not None:
                current_node = next_node
        return current_node

    def __getitem__(self, index):
        self.is_valid_index(index)
        node = self.find_node(index)
        if node is not None:
            return node.value

    def __setitem__(self, index, value):
        self.is_valid_index(index)
        node = self.find_node(index)
        if node is None:
            raise IndexError
        node.value = value

    def __delitem__(self, index):
        self.is_valid_index(index)
        if index == 0:
            node = self.head
            if node is None:
                raise IndexError
            next_node = node.next
            if next_node is None:
                self.head = self.tail = None
                self._length = 0
                return
            self.head = next_node
            next_node_1 = next_node.next
            if next_node_1 is None:
                self.tail = next_node
            self.add_link(next_node, next_node.next)
        elif index == self._length - 1:
            prev_node = self.find_node(index - 1)
            self.tail = prev_node
        else:
            prev_node = self.find_node(index - 1)
            current_node = prev_node.next
            next_node = current_node.next
            prev_node.next = next_node
        self._length -= 1

    def __len__(self):
        return self._length

    def __str__(self):
        return str(self.to_list())

    def to_list(self):
        return list(self)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.to_list()})"

    def iterator(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.value
            current_node = current_node.next

    def __iter__(self):
        return self.iterator()

    def __contains__(self, value):
        if self.find_value(value):
            return True
        return False

    def pop(self, index: int = -1):
        if index < 0:
            index = len(self) + index
        try:
            self.is_valid_index(index)
        except IndexError:
            return
        node = self.find_node(index)
        if node is not None:
            self.__delitem__(index)
            return node.value

    def remove(self, value):
        val = self.find_value(value)
        if not val:
            raise ValueError
        self.__delitem__(val[0])

    def index(self, value):
        elem = self.find_value(value)
        if elem:
            return elem[0]

    def extend(self, items_list: ["LinkedList"]):
        self.is_valid_nodes_collection(items_list)
        self.add_link(self.tail, items_list.head)
        self.tail = items_list.tail

    def __add__(self, other):
        self.is_valid_nodes_collection(other)
        clone = deepcopy(self)
        self.add_link(clone.tail, other.head)
        clone._tail = other.tail
        return clone

    def __iadd__(self, other):
        self = self.__add__(other)
        return self


class DoubleLinkedList(LinkedList):
    NODE = DoubleLinkedNode

    @staticmethod
    def add_link(left_node: Node, right_node: Node):
        left_node.next = right_node
        right_node.prev = left_node

    def find_node(self, index):
        if index > self._length // 2:
            return self.move_from_tail(index)
        return self.move_from_head(index)

    def move_from_tail(self, index):
        curr_elem = self.tail
        for _ in range(index):
            next_elem = curr_elem.prev
            if next_elem is not None:
                curr_elem = next_elem
            else:
                break
        return curr_elem


if __name__ == "__main__":
    pass
