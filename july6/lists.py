
#creating list
list=[1,2,3]
print(list)
# empty list
l1=[]
print(l1)
# list with mixed data types
l2=[1,"Python",35.8]
print(l2)
# nested list
l3=["krishnaveni",[8,4,6],['a','b']]
print(l3)
#indexing
print(l3[0][1])
l=[1,2,3,4,5,6,7]
print(l[-1])
print(l[-5])
#slicing
i=['zero','one','two','three','four','five']
print(i[2:4])
#index 1 to index 4
print(l[1:4])
#index 4 to end
print(l[4:])
#begin to end
print(l[:])
#changiong values
l=[2,4,6,8]
print(l)
l[0] = "hi"            
print(l)
l[1:4] = [1,2,3]  
print(l)
# Append and Extend list
l=[9,8,7,6,4]
l.append(7)
print(l)
l.extend([10,0,13])
print(l)
# Concatenate and repeat
l=[1,2,3,4,5]
print(l+[9,17,12])
print(["py"]*2)
#insert
l= [1,2]
l.insert(10,13)
print(l)
l[2:2]=[15,7]
print(l)
# Deleting
l= ['p', 'y', 't', 'h', 'o', 'n']
#one item
del l[2]
print(l)
#multiple items
del l[1:3]
print()
#entire list
del l

#remove
l= ['p', 'y', 't', 'h', 'o', 'n']
l.remove('p')
print(l)
#pop
print(l.pop(1))
print(l)
print(l.pop())
print(my_list)
#clear
l.clear()
print(l)

#index count

l=[1,5,1,5,2,3,4,5,6,7,'q','r','s']
l.append(['a','b'])
print(l)

print(l.index('r'))
print(l.count(5))


