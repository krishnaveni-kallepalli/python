class A:
    def __init__(self):
        print("I'm super node")
        return
class B(A):
    def fun1(self):
        print("I'm subnode 1")
        return
class C(A):
    def fun2(self):
        print("I'm subnode 2")
        return
class D(A):
    def fun3(self):
        print("I'm subnode 3")
        return
obj = B()
obj.fun1()
obj = C()
obj.fun2()
obj = D()
obj.fun3()
  
