# 3. Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?

class Demo:
    a = 10

r = Demo()
print(r.a)  # Output: 10    Because the class attribute a is 10, so it will print 10.

r.a = 0     # Here we changed the class attribute a to 0 using the object r.
print(r.a)  # Output: 0

# Now if we print the class attribute a using the class name Demo, it will still be 10.
# Because we changed the class attribute a using the object r, it will not change the class attribute a.
print(Demo.a)  # Output: 10