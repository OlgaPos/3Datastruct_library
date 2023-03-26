class Node:

    def __init__(self, data: dict, next_node=None):
        """
        Инициализация узла, который хранит
        :param data: словарь с данными
        :param next_node: ссылка на следующий узел
        """
        self.data = data
        self.next_node = next_node


class LinkedList:

    def __init__(self, head=None, tail=None):  # по умолчанию None
        """
        хранит ссылку на начало связанного списка и на его конец, т.е. на первый и последний Node.
        :param head и tail: по умолчанию None
        """
        self.head = head
        self.tail = tail

    def insert_beginning(self, data: dict):
        """Добавим данные словаря в начало списка"""
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data: dict):
        """Добавим данные словаря в конец списка"""
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def print_ll(self):
        """Выводим в консоль данные из односвязанного списка"""
        ll_string = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        print(ll_string)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_beginning({'id': 1})
    ll.insert_at_end({'id': 2})
    ll.insert_at_end({'id': 3})
    ll.insert_beginning({'id': 0})
    ll.print_ll()
    # {'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None
