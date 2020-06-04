import json
def convert(dictionary):
    data = json.dumps(dictionary)
    return data

my_dict = {"students": ["jon", "ad", "matt", "jakai"],
           "teachers": ["anton", "greg", "wasif"]
           }

result = convert(my_dict)
print(result)
