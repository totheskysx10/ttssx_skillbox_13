class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def get(self, index):
        if index < 0:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        if current is None:
            raise IndexError("Index out of range")
        return current.data

    def remove(self, index):
        if index < 0:
            raise IndexError("Index out of range")
        if index == 0:
            if self.head is not None:
                self.head = self.head.next
                if self.head is None:
                    self.tail = None
        else:
            current = self.head
            for _ in range(index - 1):
                if current is None or current.next is None:
                    raise IndexError("Index out of range")
                current = current.next
            if current.next is None:
                raise IndexError("Index out of range")
            current.next = current.next.next
            if current.next is None:
                self.tail = current

    def __str__(self):
        return f"[{', '.join(str(el) for el in self)}]"

    def __iter__(self):
        self.current_iterator = self.head
        return self

    def __next__(self):
        while self.current_iterator:
            item = self.current_iterator.data
            self.current_iterator = self.current_iterator.next
            return item
        raise StopIteration




my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)