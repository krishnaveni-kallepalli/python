'''
class A:
    def __init__(self):
        print("I'm super node")
        return
class B(A):
    def fun(self):
        print("I'm subnode")
        return
obj = B()
obj.fun()
'''


class A:
    def __init__(self):
        print("I'm super node 1")
        return
class B:
    def __init__(self):
        print("I'm supernode 2")
        return
class C(A,B):
    def fun(self):
        print("I'm subnode")
        return
obj = C()
obj.fun()
 
