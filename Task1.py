class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def index(self, element):
        current = self.head
        index = 0
        while current:
            if current.data == element:
                return index
            index += 1
            current = current.next
        raise ValueError('There is no such element in the list')

    def pop(self):
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def insert(self, data, index):
        new_node = Node(data)
        if index < 0:
            return '\nIndex should be >= 0'
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for i in range(index-1):
                if current:
                    current = current.next
            new_node.next = current.next
            current.next = new_node

    def slice(self, start, stop):
        list2 = LinkedList()
        current = self.head
        index = 0
        while index < start-1:
            index += 1
            current = current.next
        for i in range(start, stop):
            current = current.next
            list2.append(current.data)
        return list2.print_list()


if __name__ == 'main':
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append("2")
    linked_list.append(1)
    linked_list.append("Stas")
    linked_list.print_list()
    print()
    print(linked_list.index(1))
    linked_list.pop()
    print()
    linked_list.print_list()
    linked_list.insert(66, 1)
    print()
    linked_list.print_list()
    print()
    linked_list.slice(1, 3)

