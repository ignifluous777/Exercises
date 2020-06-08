class Stack:
  def __init__(self):
      self.head_node = None

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

  def empty(self):
      if self.head_node:
          return False
      return True

class Queue:
    def __init__(self):
        self.head_node = None
        self.tail_node = None
    def printList(self):
        temp = self.head_node
        while temp:
            print(f"{temp.value}")
            temp = temp.next
            
    def enqueue(self, value):
        new_node = ListNode(value)
        if not self.tail_node:
            self.head_node = new_node
            self.tail_node = new_node
        else:
            self.tail_node.next = new_node
            self.tail_node = new_node

    def dequeue(self):
        if not self.head_node:
            raise IndexError
        value = self.head_node.value
        self.head_node = self.head_node.next
        if not self.head_node:
            self.tail_node = None
        return value

    def empty(self):
        if self.head_node:
            return False
        return True

class ListNode:
  def __init__(self, value):
      self.value = value
      self.next = None

queue = Queue()
queue.enqueue(12)
queue.enqueue(34)
queue.enqueue(56)
queue.enqueue(78)

def reverse_queue(queue):
  stack = Stack()
  while not queue.empty():
      stack.push(queue.dequeue())
  while not stack.empty():
      queue.enqueue(stack.pop())

reverse_queue(queue)
queue.printList()
