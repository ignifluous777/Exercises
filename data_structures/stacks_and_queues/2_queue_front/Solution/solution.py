from queue import *

queue_a = LifoQueue(5)

def queue():
    queue_a.put(12)
    queue_a.put(34)
    queue_a.put(56)
    queue_a.put(78)
    queue_a.put(90)

result = queue()

print(queue_a.get())
