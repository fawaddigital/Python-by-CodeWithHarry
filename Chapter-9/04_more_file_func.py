f = open("file.text")

# line1 = f.readline()  # readline() → Read one line at a time.
# print(line1, type(line1))

# line2 = f.readline()
# print(line2, type(line2))

# line3 = f.readline()
# print(line3, type(line3))

# We can also use a for loop to read all lines in a file.

line = f.readline()
while (line != ""):
    print(line)
    line = f.readline()

f.close()