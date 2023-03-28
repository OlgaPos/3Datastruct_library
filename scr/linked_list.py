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

    def to_list(self) -> list:
        """Записываем в список данные из односвязанного списка"""
        _list = []
        node = self.head
        while node is not None:
            _list.append(node.data)
            node = node.next_node
        return _list

    def get_data_by_id(self, id: int) -> dict:
        """По ключу возвращаем словарь из односвязанного списка"""
        _list = self.to_list()
        try:
            for item in _list:
                if type(item) == dict and item['id'] == id:
                    return item
            else:
                raise TypeError
        except TypeError:
            print('Данные не являются словарем или в словаре нет id')


if __name__ == '__main__':
    # ll = LinkedList()
    #
    # ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    # ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
    # ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
    # ll.insert_beginning({'id': 0, 'username': 'serebro'})

    # метод to_list()
    # lst = ll.to_list()
    # for item in lst: print(item)
    # {'id': 0, 'username': 'serebro'}
    # {'id': 1, 'username': 'lazzy508509'}
    # {'id': 2, 'username': 'mik.roz'}
    # {'id': 3, 'username': 'mosh_s'}

    # get_data_by_id()
    # user_data = ll.get_data_by_id(3)
    # print(user_data)
    # {'id': 3, 'username': 'mosh_s'}
    #
    # # работа блока try/except
    ll = LinkedList()
    ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    ll.insert_at_end('idusername')
    ll.insert_at_end([1, 2, 3])
    ll.insert_at_end({'id': 2, 'username': 'mosh_s'})
    #
    user_data = ll.get_data_by_id(2)
    # # Данные не являются словарем или в словаре нет id.
    # # Данные не являются словарем или в словаре нет id.
    print(user_data)
    # {'id': 2, 'username': 'mosh_s'}

    # ll = LinkedList()
    # ll.insert_beginning({'id': 1})
    # ll.insert_at_end({'id': 2})
    # ll.insert_at_end({'id': 3})
    # ll.insert_beginning({'id': 0})
    # ll.print_ll()
    # {'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None
