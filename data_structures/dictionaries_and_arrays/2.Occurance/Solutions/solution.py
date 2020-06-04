from array import array

array_num = array("i", [1, 2, 2, 3, 4, 4, 5])
element = int(input("Input integer 1-5: "))
count = 0
for val in array_num:
    if element == val:
        count +=1
print(count)


