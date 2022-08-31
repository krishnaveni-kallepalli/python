def uppercount():
    upper=0
    f1=open("python.txt",'r')
    line=f1.read()
    for i in line:
        if (i.isupper()):
            upper+=1
    print("Total no. of upper-case alphabets :",upper,"\n")
uppercount()
