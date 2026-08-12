class employee():
    company = "Google"
    language = "Python"

    # __init__(self) is called a constructor method that is automatically called whenever an object of the class is created.
    def __init__(self):
        print("I am creating an object.")

    @staticmethod
    def greet():
        print("Good Morning")

fawad = employee()
print(fawad.company, fawad.language)

ali = employee()