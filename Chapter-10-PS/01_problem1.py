# 1. Create a class “Programmer” for storing information of few programmers
# working at Microsoft.

class programmer():
    company = "Microsoft"

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language

ali = programmer("Fawad", 100000, "Python")
print(ali.company, ali.name, ali.salary, ali.language)

ali = programmer("Ali", 100000, "Python")
print(ali.company, ali.name, ali.salary, ali.language)

