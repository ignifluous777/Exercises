from queue import *

q = Queue()

q.put(12)
q.put(34)
q.put(56)
q.put(78)
q.put(90)

def min(Q):
    prev = Queue()
    new = Queue()
    while not Q.empty():
        val = Q.get()
        prev.put(val)
        new.put(val)
    if prev.empty: return -1
    minval = prev.get()
    idx = 0
    curr_idx = 0
    while not prev.empty():
        val = prev.get()
        curr_idx +=1
        if val <= minval:
            minval = val
            idx = curr_idx
    while not new.empty():
        Q.put(new.get())
    return index

def mintorear(Q, minidx):
    if minidx == -1: return Q
    prev = Queue()
    for i in range(minidx):
        val = Q.get()
        prev.put(val)
    minval = Q.get()
    while not Q.empty():
        value = Q.get()
        prev.put(val)
    prev.put(minval)
    return prev

def sortQueue(q): 
    for i in range(1, q.qsize() + 1): 
        min_idx = min(q)  
        mintorear(q, min_idx)

sortQueue(q)
