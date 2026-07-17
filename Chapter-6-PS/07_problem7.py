# 7. Write a program to find out whether a given post is talking about “Harry” or not. 

post = input("Enter the  post: ")

if("Harry".lower() in post.lower()):
    print("Harry is in a post")
else:
    print("Harry is not in a post")