# Code your solution here
def summer(lst):
    total = 0
    for val in lst:
        total += val
    return total
l = [10, 20, 30, 40, 50, 60]
result = summer(l)
print(result)
