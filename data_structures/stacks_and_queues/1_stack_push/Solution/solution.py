import queue

class Stack:
    def __init__(self, head_node = None):
        self.head_node = head_node

    def __str__(self):
        if self.head_node:
            return f"<{self.head_node}>"
        else:
            return "<>"

    def push(self, value):
        new_head = ListNode(value)
        new_head.next = self.head_node
        self.head_node = new_head

    def pop(self):
        if self.head_node:
            value = self.head_node.value
            self.head_node = self.head_node.next
            return value
        else:
            raise IndexError

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
      
stack_a = Stack()
stack_a.push("C")
stack_a.push("Perl")
stack_a.push("C++")
stack_a.push("Java")
stack_a.push("Python")
print(stack_a)

