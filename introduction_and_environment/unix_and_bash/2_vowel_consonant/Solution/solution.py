print("Enter a single lower case letter: ")
letter = input()
vowels = ["a", "e", "i", "o", "u"]

for vow in vowels:
    if letter == vow:
        data = "vowel"
    else:
        data = "consonent"

print(data)
