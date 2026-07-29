f = open("file.text")

lines = f.readlines()   # readlines() → Read all lines and return them as a list.

print(lines, type(lines))

f.close()