x = {
  1: "krishna",
  2: "TS",
  3: 1964
}
y={"a":"1",
   "b":"2"
   }
a=0
def dict_methods(x,y):
    z=x.copy()
    print("1.copy",z)
    z=x.get(2)
    print("2.get",z)
    z=x.items()
    print("3.items",z)
    z=x.keys()
    print("4.keys",z)
    z=x.pop(2)
    print("5.pop",z)
    z=y.popitem()
    print("6.popitem",z)
    z=y.setdefault("b","thundersoft")
    print("7.setdefault",z)
    x.update({"color": "White"})
    print("8.update",x)
    z=x.values()
    print("9.values",z)
    x=dict.fromkeys(x, y)
    print("10.fromkeys",x)
    z=x.clear()
    print("11.clear",z)
    
dict_methods(x,y)
