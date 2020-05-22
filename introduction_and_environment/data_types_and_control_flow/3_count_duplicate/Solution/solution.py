list_dup = [1, 4, 4, 3, 4]

dict_lst = {i:list_dup.count(i) for i in list_dup}
print(dict_lst)

tot = 0
for value in dict_lst.values():
    if value > tot:
        tot = value
    else:
        pass
        
print(tot)


