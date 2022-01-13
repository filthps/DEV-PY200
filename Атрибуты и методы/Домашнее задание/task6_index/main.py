
class Node:
    def __init__(self, value):
        self.node = Node(value)
        self.__next = None

    def get_next(self):
        return self.node.__next

    def has_next(self):
        return bool(self.get_next())

    def set_next(self, node):
        if not isinstance(self, node):
            raise TypeError()
        self.node.__next = node

    def __repr__(self):
        return f"{self.__class__.__name__}({self.node})"


class LinkedNodes:

    def __init__(self, values):
        self.__head = None
        self.__len = 0

    def append(self):
        pass

    def steps_to_next(self, index):
        node = None
        while

    @staticmethod
    def union_nodes(left_node: Node, right_node: Node):
        left_node.set_next(right_node)

if __name__ == "__main__":
    pass
