import unittest
from random import choice
from node import Node, DoubleLinkedNode
from task import LinkedList, DoubleLinkedList


class TestNode(unittest.TestCase):

    def test_is_valid(self):
        node = Node(1)
        node_1 = Node(2)
        not_node_object = "123"
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
        self.assertEqual(nodes_list[end_index], val)
        self.assertEqual(empty_nodes_list[0], val)

    def test_insert(self):
        init_length = 40
        nodes_list = LinkedList(range(init_length))
        valid = {0: "34", 2: [1, 2, 3], 20: 123, 7: "+", 4: "t", 6: "$", 17: "&", 30: "/",
                 1: DoubleLinkedList([1, 5]), 34: tuple(), 38: "*"}
        bad_index = (-1, 3400, 0.1, "df", [2], 0.7, False, -3, -300, "4", bytes(0xf), None, True)
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
        nodes_list.insert(0, 1)
        nodes_list.insert(init_length, 1)
        nodes_list.insert(2, 1)
        for _ in range(len(valid) ** 2):
            key = choice(tuple(valid.keys()))
            value = valid[key]
            nodes_list.insert(key, value)
            self.assertEqual(nodes_list[key], value, msg="Куда-то потерялось значение! index={0}"
                                                         ", value={1}".format(key, value))
        self.assertEqual(init_length + 3 + len(valid) ** 2, len(nodes_list))

    def test_add_link(self):
        node = DoubleLinkedNode(1)
        node_1 = DoubleLinkedNode(1)

        LinkedList.add_link(node, node_1)
        self.assertEqual(node.next, node_1)

        LinkedList.add_link(node_1, node)
        self.assertEqual(node_1.next, node)

    def test_recursive_linked_node_on_self(self):
        node = DoubleLinkedNode(1)
        with self.assertRaises(ValueError):
            LinkedList.add_link(node, node)

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
        for index in valid_index:
            value = nodes_list.is_valid_index(index)
            self.assertEqual(value, True, msg=f"Вернулся неожиданный результат")

    def test_is_valid_node(self):
        nodes_list = LinkedList(list(range(0, 5)))
        nodes = [Node(1), Node(10), Node(-1), DoubleLinkedNode(2), None]
        not_nodes = (DoubleLinkedList([1, 2, 3]), "23424", 324, -1, LinkedList([1, 2, 3]), False)

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

    def test_getitem(self):
        nodes_list = LinkedList(range(5))
        val = nodes_list[2]
        self.assertEqual(val, 2)

    def test_setitem__(self):
        val = 1
        nodes_list = LinkedList(range(3))
        nodes_list[0], nodes_list[1], nodes_list[2] = val, val, val
        self.assertEqual(len(nodes_list), 3)
        for i in nodes_list:
            self.assertEqual(i, val)

    def test_delitem(self):
        values = [1, "test", 3, "last_value"]
        nodes_list = LinkedList(values)
        del nodes_list[3]
        del nodes_list[0]
        del nodes_list[2]
        del nodes_list[1]
        self.assertEqual(len(nodes_list), 0)

    def test_len(self):
        nodes = LinkedList([1, 2, 3])
        length = len(nodes)
        self.assertIsInstance(length, int)
        self.assertEqual(length, 3)

    def test_str(self):
        nodes = LinkedList([1, 2, 3])
        value = str(nodes)
        self.assertIsInstance(value, str)
        self.assertEqual(value, "[1, 2, 3]")

    def test_to_list(self):
        nodes = LinkedList([1, 2, 3])
        list_ = nodes.to_list()
        self.assertIs(type(list_), list)
        self.assertEqual(len(nodes), 3)

    def test_repr(self):
        nodes = LinkedList([1, 2, 3])
        repr_string = repr(nodes)
        self.assertEqual(repr_string, "LinkedList([1, 2, 3])")

    def test_iterator(self):
        end_index = 5
        length = end_index - 1
        nodes_list = LinkedList(range(end_index))
        iterator = iter(nodes_list)
        for i in range(len(nodes_list)):
            self.assertEqual(next(iterator), nodes_list[i])
            if i > length:
                raise IndexError("Итератор короче, чем длина последовательности!")

    def test_iter(self):
        nodes_list = LinkedList(range(3))
        nodes_list_iter = iter(nodes_list)
        next(nodes_list_iter)

    def test_contains(self):
        nodes_list = LinkedList(range(5))
        value_from_collection = nodes_list[1]
        node = Node(22)
        self.assertEqual(nodes_list.__contains__(value_from_collection), True)
        self.assertEqual(nodes_list.__contains__(node), False)
        bad_values = (node, -1, 3400, 0.1, "df", [2], False, -3, -300, "4", bytes(0xf), None, True, nodes_list)
        for val in bad_values:
            self.assertEqual(nodes_list.__contains__(val), False)

    def test_pop(self):
        values = [1, "test", "last_value", 3]
        nodes_list = LinkedList(values)
        self.assertEqual(nodes_list.pop(1), "test")
        self.assertEqual(nodes_list.pop(0), 1)
        last_index = len(nodes_list) - 1
        val = nodes_list.pop(last_index)
        self.assertEqual(val, 3)
        self.assertEqual(nodes_list.pop(-1), "last_value")
        self.assertEqual(len(nodes_list), 0)

    def test_remove(self):
        values = [1, "test", 3, "last_value"]
        nodes_list = LinkedList(values)
        nodes_list.remove(3)
        nodes_list.remove("test")
        nodes_list.remove("last_value")
        nodes_list.remove(1)
        self.assertEqual(len(nodes_list), 0)

    def test_index(self):
        values = [1, "test", 3, "last_value"]
        nodes_list = LinkedList(values)
        self.assertEqual(nodes_list.index(values[0]), 0)
        self.assertEqual(nodes_list.index(values[len(values) - 1]), len(values) - 1)
        self.assertEqual(nodes_list.index("test"), 1)
        self.assertEqual(nodes_list.index(3), 2)

    def test_extend(self):
        elements_collection_1 = [1, 2, 3]
        elements_collection_2 = ["test_val", 5, 6]
        list_1 = LinkedList(elements_collection_1)
        list_2 = LinkedList(elements_collection_2)
        list_1.extend(list_2)
        self.assertIn("test_val", list_1)
        self.assertIn(6, list_1)
        self.assertIn(5, list_1)

    def test_add(self):
        elements_collection_1 = [1, 2, 3]
        elements_collection_2 = ["test_val", 5, 6]
        list_1 = LinkedList(elements_collection_1)
        list_2 = LinkedList(elements_collection_2)
        new_list = list_1 + list_2
        for item in elements_collection_1 + elements_collection_2:
            self.assertIn(item, new_list)
        # Исходные коллекции должны остаться нетронутыми
        self.assertEqual(len(list_1), len(LinkedList(elements_collection_1)))
        for element in list_1:
            self.assertIn(element, elements_collection_1)
            self.assertNotIn(element, elements_collection_2)

    def test_add_2(self):
        elements_collection_1 = [1, 2, 3]
        elements_collection_2 = ["test_val", 5, 6]
        list_1 = LinkedList(elements_collection_1)
        list_2 = LinkedList(elements_collection_2)

        new_list = list_1 + list_2

        self.assertEqual(6, new_list.tail.value)

    def test_iadd(self):
        elements_collection_1 = [1, 2, 3]
        elements_collection_2 = ["test_val", 5, 6]
        list_1 = LinkedList(elements_collection_1)
        list_2 = LinkedList(elements_collection_2)
        list_1 += list_2
        self.assertIn("test_val", list_1)
        self.assertIn(6, list_1)
        self.assertIn(5, list_1)

    def test_break_head(self):
        ll = LinkedList([1, 2, 3])
        ll.head = Node(100)

        self.assertEqual(100, ll.head.value)
        self.assertEqual(3, len(ll))
        print(ll)
        # self.assertEqual(3, ll[2])

    def test_break_head_2(self):
        ll = LinkedList([])
        ll.head = Node(100)

        self.assertEqual(1, len(ll))



