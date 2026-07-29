st = "Fawad ali khan is a good boy"

f = open("myfile.txt", "a")  # "a" → Append mode. It will add content to the end of the file without overwriting existing content.

f.write(st)

f.close()