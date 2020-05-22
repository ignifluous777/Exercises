string = "BYTE ACADEMY"
data = []
vowels = ["A", "E", "I", "O", "U"]
lst_string = list(string)

for i in lst_string:
    if i.isalpha() == True:
        if i in vowels:
            pass
        else:
            data.append(i)
    else:
        pass
    
print(data)
    
