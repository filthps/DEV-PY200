from weakref import ref


class Node:
    def __init__(self, val: int = 1):
        self.value = val
        self._next = None

    def is_valid(self, val):
        if not isinstance(self, type(val)):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, val):
        self.is_valid(val)
        self._next = val

    def __repr__(self):
        return f"Node({self.value}, Node({self.next}))"

    def __str__(self):
        return str(self.value)


class DoubleLinkedNode(Node):

    def __init__(self, val):
        super().__init__(val)
        self._prev = None

    @property
    def prev(self):
        if self._prev is None:
            return None
        return self._prev()

    @prev.setter
    def prev(self, value):
        self.is_valid(value)
        self._prev = ref(value)

    def __repr__(self):
        name = self.__class__.__name__
        return f"{name}({name}({self.prev}), {self.value}, {name}({self.next}))"
