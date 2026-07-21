# 6. Write a program to calculate the factorial of a given number using for loop. 
# 5! = 5 × 4 × 3 × 2 × 1 = 120

n = int(input("Enter a number: "))
product = 1

for i in range(1, n+1):
    # Multiply product by the current value of i
    product = product * i

print(f"The factorial of {n} is {product}")