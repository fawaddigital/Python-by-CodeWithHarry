# A dictionary is a collection of data stored in key-value pairs.
'''
    Dictionaries are written using curly braces {}.
    Data is stored as key : value pairs.
    Keys must be unique.(Cannot contain Duplicate keys)
    Dictionaries are mutable (can be changed).
'''
# Syntex
student = {
    "name" : "fawad",   # Name is 'Key' and 'Ali' is its value
    "age" : 20,
    "Degree" : "CS",
    "list" : [1,2,3]
}
print(student)
print(student["name"])   # Prints "fawad"
print(student["list"]) # Prints "[1,2,3]"

d = {}  # Empty Dictionary
print(type(d))