# Code your solution here
print("Input an integer value: ")
number = int(input())
def numcheck(x):
    if x <= 100:
        data = "GREATNESS"
    else:
        data = "OOPS"
    return data

print(numcheck(number))
