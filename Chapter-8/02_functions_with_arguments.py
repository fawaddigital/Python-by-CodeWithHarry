'''
Function with Arguments:
Definition: A function with arguments is a function that receives values (arguments) when it is called.
'''

# Syntax
# def function_name(parameter):
    # code

# Example:
def greet(name):
    print("Hello,", name)

greet("Fawad")
greet("Ali")

'''
    name is a parameter (defined in the function).
    "Fawad" is an argument (passed when calling the function).
'''

# Function with Two arguments.
def func1(name, ending):
    print("Hello,", name)
    print(ending)

# Calling function with two or more values.
func1("Fawad", "Thanks")
func1("Ali", "Thanks")