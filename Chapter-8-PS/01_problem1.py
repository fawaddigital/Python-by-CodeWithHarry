# 1. Write a program using functions to find greatest of three numbers. 

def greatest(a, b, c):
    if(a>b and a>c):
        print("A is greator")
        return a
    
    elif(b>a and b>c):
        print("B is greator")
        return b
    
    elif(c>a and c>b):
        print("C is greator")
        return c

a = 3
b = 8
c = 18

print(greatest(a, b, c))