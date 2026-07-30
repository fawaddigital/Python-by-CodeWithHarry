f = open("file.text")
print(f.read())
f.close()

#   Why we use the with statement?
#   The same can be done using the with statement.
#   It automatically closes the file.
#   Shorter and cleaner code. It is recommended to use the with statement when working with files.

with open("file.text") as f:
    print(f.read())