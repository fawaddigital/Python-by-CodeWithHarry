# For Loop with Else

# The else block of a for loop executes when the loop finishes normally without encountering a break statement.

l = [1, 5, 18]

for values in l:
    print(values)
else: 
    print("done")


# Else block will not execute if there is a break statement
# Using break

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed! ")

# The else block does not execute because the loop was terminated by break.
