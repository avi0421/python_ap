# A dictionary is a built-in data structure in Python that allows you to store a collection of key-value pairs.
# dictionary is mutable and it is unordered

my_dict = {
    "std_id": 123,
    "std name": "ABC",
    "course": "MCA"
}
print(my_dict)

x=my_dict['course']
print("The course selected is",x)

x=my_dict.get("std_id")
print(x)

# find all keys present in dictionary
y=my_dict.keys()
print("The keys present are:",y)
# To update dictionary element
my_dict.update({"std_name":"Sameer"})
print(my_dict)
# To add new element in dictionary
my_dict["fees"]=70000
print(my_dict)

my_dict["std_addr"]="Thane"
print(my_dict)

#to remove certain element from dictionary 
my_dict.popitem()
print(my_dict)

# looping over dictionary
for i in my_dict:
    print(i)

# to get keys from dictionary
for i in my_dict.keys():
    print(i)
# to het values from dictionary
for i in my_dict.values():
    print(i)

# to get items (keys & values) from dictionary
for x,y in my_dict.items():
    print(x,y)