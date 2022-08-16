
class car:
    def __init__(self,year,speed):
        self.year = year
        self.speed = speed
    def Speed(self):
        print("Speed:",self.speed)
        print("Launch Year:",self.year)

BMW = car(2022,150)
FORD = car(2020,160)

BMW.Speed()
FORD.Speed()

class car:
    def __init__(self,name,year,speed):
        self.name = name
        self.year = year
        self.speed = speed
        return
    def Speed(self):
        
        print("Name : " ,self.name)
        print("Speed: ",self.speed)
        print("Launch Year: ",self.year)
        return
print("\n")
name = input("Enter Name : ")
speed = int(input("Enter speed ""kmph"))
year = int(input("Enter launch year : "))
print("\n")
car1 = car(name,year,speed)
car1.Speed()

print("\n")
name = input("Enter Name : ")
speed = int(input("Enter speed ""kmph"))
year = int(input("Enter launch year : "))
print("\n")
car2 = car(name,year,speed)
car2.Speed()







