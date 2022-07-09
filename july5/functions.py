
#max of 2 nums
def max(a,b):
    if a>b:
        return a
    else:
        return b
#area of circle
r=int(input("enter radius"))
def circle(r):
    pi=3.14
    return pi*(r*r)
print(circle(r))

#calculator
a=int(input())
b=int(input())
print("Maximum num is",max(a,b))

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
a=int(input("Enter a:"))
b=int(input("Enter b:"))
ch=int(input("Enter choice(1/2/3/4):"))

if ch==1:
    print(add(a,b))
elif ch==2:
    print(sub(a,b))
elif ch==3:
    print(mul(a,b))
elif ch==4:
    print(div (a,b))
else:
    print("None")

#find nth fibonacci num
n=int(input("Enter n:"))
def fib(n):
    if n<=0:
        print("Incorrect input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(n))

#sum of n nums
n=int(input("enter n:"))
def sqsum(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
        return sum
print(sqsum(n))
#sumof squares on n natural nums
n=int(input("enter n:"))
def sqsum(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+(i*i)
        return sum
print(sqsum(n))
#cube sum of n natural nums
n=int(input("enter n:"))
def sqsum(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+(i*i*i)
        return sum
print(sqsum(n))

#print all prime nums
s=int(input("Enter start:"))
e=int(input("Enter end:"))
def prime(s,n):
    for i in range(s,e+1):
        if i>1:
            for j in range(2,i):
                if(i%j==0):
                    break;
            else:
               print(i)
prime(s,e)

#find sum of array
def _sum(arr):
    sum=0
    for i in arr:
        sum=sum+i
    return sum

arr=[12,3,4,15]
n=len(arr)
result=_sum(arr)
print('sum of arr is' ,result)

#find minimum sum of factors
def minsum(sum):
    sum=0
    i=2
    while((i*i) <= num):
        while(num%i==0):
            sum=sum+i
            num=num/i
        i=i+1
    sum=sum+num
    return sum
num=int(input("enter num:"))
print(minsum(sum))
