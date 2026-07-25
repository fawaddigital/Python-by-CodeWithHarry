# 2. Write a python program using function to convert Celsius to Fahrenheit. 

def f_to_c(f):
    # Convert Fahrenheit value to Celsius using the formula C = 5(F−32)/9.
    return 5*(f-32)/9

f = int(input("Enter temperature in F: "))
c = (f_to_c(f))

# Print the Celsius temperature rounded to 2 decimal places.
print(f"{round(c, 2)}°C")
