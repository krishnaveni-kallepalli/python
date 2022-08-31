# This will print every line one by one in the file
'''
file = open('python.txt', 'r')
for each in file:
    print (each)
'''
# Python code to illustrate read() mode
'''
file = open("file.txt", "r")
print (file.read())
'''
# Python code to illustrate read() mode character wise
#the following code the interpreter will read the first five characters of stored data and return it as a string
'''
file = open("file.txt", "r")
print (file.read(5))
'''
# Python code to create a file
'''
file = open('python.txt','w')
file.write("This is the write command\n")
file.write("It allows us to write in a particular file\n")
file.close()
'''
# Python code to illustrate append() mode
'''
file = open('python.txt','a')
file.write("This will add this line\n")
file.close()
'''
# Python code to illustrate with() 
'''
with open("python.txt") as file: 
    data = file.read()
# do something with data
'''
# Python code to illustrate with() alongwith write() - override content
'''
with open("python.txt", "w") as f:
    f.write("Hello World!!!")
'''

# Python code to illustrate split() function
'''
with open("python.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)
'''














