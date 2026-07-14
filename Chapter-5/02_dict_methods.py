student = {
    "name" : "fawad",   
    "age" : 20,
    "Degree" : "CS",
    0 : "ali"
}
    # Dictionary Methods
print(student.items())  # Returns a list of (key,value)tuples
print(student.keys())   #  Returns a list containing dictionary's keys.
print(student.values()) #  Returns a list containing dictionary's pairs.

# Updating value in a dict
student.update({"age": 22, "Semester": "4th"})   # Updates Age value, Also add the new Pair.
print(student)

my_dict = {
    "name" : "Ali",
    "Age" : 20,
    "Degree" : "MLT",
    "Sem" : "6th"
}
#  Returns the value of a key
print(my_dict.get("Age"))

# Removes  a specific key.
my_dict.pop("Degree")
print(my_dict)

# Removes the last inserted key-value pair.
my_dict.popitem()
print(my_dict)
