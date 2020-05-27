# Code your solution here
def iseven(*args):
    data = [arg for arg in args if arg % 2 == 0]
    return data
result = iseven(34, 23, 75, 1, 24, 66, 79, 99)
print(result)
