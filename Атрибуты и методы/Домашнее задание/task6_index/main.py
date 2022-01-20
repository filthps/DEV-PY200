from typing import Optional, Iterable, Any

class Node:
    def __init__(self, val):
        self.value = val
        self._next: ["Node"] = Node

    def __repr__(self):
        if self.next:
            return f"Node({self.value}, Node({self.value + 1}))"
        return f"Node({self.value})"

    def __str__(self):
        if self.next:
            return f"Node({self.value}, Node({self.value + 1}))"
        return f"Node({self.value})"

    
    def is_valid(self, node: ["Node"]):
        if not isinstance(self, node.__class__):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, val):
        self.is_valid(val)
        self._next = val


class LinkedList:
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.len = 0
        self.head: Optional[Node] = None
        self.tail = self.head

        if data is not None:
            for value in data:
                self.append(value)

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.len += 1

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def index(self, node):
        if not type(node) is Node:
            raise TypeError
        return node.value


    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"


if __name__ == "__main__":
    l = [1,2,3,4,5]
    nodes = LinkedList(l)
    node = nodes[3]
    index = nodes.index(node)
    print(f"Нода {node} индекс ноды в связанном списке {index}")
