# Code your solution here
from queue import *

queue_a = Queue(5)

def queue():
    queue_a.put(12)
    queue_a.put(34)
    queue_a.put(56)
    queue_a.put(78)
    queue_a.put(90)

data = queue()

result = queue_a

while not result.empty():
    print(result.get())
