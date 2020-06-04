from array import array
my_array = array('i',[12, 34, 56, 78, 90])

print("Enter position and value of an integer to enter into the array: ")
ins_pos = int(input())
ins_val = int(input())
my_array.insert(ins_pos, ins_val)

print(my_array)
