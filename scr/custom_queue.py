class Node:

    def __init__(self, data, next_node=None):
        """
        Инициализация узла
        :param data: данные
        :param next_node: ссылка на следующий узел
        """
        self.data = data
        self.next_node = next_node


class Queue:

    def __init__(self, head=None, tail=None):  # по умолчанию None
        """
        Инициализация очереди
        :param начало и конец очереди по умолчанию None
        """
        self.head = head
        self.tail = tail

    def enqueue(self, data):
        """Добавляем данные в конец очереди"""
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue('data1')
    queue.enqueue('data2')
    queue.enqueue('data3')

    print(queue.head.data)
    print(queue.head.next_node.data)
    print(queue.tail.data)
    print(queue.tail.next_node)
    print(queue.tail.next_node.data)