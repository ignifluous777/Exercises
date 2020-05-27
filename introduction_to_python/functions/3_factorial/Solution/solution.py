# Code your solution here
print("Input an integer to find factorial value: ")
n = int(input())
def factor(x):
    if x == 0:
        return 0
    data = 1
    count = x
    while count >= 1:
       data *=  count
       count -= 1
    return data
result = factor(n)
print(result)
        
