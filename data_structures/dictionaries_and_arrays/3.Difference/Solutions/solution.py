from array import *

array_num = array("i", [12, 23, 34, 45, 56])

def find_greatest(arr):
    greatest = arr[0]
    for i in arr:
        if i > greatest:
            greatest = i
    return greatest

def find_lowest(arr):
    lowest = arr[0]
    for i in arr:
        if i < lowest:
            lowest = i
    return lowest

result = find_greatest(array_num) - find_lowest(array_num)
print(result)
