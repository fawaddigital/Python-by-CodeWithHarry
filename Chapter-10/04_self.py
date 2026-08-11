class employee:
    company = "Google"
    language = "Python"

#    Here we defines a  function inside the class employee.
    def getinfo(self):  
        print(f"The name of the commpany is {self.company} and language is {self.language}")

    @staticmethod 
    def greet():
    # def greet(self):    # if we don't pass (self) as a parameter in the greet function then it will give an error.
        print("Good Morning")

fawad = employee()  
fawad.getinfo()     
fawad.greet()

'''
A static method is a method that belongs to a class
but does not use the object's data (self) or the class's data (cls).
'''