# Code your solution here
print("Input a boolean value (true or false): ")
x = input()
def shutdown(z):
    if z == "true":
        return "SHUTDOWN"
    else:
        return "SHUTDOWN ABORTED"
result = shutdown(x)
print(result)
