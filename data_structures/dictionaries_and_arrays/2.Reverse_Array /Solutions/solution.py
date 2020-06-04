from array import array

array_num = array("i", [1, 23, 456, 7890])
reverse_array = array("i", [])
for element in array_num[::-1]:
    reverse_array.append(element)
print(reverse_array)
