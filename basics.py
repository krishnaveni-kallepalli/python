'''
#cretae a class
class Employee:
    salary = 10000
    name = "krishna"
 
emp1 = Employee()
print(emp1.salary)
print(emp1.name)

#create a empty class

class Employee:
    pass

e = Employee()
print(e)
e.name = "krishna"
print(e.name)

#class using type
e1 = type('Employee', (), {})()
print(e1)
 
e1.name = "krishna"
print(e1.name)

class Employee:
        def __init__(self, salary, name):
                self.salary = salary
                self.name = name
 
 
emp1 = Employee(10000, "Krishna")
print(emp1.salary)
print(emp1.name)

#change val of obj
class Employee:
    def __init__(self, salary, name):
        self.salary = salary
        self.name = name
 
 
emp1 = Employee(10000, "John Doe")
print(emp1.salary)
 
emp1.salary = 20000
print(emp1.salary)

#delete obj 

class Employee:
    def __init__(self, salary, name):
        self.salary = salary
        self.name = name
 
 
emp1 = Employee(10000, "Krishna")
 
del emp1.salary
del emp1            


class Vehicle:
    def __init__(self):
        self.trucks = []

    def add_truck(self, truck):
        self.trucks.append(truck)


class Truck:
    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return "{}".format(self.color)


def main():
    v = Vehicle()
    for t in 'Red Blue Black'.split():
        t = Truck(t)
        v.add_truck(t)
    print(v.trucks)


if __name__ == "__main__":
    main()
#bank account  :
class Account:
    def __init__(self,balance):
        self.balance = balance
        return

    def withdraw(self, amount):
        print("Withdrawing.... : ", amount)
        print("Avail balance : ", self.balance)
        if amount<=self.balance :
            self.balance = self.balance - amount
            print("Please collect the cash  : ",amount)
        else:
            print("error : Lowbalance ")
        return

amount = int(input("Enter total available amount : "))
acc = Account(amount)
print("balance : ",acc.balance)
amount = int(input("Enter amount to withdraw : "))
acc.withdraw(amount)
print("Final balance : ", acc.balance)
#create data attributes
class Employee:
    pass
 
 
emp1 = Employee()
setattr(emp1, 'Salary', 12000)
 
emp2 = Employee()
setattr(emp2, 'Age', 25)
 
print(emp1.Salary)
print(emp2.Age)


'''










