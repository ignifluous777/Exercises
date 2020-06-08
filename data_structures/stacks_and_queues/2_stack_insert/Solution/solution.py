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

    def insert_idx(self, val, pos):
        if not self.head:
            print("Empty Linked List")
            return None
        temp = self.head
        if pos == 0:
            self.head = val
            self.next = temp
        for i in range(pos):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        val = Node("Earth")
        temp_nxt = temp.next
        val.next = temp.next
        temp.next = val
            
            
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

stack_planets = Stack()
stack_planets.push("Neptune")
stack_planets.push("Uranus")
stack_planets.push("Saturn")
stack_planets.push("Mars")
stack_planets.push("Venus")
stack_planets.push("Mercury")
stack_planets.insert_idx("Earth", 1)
stack_planets.printList()

