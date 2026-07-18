# A for loop is used to iterate over a sequence (such as a list, tuple, string, or range) and execute a block of code for each item.

for i in  range(4): # The range() function is used to generate a sequence of number. 
    print(i)
print("First loop ends here: ")

# Using range(start, stop)
for i in range(2,8):
    print(i)
print("Second loops end here: ")

# Using range(start, stop, step)
for i in range(1, 20, 3):      # Here 3 means skip 3 values.
    print(i)
    