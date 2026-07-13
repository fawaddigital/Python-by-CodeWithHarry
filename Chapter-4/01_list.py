#   A list is a collection of multiple items stored in a single variable using square [] brakets.
#   Lists are ordered, meaning items keep their position.
#   Lists can be changed (they are mutable).

fruits = ["apple","orange", 5, 118.5, True, "fawad"]    # Here fruit is a list that contains different types of data.
print(fruits)

    # You can do indexing in a list
print(fruits[1])    # Prints Orange only.
print(fruits[1:4])  # Prints only from 1 to 3 index.(Last value not included)


    # You can change a value inside list
fruits[0] = "Mango"     # Value changes from Apple to  Mango.
print(fruits[0])
