set_1 = [3, 5, 7, 11]
set_2 = [3, "hello", 7, 13]
result = []
if len(set_1) == len(set_2):
    length = len(set_1)
elif len(set_1) > len(set_2):
    length = len(set_1)
else:
    length = len(set_2)
print(length)

for i in range(0, length - 1):
    if set_1[i] != set_2[i]:
        result.append(set_1.pop(i))
        result.append(set_2.pop(i))
    else:
        pass

print(result)
