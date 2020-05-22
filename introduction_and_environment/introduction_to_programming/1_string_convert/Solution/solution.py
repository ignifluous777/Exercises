print("Enter a string in all upper case or lower case: ")
string = input()

if string.islower() == True:
    data = string.upper()
elif string.isupper() == True:
    data = string.lower()

print(data)
