'''
5. Write a python function to print first n lines of the following pattern: 

*** 
**               
* -  for n = 3

'''
def patttern(n):
    if(n==0):
        return
    print("*" * n)
    patttern(n - 1)

patttern(3)