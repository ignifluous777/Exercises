class Stack:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(f"{temp.value}")
            temp = temp.next

    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head
        
    def pop(self):
        if self.head:
            value = self.head.value
            self.head = self.head.next
            return value
        else:
            raise IndexError
        
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

stack_fruits = Stack()
stack_fruits.push("apple")
stack_fruits.push("banana")
stack_fruits.push("orange")
stack_fruits.push("watermelon")
stack_fruits.push("grapes")
stack_fruits.pop()
result = stack_fruits.printList()
