class employee():
    language = "python"
    salary = 100000

fawad = employee()
fawad.language = "javascript"
print(fawad.language, fawad.salary)  


# Here, instance attributes prevail over class attributes.
# object attributes are also called instance attributes.
