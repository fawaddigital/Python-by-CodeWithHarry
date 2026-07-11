    #   Negative slicing starts from -1

name = "fawad"

print(name[0:3])

print(name[-4:-1])
print(name[1:4])

print(name[:4])     # Is same as print(name[0:4])
print(name[1:])     # Is same as print(name[1:5])

    # SLICING WITH SKIP VALUE 
name1  = "fawadalikhan"
print(name1[1:6:2])     # 1:6 means print these number with skip value of 2.

name2 = "0123456789"
print(name2[1:9:3])     # skip value is 3.
