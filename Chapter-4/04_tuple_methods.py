data = (1, 3, 5, 18, False, 18, "fawad", "ali")
print(data)

    # Tuple methods / Functions
# Check lenght of a tuple
print(len(data))

# Counts how many times an item appears.
no = data.count(18)
print(no)

# Returns the position (index) of a value
i = data.index("fawad")
print(i)

# Slicing in tuple
slice = data[1:5]
print(slice)

# Joins two tuples
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)

# Repeats a tuple
t = (1, 2)
print(t * 3)