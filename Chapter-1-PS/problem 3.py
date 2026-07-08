import os

# specify the directory path (change this as needed)
path = "."

# get the list of contents
contents = os.listdir(path)

# print each item
print("Directory contents:")
for item in contents:
    print(item)