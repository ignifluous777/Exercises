# A LinkedList is either:
# None
# Node

class Node:
    # first: int
    # rest: LinkedList
    def __init__(self, first, rest = None):
        self.first = first
        self.rest = rest

# Write a function named map that consumes a LinkedList ll and a function f that consumes a number and returns another number. The function map should return a ll with each element changed according to f
# map(Node(1, Node(2, Node(3, None))), lambda x: x**2) -> Node(1, Node(4, Node(9, None)))
def map_fun(ll, f):
    if ll != None:
        ll.first = f(ll.first)
        return map_fun(ll.rest, f)

def funct(num):
    return num**2
f = funct
    
ll = Node(1, Node(2, Node(3, None)))

map_fun(ll, f)
