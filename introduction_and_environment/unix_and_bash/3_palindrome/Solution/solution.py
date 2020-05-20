print("Enter a string to test if it is a palindrome:")
line = input()

def pal_test(string):
    if string[::1] == string[::-1]:
        return True
    else:
        return False
is_palindrome = pal_test(line)

print(is_palindrome)
