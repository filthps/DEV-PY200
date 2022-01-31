from typing import Optional
from weakref import ref


class Node:
    def __init__(self, val: int = 1, next_: Optional["Node"] = None):
        self.value = val
        self._next = None
        self.next = next_

    @classmethod
    def is_valid(cls, val):
        if not isinstance(val, (cls, type(None),)):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, val):
        self.is_valid(val)
        self._next = val

    def __repr__(self):
        name = self.__class__.__name__
        if self.next:
            return f"{name}({self.value}, next_={name}({self.next}))"
        return f"{name}({self.value})"

    def __str__(self):
        return str(self.value)

    def __del__(self):
        print(f"{ self.__class__.__name__}({self.value}) - delete")


class DoubleLinkedNode(Node):

    def __init__(self, val, _next_: Optional["DoubleLinkedNode"] = None, prev: Optional["DoubleLinkedNode"] = None):
        super().__init__(val, next_=_next_)
        self._prev = None
        self.prev = prev

    @property
    def prev(self):
        if self._prev is None:
            return None
        return self._prev()

    @prev.setter
    def prev(self, value):
        self.is_valid(value)
        self._prev = ref(value) if value is not None else None

    def __repr__(self):
        name = type(self).__name__
        next_ = f", _next_={name}({self.next})" if self.next else None
        prev = f"prev={name}({self.prev}) ," if self.prev else None
        return f"{name}({prev if prev else ''}{self.value}{next_ if next_ else ''})"


if __name__ == "__main__":
    dbl_node = DoubleLinkedNode(1)
    dbl_node_1 = DoubleLinkedNode(2)
    dbl_node_2 = DoubleLinkedNode(3)
    dbl_node_1.prev = dbl_node
    dbl_node_1.next = dbl_node_2
    print(dbl_node_1.prev)
