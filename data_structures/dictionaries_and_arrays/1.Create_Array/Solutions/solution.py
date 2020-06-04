from array import array
my_array = array('i', [12, 34, 56, 78, 90, 123])
buffer_info = my_array.buffer_info()
print(buffer_info)
