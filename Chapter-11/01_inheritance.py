# What is inheritance in Python?
# Inheritance is a way of creating a new class from an existing class.
# It allows the new class (Child class) to inherit attributes and methods from the existing class (Parent class).

# Example:
class Parent:   # Parent/Base Class
    def greet(self):
        print("Hello!")

class child(Parent):     # Child/Derived class
    pass

# Create an object of the Child class
obj = child()

# Call the inherited greet() method from the Parent class.
obj.greet()     

# Output: Hello!