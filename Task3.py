from Task1 import Node
from Task1 import LinkedList

class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, item):
        return self.queue.append(item)

    def dequeue(self):
        self.queue.head = self.queue.head.next

    def isempty(self):
        return self.stack.head == None

    def size(self):
        current = self.queue.head
        size = 0
        while current:
            size += 1
            current = current.next
        return size

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.queue.print_list()
print()
queue.dequeue()
queue.queue.print_list()
print()
print(queue.size())