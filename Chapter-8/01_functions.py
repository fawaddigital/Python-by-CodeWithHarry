"""
    A function is a block of code that performs a specific task. You can write it once and use it many times
    
    Why use functions?
        Avoid repeating code.
        Make programs easier to read.
        Make code easier to maintain.
"""
'''
BASIC SYNTEX!
def function_name():
    # code to execute
'''
def avg():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))

    avg = (a+b+c)/3
    print(avg)

# Calling a function
avg()
avg()
avg()