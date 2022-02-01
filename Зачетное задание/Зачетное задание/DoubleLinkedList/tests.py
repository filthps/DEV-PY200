import unittest
from random import choice
from node import Node, DoubleLinkedNode
from task import LinkedList, DoubleLinkedList


class TestNode(unittest.TestCase):

    def test_is_valid(self):
        node = Node(1)
        node_1 = Node(2)
        not_node_object = "123"
        with self.failUnlessRaises(TypeError):
            node.next = node_1
        with self.assertRaises(TypeError):
            node.next = not_node_object

    def test_repr(self):
        node = Node(2)
        self.assertEqual(repr(node), "Node(2)")

    def test_str(self):
        node = Node(2)
        self.assertEqual(str(node), "2")
        
        
class TestDoubleNode(unittest.TestCase):

    def test_is_valid(self):
        node = DoubleLinkedNode(1)
        node_1 = DoubleLinkedNode(2)
        invalid_object = "123"
        with self.failUnlessRaises(TypeError):
            node.next = node_1
        with self.assertRaises(TypeError):
            node.next = invalid_object

    def test_repr(self):
        node = DoubleLinkedNode(2)
        self.assertEqual(repr(node), "DoubleLinkedNode(2)")

    def test_str(self):
        node = DoubleLinkedNode(2)
        self.assertEqual(str(node), "2")


class TestLinkedNode(unittest.TestCase):
    
    def test_append(self):
        end_index = 50
        empty_nodes_list = LinkedList()
        nodes_list = LinkedList(list(range(0, end_index)))

        val = 1
        empty_nodes_list.append(val)
        nodes_list.append(val)

    def test_insert(self):
        end_index = 50
        nodes_list = LinkedList(list(range(0, end_index)))
        
        valid_index_tuple = (0, end_index - 1, 20, 2, 4, 6, 17)
        bad_index = (end_index + 1, -1, 100, 0.1, "df", [2], 0.7, False, -3, -300, "4", bytes(0xf), None, True)
        falls_counter = 0
        for index in bad_index:
            try:
                nodes_list.insert(index, 1)
            except TypeError:
                falls_counter += 1
            except IndexError:
                falls_counter += 1
        self.assertEqual(falls_counter, len(bad_index),
                         msg=f"Ожидалось {len(bad_index)} ошибок, выявлено {falls_counter}!")
        for _ in range(len(valid_index_tuple) ** 2):
            nodes_list.insert(4, 1)  # В конец
            nodes_list.insert(0, 1)  # В начало
            nodes_list.insert(2, 1)  # В середину
            nodes_list.insert(choice(valid_index_tuple), 1)  # Произвольно

    @unittest.skip("Нет определённости относительно ссылки ноды на ссаму себя!")
    def test_add_link(self):
        node = DoubleLinkedNode(1)
        node_1 = DoubleLinkedNode(1)

        LinkedList.add_link(node, node_1)
        self.assertEqual(node.next, node_1)

        LinkedList.add_link(node_1, node)
        self.assertEqual(node_1.next, node)

        LinkedList.add_link(node_1, node_1)
        self.assertEqual(node_1.next, node_1)

    def test_is_valid_index(self):
        end_index = 50
        nodes_list = LinkedList(list(range(0, end_index)))

        valid_index = (0, end_index, 20, 2, 4, 6, 17)
        bad_index = (-1, end_index + 1, end_index + 101, 76)
        bad_type = ("d", [2], "4", LinkedList([1]), bytes(0xf), Node(3), None, "1", True)

        falls_counter_type, falls_counter_index = 0, 0
        for index in bad_type:
            try:
                nodes_list.is_valid_index(index)
            except TypeError:
                falls_counter_type += 1
        self.assertEqual(falls_counter_type, len(bad_type))

        for index in bad_index:
            try:
                nodes_list.is_valid_index(index)
            except IndexError:
                falls_counter_index += 1
        self.assertEqual(falls_counter_index, len(bad_index))

        with self.assertRaises((IndexError, TypeError,)):
            for index in valid_index:
                value = nodes_list.is_valid_index(index)
                self.assertEqual(value, True, msg="Вернулся неожиданный результат!")

    def test_is_valid_node(self):
        nodes_list = LinkedList(list(range(0, 5)))
        nodes = [Node(1), Node(10), Node(-1), DoubleLinkedNode(2)]
        not_nodes = (None, DoubleLinkedList([1, 2, 3]), "23424", 324, -1, LinkedList([1, 2, 3]), False)

        for node in nodes:
            self.assertEqual(nodes_list.is_valid_node(node), True, msg="Вернулся неожиданный результат!")

        counter = 0
        for not_node in not_nodes:
            try:
                nodes_list.is_valid_node(not_node)
            except TypeError:
                counter += 1
        self.assertEqual(counter, len(not_nodes))

    def test_find_node(self):
        end_index = 50
        nodes_list = LinkedList(list(range(0, end_index)))

        node = nodes_list.find_node(0)
        self.assertIsInstance(node, Node)

    def move_from_head(self):
        ...

    def test_getitem__(self):
        pass

    def test_setitem__(self):
        ...

    def test_delitem__(self):
        ...

    def __len__(self):
        pass

    def __str__(self):
        pass

    def to_list(self):
        pass

    def __repr__(self):
        ...

    def iterator(self):
        pass

    def __iter__(self):
        pass

    def __contains__(self, item):
        pass

    def pop(self, index: int = ...):  # ...??
        pass

    def remove(self, node=None) -> None:
        pass

    def index(self, node):
        pass

    def extend(self, items):
        pass
