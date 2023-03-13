class Node:

    def __init__(self, data, next_node=None):
        """
        Инициализация узла
        :param data: данные
        :param next_node: ссылка на следующий узел
        """
        self.data = data
        self.next_node = next_node


class Stack:

    def __init__(self, top=None):  # по умолчанию None
        """
        Инициализация стэка
        :param top: по умолчанию None
        """
        self.top = top

    def push(self, data):
        """Добавляет данные в стэк"""
        self.top = Node(data, self.top)

    def pop(self):
        """Удаляет данные из стэка"""
        data = self.top.data
        self.top = self.top.next_node
        return data


if __name__ == '__main__':
    # n1 = Node(5, None)
    # n2 = Node('a', n1)
    # print(n1.data)
    # print(n2.data)
    # print(n1)
    # print(n2.next_node)
    #
    # stack = Stack()
    #
    # stack.push('data1')
    # stack.push('data2')
    # stack.push('data3')
    # print(stack.top.data)
    # print(stack.top.next_node.data)
    # print(stack.top.next_node.next_node.data)
    # print(stack.top.next_node.next_node.next_node)
    # print(stack.top.next_node.next_node.next_node.data)

    stack = Stack()
    stack.push('data1')
    data = stack.pop()

    # стэк стал пустой
    print(stack.top)

    # pop() удаляет элемент и возвращает данные удаленного элемента
    print(data)

    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    data = stack.pop()

    # теперь последний элемента содержит данные data1
    print(stack.top.data)

    # данные удаленного элемента
    print(data)
