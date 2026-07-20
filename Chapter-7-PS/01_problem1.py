# 1. Write a program to print multiplication table of a given number using for loop. 
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} X {i} = {n * i}")

    # {n} prints the value of n
    # {i} prints the value of i
    # {n * i} calculates and prints n multiplied by i