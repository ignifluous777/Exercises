class Stack:
    def __init__(self, head_node = None):
        self.head_node = head_node

stack_1 = Stack()

if stack_1.head_node == None:
    print(True)
else:
    print(False)
