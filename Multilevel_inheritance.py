class A:
    def __init__(self):
        print("I'm super node")
        return
class B(A):
    def fun1(self):
        print("I'm subnode 1")
        return
class C(B):
    def fun2(self):
        print("I'm subnode 2")
        return
    
obj = B()
obj.fun1()
obj = C()
obj.fun2()
