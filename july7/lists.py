
#list is in ascending order or not
list1=[1,2,3,4,5,6,7,8]
temp_list = list1[:]
list1.sort()
if temp_list == list1:
    print("Ascending Order")
else:
    print("Not Ascending Order")
#interchage elements
list5 = [1, 29, 51, 9, 17, 6, 7, 23]
list5[0], list5[-1] = list5[-1], list5[0]
print(list5)
#print even nums
list2 = [1,2,3,4,5,6,7,8]
for i in list2:
    if i % 2 == 0:
        print(i)
#print odd nums
list2 = [1,2,3,4,5,6,7,8]
for i in list2:
    if i % 2 != 0:
        print(i)
#merge 2 lists
list3 = [1,3,4,6]
list4 = [10,11,12,13]
list3.extend(list4)
print(list3)
#subtract list
a = [1,2,3,4,5]
b = [1,2]
l1 = []
for i in a:
    if i not in b:
        l1.append(i)
print(l1)
#print odd occurance of elements
x = [1,2,3,4,5,1,3,3,4]
l1 = []
for i in x:
    if x.count(i) % 2 != 0:
        if i not in l1:
            l1.append(i)
print(l1)









