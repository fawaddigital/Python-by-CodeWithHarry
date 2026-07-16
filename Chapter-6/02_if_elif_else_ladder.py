'''
    An if-elif-else ladder is used to check multiple conditions one by one. Python executes the block of the first true condition and skips the rest.
'''

a = int(input("Enter your Age: "))

# if elif else ladder 

if(a>=18):
    print("You are above the age of consent")

elif(a<0):
    print("You are entering an invalid negative age")

elif(a==0):
    print("You have entered 0 which is invalid age")

else:
    print("You are below the age of consent")

print("End of program")