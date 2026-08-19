class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

o = Employee()
print(o.a)  # Print the value of 'a' from Employee class
# print(o.b)  # This will raise an AttributeError since 'b' is not defined in Employee

o = Programmer()
print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)