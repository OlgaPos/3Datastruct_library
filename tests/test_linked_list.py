import unittest
from scr.linked_list import *


class TestLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.ll = LinkedList()
        self.ll.insert_beginning({'id': 1})
        self.ll.insert_at_end({'id': 2})
        self.ll.insert_at_end({'id': 3})
        self.ll.insert_beginning({'id': 0})

    def test_insert(self):
        self.assertEqual(self.ll.head.data, {'id': 0})
        self.assertEqual(self.ll.head.next_node.data, {'id': 1})
        self.assertEqual(self.ll.tail.data, {'id': 3})


class TestLinkedList2(unittest.TestCase):
    def setUp(self) -> None:
        self.lll = LinkedList()
        self.lll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.lll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        self.lll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        self.lll.insert_beginning({'id': 0, 'username': 'serebro'})

    def test_to_list(self):
        self.assertEqual(len(self.lll.to_list()), 4)
        self.assertEqual(self.lll.to_list(), [{'id': 0, 'username': 'serebro'},
                                              {'id': 1, 'username': 'lazzy508509'},
                                              {'id': 2, 'username': 'mik.roz'},
                                              {'id': 3, 'username': 'mosh_s'}])


class TestLinkedList3(unittest.TestCase):
    def setUp(self) -> None:
        self.llll = LinkedList()
        self.llll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.llll.insert_at_end('idusername')
        self.llll.insert_at_end([1, 2, 3])
        self.llll.insert_at_end({'id': 2, 'username': 'mosh_s'})

    def test_get_data_by_id(self):
        self.assertEqual(self.llll.get_data_by_id(2), {'id': 2, 'username': 'mosh_s'})
        self.assertEqual(self.llll.get_data_by_id(3), None)
        self.assertEqual(self.llll.get_data_by_id(5), None)
