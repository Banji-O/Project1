# Reading and writing files


# write

f = open("D:\\AI Engineering\\Python\My_Projects\\Project1\\python.txt", "w")
f.write("Learning python from scratch,")
f.close()

# append
f = open("D:\\AI Engineering\\Python\My_Projects\\Project1\\python.txt", "a")
f.write(" because I need to use it for AI.")
f.close()

# New line
f = open("D:\\AI Engineering\\Python\My_Projects\\Project1\\python.txt", "a")
f.write("\nThis will let me become an AI engineer.")
f.close()

# Read file
f = open("D:\\AI Engineering\\Python\My_Projects\\Project1\\funny.txt", "r")
print(f.read())
f.close()

# Read file line by line
f = open("D:\\AI Engineering\\Python\My_Projects\\Project1\\funny.txt", "r")
for line in f:
    tokens = line.split(' ')
    print(str(tokens))
    print(len(tokens))
f.close()

# Read file line by line and add word count
f = open("D:\\AI Engineering\\Python\My_Projects\\Project1\\funny.txt", "r")
f_write = open("D:\\AI Engineering\\Python\My_Projects\\Project1\\funny_wordCount.txt", "w")
for line in f:
    tokens = line.split(' ')
    f_write.write(" wordcount:"+str(len(tokens)) + line)
f.close()
f_write.close()

# With statement is used for file to close automatically
with open("D:\\AI Engineering\\Python\My _Projects\\Project1\\funny.txt", "r") as f:
    print(f.read())
    print(f.closed)

