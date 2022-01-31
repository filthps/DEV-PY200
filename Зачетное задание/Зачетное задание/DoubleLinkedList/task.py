from collections.abc import MutableSequence
from node import Node, DoubleLinkedNode


class LinkedList(MutableSequence):
    NODE = Node
    
    def __init__(self, items):
        self._head = None
        self._tail = None
        self._length = 0

        for i in items:
            self.append(i)

    def append(self, value) -> None:  # todo: написать тест
        new_node = self.NODE(value)
        if self._head is None:
            self._head = self._tail = new_node
        else:
            self.add_link(self._tail, new_node)
            self._tail = new_node
        self._length += 1

    def insert(self, index: int, value) -> None:  # todo: написать тест
        self.is_valid_index(index)
        node = self.NODE(value)
        if index == 0:
            self.add_link(node, self._head)
            self._head = node
        elif index == self._length:  # fixme test case insert(does_not_exist_index) index > len
            self.add_link(self._tail, node)
            self._tail = node
        else:
            elem = self.find_node(index)
            self.add_link(elem, node)  # fixme test case in middle
        self._length += 1

    @staticmethod
    def add_link(left_node: Node, right_node: Node):
        left_node.next = right_node

    def is_valid_index(self, index):
        if type(index) is not int:
            raise TypeError
        if 0 > index < self._length:
            raise IndexError
        
    def is_valid_node(self, node):
        if not isinstance(node, self.__class__.NODE):
            raise TypeError

    def find_node(self, index):
        return self.move_from_head(index)

    def move_from_head(self, index):  # todo negative index, index error???
        current_node = self._head
        for _ in range(index):
            next_node = current_node.next
            if next_node is not None:
                current_node = next_node
                return current_node
            else:
                return None

    def __getitem__(self, i):
        self.is_valid_index(i)
        return self.find_node(i)

    def __setitem__(self, i, value):
        self.insert(i, value)

    def __delitem__(self, i):
        self.is_valid_index()
        if i == 0:
            node = self._head
            if node is None:
                raise IndexError
            next_node = node.next
            if next_node is None:
                self._head = self._tail = None
                return
            self._head = next_node
            next_node_1 = next_node.next
            if next_node_1 is None:
                self._tail = next_node
            self.add_link(next_node, next_node.next)
        elif i == self._length - 1:
            try:
                prev_node_1 = self.find_node(i - 2)
            except IndexError:
                prev_node_1 = None
            prev_node = self.find_node(i - 1)
            self._tail = prev_node
            if prev_node_1 is not None:
                prev_node_1.next = prev_node
        else:
            prev_node = self.find_node(i - 1)
            current_node = prev_node.next
            next_node = current_node.next
            prev_node.next = next_node

    def __len__(self):
        return self._length

    def __str__(self):
        return str(self.to_list())

    def to_list(self):
        return list(self.__iter__())

    def __repr__(self):
        return f"{self.__class__.__name__}({self.to_list()})"

    def iterator(self):  # todo: написать тест
        current_node = self._head
        while current_node is not None:
            yield current_node
            current_node = current_node.next  # test case ???

    def __iter__(self):
        return self.iterator()

    def __contains__(self, item):
        try:
            self.is_valid_node(item)
        except TypeError:
            return False
        for node in self:
            if node is item:
                return True
        return False

    def pop(self, index: int = ...):  # ...??
        self.is_valid_index(index)
        elem = self.find_node(index)
        self.__delitem__(index)
        return elem

    def remove(self, node=None) -> None:
        try:
            self.is_valid_node(node)
        except TypeError:
            raise ValueError
        node_from_container = None
        counter = 0
        for item in self:
            if item is node:
                node_from_container = node
                break
            counter += 1
        if node_from_container is not None:
            self.__delitem__(counter)

    def index(self, node):
        self.is_valid_node(node)
        counter = 0
        for item in self:
            if item is node:
                break
            counter += 1
        else:
            counter = None
        return counter

    def extend(self, items):
        if items.__class__ is self.__class__:
            for item in items:
                self.append(item)
        else:
            raise ValueError


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
        curr_elem = self._tail
        if index == self._length - 1:
            return curr_elem
        for _ in range(index):
            curr_elem = curr_elem.prev
            if curr_elem is not None:
                return curr_elem
            else:
                return None


if __name__ == "__main__":
    pass
