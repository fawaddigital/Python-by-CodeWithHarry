class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):     # operator overloading is used to define the behavior of the '+' operator for instances of the Number class. Here, it allows us to add two Number objects together by adding their 'n' attributes.
        return self.n + num.n

n = Number(2)
m = Number(3)

print(n + m)


# Other operator overloading methods include:
# __sub__ for subtraction (-)
# __mul__ for multiplication (*)
# __truediv__ for division (/)
# __floordiv__ for floor division (//)
# __mod__ for modulus (%)
# __pow__ for exponentiation (**)