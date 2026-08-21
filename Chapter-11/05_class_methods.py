class Employee:
    a = 1

    @classmethod    # classmethod is used to define a method that is bound to the class and not the instance of the class. It can access class attributes and methods.

    def show(cls):
        print(f"The class attribute of a is: {cls.a}")

e = Employee()
e.a = 45

e.show()    # This will print 45 because the instance attribute 'a' overrides the class attribute 'a'.