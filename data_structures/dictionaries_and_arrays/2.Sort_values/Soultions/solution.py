import operator
my_dict = {2: 2, 1: 1, 3: 3}
results = sorted(my_dict.items(), key=lambda v: operator.itemgetter(1)(v))
print("Ascending", results)
results = sorted(my_dict.items(), key=lambda v: operator.itemgetter(1)(v), reverse=True)
print("Decending", results)

