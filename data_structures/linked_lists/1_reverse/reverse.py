# A LinkedList is either:
# None
# Node

class Node:
    # first: int
    # rest: LinkedList
    def __init__(self, first, rest = None):
        self.first = first
        self.rest = rest

# Write a function named reverse that consumes a LinkedList ll and returns a LinkedList with all the elements reversed
# reverse(Node(1, Node(2, Node(3, None)))) -> Node(3, Node(2, Node(1, None)))
def reverse(ll):
    def recursive(cur, prev):
        if not cur:
            return prev
        nxt = cur.rest
        cur.rest = prev
        prev = cur
        cur = nxt
        return recursive(cur, prev)
    new_node = recursive(cur=ll, prev=None)
    return new_node
ll = Node(1, Node(2, Node(3, None)))
ll_rv = reverse(ll)
