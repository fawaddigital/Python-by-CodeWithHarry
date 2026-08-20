class Employee:
    def __init__(Self):
        print("Constructor of employee")
    a = 1

class Programmer(Employee):
    def __init__(Self):
        print("Constructor of Programmer")
    b = 2

class Manager(Programmer):
    def __init__(Self):
        super().__init__()  # Super() is used to call the constructor of the parent class. Here, manager parent class is programmer.
        print("Constructor of Manager")
    c = 3

# o = Employee()
# print(o.a)  # Print the value of 'a' from Employee class

# o = Programmer()
# print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)