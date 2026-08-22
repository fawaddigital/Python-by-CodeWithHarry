class Employee:
    a = 1

    @classmethod    
    def show(cls):
        print(f"The class attribute of a is: {cls.a}")

    @property   # property is used to define a method that can be accessed like an attribute. It allows us to define getter and setter methods for a class attribute.
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter    # name.setter is used to define a setter method for the property 'name'. It allows us to set the value of 'name' and automatically split it into first name and last name.
    def name (self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45

e.name = "fawad khan"
print(e.name)

e.show()  