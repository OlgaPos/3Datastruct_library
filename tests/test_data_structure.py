import unittest
from scr.data_structure import Node, Stack
from scr.custom_queue import *


class TestNode(unittest.TestCase):
    """Тест класса Node"""

    def test_node_init(self):
        """Проверим, что значение передаётся в узел"""
        node = Node(10)
        assert node.data == 10
        assert node.next_node is None

    def test_node_next_node(self):
        """Проверим, что next_node ссылается на узел"""
        node1 = Node(10)
        node2 = Node(220, node1)
        assert node2.next_node is node1


class TestStack(unittest.TestCase):
    """Создадим и заполним стэк"""
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    def test_push(self):
        """Проверим, что данные записались и вызываются из стэка корректно"""
        self.assertEqual(self.stack.top.data, 2)
        self.assertEqual(self.stack.top.next_node.data, 1)
        self.assertEqual(self.stack.top.next_node.next_node, None)

    def test_pop(self):
        """Проверим, что данные удаляются из стэка корректно"""
        self.assertEqual(self.stack.pop(), 3)



