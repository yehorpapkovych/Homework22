from Task1 import Node
from Task1 import LinkedList

class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def push(self, z):
        return self.stack.append(z)

    def pop(self):
        return self.stack.pop()

    def isempty(self):
        return self.stack.head == None

    def size(self):
        current = self.stack.head
        size = 0
        while current:
            size += 1
            current = current.next
        return size

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.stack.print_list()
print()
stack.pop()
stack.stack.print_list()
print()
print(stack.size())