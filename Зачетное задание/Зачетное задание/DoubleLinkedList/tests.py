import unittest
from node import Node, DoubleLinkedNode


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
        repr_string = repr(node)
        #with self.assertRaises(Exception):
            #print(repr_string)
            #Node(1, next_=repr_string)
        self.assertEqual(repr_string, "Node(2)")

    def test_str(self):
        pass

class TestDoubleLinkedNode(unittest.TestCase):
    pass
