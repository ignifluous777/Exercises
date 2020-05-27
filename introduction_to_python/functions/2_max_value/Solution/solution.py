# Code your solution here
print("Input three integer values: ")
a = int(input())
b = int(input())
c = int(input())
def checkmax(x, y, z):
    max_value = max(x, y, z)
    return max_value

result = checkmax(a, b, c)
print(result)
