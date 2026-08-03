# 8. Write a program to make a copy of a text file “this.txt”
with open("this.txt") as f:
    content = f.read()

# Open (or create) the file "this_copy.txt" in write mode.
with open("this_copy.txt", "w") as f:

    # Write the contents copied from "this.txt" into "this_copy.txt"
    f.write(content)