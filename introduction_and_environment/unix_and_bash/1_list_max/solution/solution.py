# L = [152, 463, 1112, 1337, -10]
from provided_code import L

LIST_MAX = L[0]

if LIST_MAX < L[1]:
    LIST_MAX = L[1]
if LIST_MAX < L[2]:
    LIST_MAX = L[2]
if LIST_MAX < L[3]:
    LIST_MAX = L[3]
if LIST_MAX < L[4]:
    LIST_MAX = L[4]

print(LIST_MAX)
