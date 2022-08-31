#reads this text file and prints only the numbers or digits in the file.
fh=open("python.txt","r")                                                     
rec=fh.read();
for a in rec:
    if a.isdigit():
        print(a,end=' ')
fh.close()
