class student:
    def __init__(self,name,rollno,percentage):
        self.name = name
        self.rollno = rollno
        self.percentage = percentage
    def details(self):
        print("NAME : ",self.name)
        print("Roll No :",self.rollno)
        print("Percentage : ",self.percentage)

student1 = student("krish",355,99)
student2 = student("kittu",356,89)
student1.details()
student2.details()


class student:
    def __init__(self,name,rollno,percentage):
        self.name = name
        self.rollno = rollno
        self.percentage = percentage
    def details(self):
        print("NAME : ",self.name)
        print("Roll No :",self.rollno)
        print("Percentage : ",self.percentage)
        return

name = input("Enter Name : ")
rollno = int(input("Enter Roll.No : "))
percentage = int(input("Enter percentage: "))

student1 = student(name,rollno,percentage)
student1.details()

name = input("Enter Name : ")
rollno = int(input("Enter Roll.No : "))
percentage = int(input("Enter percentage : "))

student2 = student(name,rollno,percentage)
student2.details()
