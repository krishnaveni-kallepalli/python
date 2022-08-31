#display all the records in a file “python.txt” along with line/record number?
fh=open("python.txt","r")
count=0
rec=""
while True:
    rec=fh.readline()
    if rec=="":
        break
    count=count+1
    print(count,rec)
fh.close()
