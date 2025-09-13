#  dictionary in python

# dictionaries are used to store data values in key:value pairs

# They are unorderd , mutable(Changable) and don't allow duplicate keys

# info={
#     "key":"value",
#     "name":"Akshay Yadav",
#     "learning":["C","c++", "python", "javascript", "java"],
#     "age":"23",
#     "is Adult":True,
#     "CGPA":7.4,
#     "Topics":("dist","set")
# }

# info["CGPA"]=7.8          Changes the values by using the key,  info[key]=value
# print(info)


# null_dist={}              creating a null distinory



#  Nested Distinary in python 

# Nested Distionaries

nested={
    "key":"value",
    "name":"Akshay Yadav",
    "learning":["C","c++", "python", "javascript", "java"],
    "Subject":{
        "c":98,
        "c++":83,
        "python":94,
        "Grade":"Very Good"
    }
}


# print(nested)
# print(nested["Subject"])
# print(nested["Subject"]["c"])



#  Methods

# dist.keys()     returns all keys
# dist.values()     returns all values
# dist.items()      returns all (key,val)   pairs as tuples
# dist.get("key")   returns the key accrordings to value
# dist.update(newDict)      insert the specified items to the dictionary

# print(nested.keys())                  dict_keys(['key', 'name', 'learning', 'Subject'])

# print(list(nested.keys()))          ['key', 'name', 'learning', 'Subject']

# print(nested.values())              dict_values(['value', 'Akshay Yadav', ['C', 'c++', 'python', 'javascript', 'java'], {'c': 98, 'c++': 83, 'python': 94, 'Grade': 'Very Good'}])

# print(nested.items())      returns in tuples ------>         dict_items([('key', 'value'), ('name', 'Akshay Yadav'), ('learning', ['C', 'c++', 'python', 'javascript', 'java']), ('Subject', {'c': 98, 'c++': 83, 'python': 94, 'Grade': 'Very Good'})])

# data= list(nested.items())
# print(data)
# print(data[:3])             [('key', 'value'), ('name', 'Akshay Yadav'), ('learning', ['C', 'c++', 'python', 'javascript', 'java'])]

nested.update({"new":"content"})
print(nested)

# print(nested)           {'key': 'value', 'name': 'Akshay Yadav', 'learning': ['C', 'c++', 'python', 'javascript', 'java'], 'Subject': {'c': 98, 'c++': 83, 'python': 94, 'Grade': 'Very Good'}, 'new': 'content'}


