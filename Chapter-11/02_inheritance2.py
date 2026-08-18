class Employee:
    company = "Samsung"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")

    
class programmer(Employee):
    company = "Microsoft"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

a = Employee()
b = programmer()
print(a.company, b.company)
