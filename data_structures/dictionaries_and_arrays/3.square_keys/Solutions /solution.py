num = int(input("Enter a number: "))

def enter_num(num):
    my_dict = {}
    for i in range(num + 1):
        my_dict[i] = i**2
    return my_dict

print(enter_num(num))
