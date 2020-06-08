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

    def delete(self, pos):
        if not self.head:
            return
        temp = self.head
        if pos == 0:
            self.head = temp.next
            temp = None
            return
        for i in range(pos - 1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        next = temp.next.next
        temp.next = None
        temp.next = next

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def create_conts():
    stack_continents.push('North America')
    stack_continents.push('Europe')
    stack_continents.push('Asia')
    stack_continents.push('South America')
    stack_continents.push('Antartica')
    stack_continents.push('Australia')
    stack_continents.push('Africa')
    return

stack_continents = Stack()
create_conts()

stack_continents.delete(5)
stack_continents.printList()



    
