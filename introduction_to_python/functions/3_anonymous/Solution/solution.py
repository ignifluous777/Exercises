# Code your solution here
def divthirteen(*args):
    data = [arg for arg in args if arg % 13 == 0]
    return data
result = divthirteen(1, 13, 35, 39, 78, 97)
print(result)
