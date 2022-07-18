
#STRING
print("Hello")
print('Hello')
#Assign String to a Variable
a="HELLO"
print(a)
#Multiline Strings

a = '''Hello Python,
Hello,
world,
WELCOME'''

print(a)

a = "Hello""World!"
print(a)
#ARRAY REPRESENTATION 
a = "HelloWorld!"
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
#USING LOOPS
for x in "banana":
  print(x)

#String Length
a = "Hello PYTHON!"
print(len(a))
#FIND STRING in OR not in TEXT
a = "Hello PYTHON!"
print("PY" in a)
print("hy" not in a)

if "PY" in a:
      print("PY is in a")
if "hy" not in a:
      print("hy is not in a")

#Slicing
print(a[2:5])
print(a[:5])
print(a[2:])
print(a[-5:-2])

#methods
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("H","h"))
print(a.split(","))

#String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

c = a + " " + b
print(c)

#Format
age = 22

txt = "My name is Krish, I am " + age
print(txt)


txt = "My name is Krish, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 56
price = 4.95

myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#escape sequence
txt = "Welcome to the \"world\" of programming"
print(txt)

txt = "Welcome to the \'world\' of programming"
print(txt)
txt = "Welcome to the \\world\\ of programming"
print(txt)
txt = "Welcome to the \nworld of programming"
print(txt)
txt = "Welcome to the \bworld of programming"
print(txt)
txt = "Welcome to the \rworld of programming"
print(txt)
txt = "Welcome to the \tworld of programming"
print(txt)
txt = "Welcome to the \fworld of programming"
print(txt)
txt = "\110\145\154\154\157"
print(txt)
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)

















