import unittest

from task import Node


class TestCase(unittest.TestCase):  # TODO наследоваться от unittest.TestCase
    def test_init_node_without_next(self):
        """Проверить следующий узел после инициализации с аргументом next_ по умолчанию"""
        node = Node(5)
        self.assertIsNone(node.next)

    def test_init_node_with_next(self):
        """Проверить следующий узел после инициализации с переданным аргументом next_"""
        node = Node(5)
        self.assertEqual(5, node.value)

    def test_repr_node_without_next(self):
        """Проверить метод __repr__, для случая когда нет следующего узла."""
        right_node = Node("right")
        left_node = Node("left", next_=right_node)

        self.assertIs(right_node, left_node.next)

        self.assertEqual("right", right_node.value)

    @unittest.skip("Будет дорабатываться")
    def test_repr_node_with_next(self):
        """Проверить метод __repr__, для случая когда установлен следующий узел."""
        node = Node(1)
        self.assertEqual(f"Node(1, None)", repr(node))

    def test_str(self):
        some_value = 5
        node = Node(some_value)

        self.assertEqual(str(some_value), str(node))

    def test_is_valid(self):
        Node.is_valid(Node(1))
        Node.is_valid(None)

        with self.assertRaises(TypeError, msg="Комментарий. Что именно пошло не так. Должно быть то-то"):
            Node.is_valid(2)

