from weakref import ref


class Node:
    def __init__(self, val: int = 1, next: ["Node"] = None):
        self.value = val
        self._next = next

    @classmethod
    def is_valid(cls, val):
        if not isinstance(cls, (val, None,)):
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

    def __del__(self):
        print(f"{self.__class__.__name__}({self.value}) - удалена")


class DoubleLinkedNode(Node):

    def __init__(self, val, next = None):
        super().__init__(val, next=next)
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
