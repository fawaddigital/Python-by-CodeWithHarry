a = int(input("Enter number 1: "))

b = int(input("Enter number 2: "))

print("Number a is: ", a)
print("Number b is: ", b)
print("Sum is ", a + b)    # Suppose a=10 and b=20, the answer suppose to be 30 but its shows 1020. It is because we are adding two Strings. To avoid this put 'int' before input function.