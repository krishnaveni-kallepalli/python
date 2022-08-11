
s={1,2,3,6,4}
y={7,4,8,0}
a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
print("s =",s)
print("y =",y)
def set_methods(s,y,a,b):
    s.add(23)
    print("1.add",s)
    s.copy()
    print("2.copy",s)
    x=s.difference(y)
    print("3.difference",x)
    s.add(334)
    x=s.difference_update(y)
    print("4.difference_update",x)
    s.discard(4)
    print("5.discard",s)
    a=a.intersection(b)
    print("6.Intersection",a)
    a=a.union(b)
    print("7.union",a)
    z = a.isdisjoint(b)
    print("8.isdisjoint",z)
    z=a.issubset(b)
    x=s.issubset(y)
    print("9.issubset",x)
    x=s.issuperset(y)
    print("10.issuperset",x)
    print("9.issubset",z)
    x=a.issuperset(b)
    print("10.issuperset",x)
    x=a.pop()
    print("11.pop",x)
    z= a.symmetric_difference(b)
    print("12.symm_diff",z)
    z= a.symmetric_difference_update(b)
    print("13.symm_diff_update",z)
    b.add("carrot")
    z=a.update(b)
    print("14.update",z)
    x=s.intersection_update(y)
    print("15.Intersectionupdate",x)
    x=a.remove("apple")
    print("16.remove",x)
    x=s.clear()
    print("17.clear",x)
set_methods(s,y,a,b)








