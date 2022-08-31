#write content into the file through user input
def program():
    f = open("intro.txt","w")
    text=input("Enter the text:")
    f.write(text)
    f.close()

#user input in 3 newlines
def program1():
    f = open("MyFile.txt","w")
    line1=input("Enter the text:")
    line2=input("Enter the text:")
    line3=input("Enter the text:")
    new_line="\n"
    f.write(line1)
    f.write(new_line)
    f.write(line2)
    f.write(new_line)
    f.write(line3)
    f.write(new_line)
    f.close()
    
#merge content in 2 files to 3rd file    
def program3():
    with open("MyFile.txt","r") as f1:
       data=f1.read()
    with open("intro.txt","r") as f2:
        data1=f2.read()
    with open("merge.txt","w") as f3:
        f3.write(data)
        f3.write(data1)

#Replace all spaces from text with – (dash)

def program2():
    cnt = 0
   # n = int(input("Enter no. characters to read:"))
    with open("merge.txt","r") as f1:
       data = f1.read()
       data=data.replace(' ','-')
    with open("merge.txt","w") as f1:
        f1.write(data)

program()
program1()
program3()
program2()    








