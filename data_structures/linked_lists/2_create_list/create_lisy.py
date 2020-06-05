# A LinkedList is either:
# None
# Node

class Node:
    # first: int
    # rest: LinkedList
    def __init__(self, first, rest = None):
        self.first = first
        self.rest = rest

# Write a function named create_list that consumes a number n and returns a LinkedList of 1,2,..,n 
# create_list(3) -> Node(1, Node(2, Node(3, None)))
def create_list(n):
    return recursive(n, 1) 
def recursive(n, x):
    if x > n:
        return None
    else:
        return Node(x, recursive(n, x+1))

ll = create_list(5)

